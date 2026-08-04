#!/usr/bin/env python3
"""Troca a folha de estilo do Google Fonts por @font-face embutido em data URI.

Por que: uma peça que depende de CDN não é permanente. Se o Google mudar a URL,
se a rede cair, ou se alguém abrir o arquivo salvo em disco, a tipografia cai
para o fallback em silêncio — e a peça muda de cara sem avisar. Embutindo, o
arquivo passa a ser a peça inteira.

O subconjunto é montado a partir dos caracteres que a peça realmente usa (mais
um conjunto-base latino, para caber correção de texto depois sem regerar tudo),
o que costuma derrubar cada família de dezenas de KB para menos de dez.

Uso:
    python3 tools/embed-fonts.py infograficos/*/index.html cards/*/index.html

Requer: pip install fonttools brotli
"""

import base64
import io
import pathlib
import re
import sys
import urllib.request
from html.parser import HTMLParser

from fontTools.subset import Options, Subsetter
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# Conjunto-base: português + os símbolos que os diagramas usam. Entra sempre,
# mesmo que a peça atual não use, para que editar um rótulo não exija regerar.
BASE_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    "ÁÀÂÃÉÊÍÓÔÕÚÜÇáàâãéêíóôõúüçÑñ"
    " .,;:!?()[]{}-–—·|/\\'\"“”‘’%+*=<>&@#°ºª…•_^~$"
    "→←↑↓≤≥≈×✕✓⁺²₂₁"
)

# Eixos que a peça nunca varia: fixar derruba a tabela de variação inteira.
# O eixo de peso fica livre, porque as peças usam mais de um.
PIN_AXES = {"Newsreader": {"opsz": 18}}

GF_LINK = re.compile(r"[ \t]*<link[^>]*fonts\.(?:googleapis|gstatic)\.com[^>]*>\n?", re.I)
GF_HREF = re.compile(r'<link[^>]*href="(https://fonts\.googleapis\.com/css2\?[^"]+)"', re.I)
GF_CSS = "https://fonts.googleapis.com/css2?family={}&display=swap"


def as_weight_range(spec: str) -> str:
    """`Space+Grotesk:wght@400;500;600;700` → `Space+Grotesk:wght@400..700`.

    Pedir pesos soltos devolve uma estática por peso; pedir a faixa devolve uma
    variável só, que pesa quase o mesmo que uma delas. As tuplas são agrupadas
    pelos outros eixos, para `ital` continuar separando romano de itálico.
    """
    if ":" not in spec:
        return spec
    name, _, axis_part = spec.partition(":")
    axes, _, values = axis_part.partition("@")
    axis_list = axes.split(",")
    if "wght" not in axis_list:
        return spec
    at = axis_list.index("wght")

    groups: dict[tuple, list[str]] = {}
    for tup in values.split(";"):
        parts = tup.split(",")
        if len(parts) != len(axis_list):
            return spec
        groups.setdefault(tuple(parts[:at] + parts[at + 1:]), []).append(parts[at])

    out = []
    for others, weights in groups.items():
        flat = [w for spec_w in weights for w in spec_w.split("..")]
        if not all(w.isdigit() for w in flat):
            return spec
        lo, hi = min(int(w) for w in flat), max(int(w) for w in flat)
        rng = str(lo) if lo == hi else f"{lo}..{hi}"
        parts = list(others)
        parts.insert(at, rng)
        out.append(",".join(parts))
    return f"{name}:{axes}@{';'.join(sorted(out))}"


def fetch_css(spec: str) -> str:
    """Busca o CSS de uma família, preferindo a variável e caindo para o pedido original."""
    for candidate in dict.fromkeys([as_weight_range(spec), spec]):
        req = urllib.request.Request(GF_CSS.format(candidate), headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req) as r:
                return r.read().decode()
        except urllib.error.HTTPError:
            continue  # família sem versão variável: tenta o pedido como veio
    raise RuntimeError(f"Google Fonts recusou {spec!r}")


class TextHarvester(HTMLParser):
    """Junta os nós de texto que chegam à tela (fora de script e style)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.chunks.append(data)


def latin_faces(css: str):
    """Devolve (família, estilo, peso, url) de cada @font-face do subconjunto latino."""
    for block in re.findall(r"@font-face\s*\{(.*?)\}", css, re.S):
        if "U+0000-00FF" not in block:
            continue
        yield (
            re.search(r"font-family:\s*'([^']+)'", block).group(1),
            re.search(r"font-style:\s*(\w+)", block).group(1),
            re.search(r"font-weight:\s*([\d\s]+);", block).group(1).strip(),
            re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1),
        )


def build_face(family: str, style: str, weight: str, url: str, chars: str) -> tuple[str, int]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as r:
        font = TTFont(io.BytesIO(r.read()))

    if family in PIN_AXES and "fvar" in font:
        instantiateVariableFont(font, PIN_AXES[family], inplace=True, updateFontNames=False)

    opts = Options()
    opts.flavor = "woff2"
    opts.hinting = False
    opts.desubroutinize = True
    opts.layout_features = ["kern", "liga", "calt", "tnum"]
    sub = Subsetter(options=opts)
    sub.populate(text=chars)
    sub.subset(font)

    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    payload = buf.getvalue()
    b64 = base64.b64encode(payload).decode()
    rule = (
        f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
        f"font-display:block;src:url(data:font/woff2;base64,{b64}) format('woff2');}}"
    )
    return rule, len(payload)


def embed(path: pathlib.Path) -> None:
    html = path.read_text()

    if "data:font/woff2" in html:
        print(f"{path}: já embutido, pulando")
        return
    href = GF_HREF.search(html)
    if not href:
        print(f"{path}: sem folha do Google Fonts, pulando")
        return

    harvester = TextHarvester()
    harvester.feed(html)
    chars = "".join(sorted(set(BASE_CHARS) | set("".join(harvester.chunks))))

    specs = re.findall(r"family=([^&]+)", href.group(1))

    rules, total, seen = [], 0, set()
    for spec in specs:
        for family, style, weight, url in latin_faces(fetch_css(spec)):
            if (family, style, weight) in seen:
                continue
            seen.add((family, style, weight))
            rule, size = build_face(family, style, weight, url, chars)
            rules.append(rule)
            total += size
            print(f"  {family} {style} {weight}: {size // 1024} KB")

    if not rules:
        print(f"{path}: nenhuma face latina encontrada, nada a fazer")
        return

    out = GF_LINK.sub("", html)
    block = "<style>\n" + "\n".join(rules) + "\n</style>\n"
    out = out.replace("<style>", block + "<style>", 1)
    path.write_text(out)
    print(f"{path}: {len(rules)} faces, {total // 1024} KB de fonte "
          f"({len(html) // 1024} KB → {len(out) // 1024} KB)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for arg in sys.argv[1:]:
        embed(pathlib.Path(arg))
