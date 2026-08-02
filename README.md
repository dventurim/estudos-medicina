# MedRam — Memória Clínica

Infográficos e cards clínicos construídos sobre literatura primária. Um tema por peça, com o raciocínio inteiro visível — semiologia, fisiopatologia, algoritmo de decisão e a armadilha que derruba a questão de prova.

**Daniel Venturim Ramos** — Faculdade de Medicina, Universidade Federal de Minas Gerais (UFMG), desde 2018.
[ORCID 0000-0002-1910-6062](https://orcid.org/0000-0002-1910-6062) · [Currículo Lattes](http://lattes.cnpq.br/1211641598704539) · [@medramnews](https://www.instagram.com/medramnews/) · [Blog](https://medram-news.blogspot.com/)

## 🌐 Galeria

O conteúdo está pronto para o GitHub Pages servir. Faltam **dois** passos, nesta ordem.

**1. Resolver o domínio.** Hoje `dventurim.github.io` responde `301` para `http://venturim.me/…`, porque o repositório `dventurim.github.io` tem um domínio próprio configurado — e `venturim.me` não resolve. Enquanto isso valer, ligar o Pages não adianta: a URL redireciona para um endereço que não existe.

- **Caminho rápido:** em `dventurim.github.io` → *Settings → Pages → Custom domain*, apagar `venturim.me`. A galeria passa a atender em `https://dventurim.github.io/estudos-medicina/`.
- **Caminho bonito:** reativar `venturim.me` e apontar o DNS para o GitHub. A galeria fica em `https://venturim.me/estudos-medicina/`.

**2. Ligar o Pages neste repositório:** *Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`*.

Feito isso, atualize o endereço aqui e o badge **Acervo** no [README do perfil](https://github.com/dventurim/dventurim).

## 📂 Estrutura

```
index.html                        galeria (a página que o Pages serve)
cards/
  hipocalemia-ppt/
    index.html                    o card
    support.js                    runtime dos Design Components
    assets/ecg.png                ECG do caso 183 do Wave-Maven
infograficos/
  README.md                       como adicionar uma peça
```

Cada peça mora na própria pasta, com tudo que precisa dentro dela, e o arquivo principal chama-se sempre `index.html` — é isso que deixa a URL limpa (`…/cards/hipocalemia-ppt/`, sem `.html` no fim).

## 🩺 Peças

### Hipocalemia grave e paralisia periódica tireotóxica

`cards/hipocalemia-ppt/` — ECG de 12 derivações, batimento esquemático em SVG com a fusão T–U, os cinco achados eletrocardiográficos, a bomba Na⁺/K⁺-ATPase por trás do shift, e o ponto que muda conduta: repor K⁺ com cautela, porque o potássio corporal total é normal e o rebote é real.

O card é um Design Component — o template fica no `<x-dc>` e a lógica numa classe `DCLogic`, que expõe três props compiladas em CSS custom properties:

| Prop | Valores | Efeito |
| --- | --- | --- |
| `paletteLead` | `Terracota` · `Sálvia` | qual das duas paletas lidera |
| `shapeStyle` | `Redondo` · `Suave` · `Nítido` | escala de border-radius |
| `decorShapes` | `true` · `false` | formas decorativas de fundo |

## 🔧 Rodando localmente

O runtime faz `fetch` do próprio arquivo, o que não funciona em `file://`. Sirva por HTTP:

```bash
python3 -m http.server 8000
# galeria:  http://localhost:8000/
# o card:   http://localhost:8000/cards/hipocalemia-ppt/
```

## 📖 Fontes e direitos

Cada peça cita a literatura que a sustenta, ao lado da afirmação — não numa lista solta no rodapé.

O ECG do card de hipocalemia é o **caso 183** do [ECG Wave-Maven](https://ecg.bidmc.harvard.edu), do Beth Israel Deaconess Medical Center: K⁺ 1,9 mEq/L, taquicardia sinusal em repouso com prolongamento do PR, ondas P em DII sobrepostas às ondas TU, ondas U muito amplas em V3–V4, paralisia periódica tireotóxica. Imagem © Beth Israel Deaconess Medical Center, creditada na legenda do card.

---

Material de estudo. Não se destina a orientar conduta em paciente individual.
