# Infográficos

Cada infográfico mora na própria pasta, com tudo que ele precisa dentro dela:

```
infograficos/
  ileo-biliar/
    index.html
    assets/
      rx-pneumobilia.png
  sequestro-esplenico/
    index.html
```

## Como adicionar um

1. Crie a pasta com um *slug* curto, sem acento e sem espaço — ela vira a URL:
   `infograficos/ileo-biliar/` → `…/infograficos/ileo-biliar/`
2. O arquivo principal chama-se **`index.html`**. É isso que faz a URL ficar limpa,
   sem `.html` no fim.
3. Imagens ficam em `assets/` dentro da própria pasta, referenciadas por caminho
   relativo (`assets/rx.png`). Nada de caminho absoluto — quebra no GitHub Pages.
4. Adicione um cartão para a peça na seção **Infográficos** do `index.html` da raiz.

## O que colocar no `<head>`

Isso é o que faz a peça aparecer decente quando alguém compartilha o link:

```html
<title>Íleo biliar — tríade de Rigler | MedRam</title>
<meta name="description" content="Pneumobilia, obstrução mecânica e cálculo ectópico.">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

## Duas coisas que valem a disciplina

**Referência ao lado da afirmação.** É o que separa o material do resto — e é o
que permite corrigir sem refazer, quando a evidência muda.

**Diga quando a fonte não alcança.** Como na peça de erupções acneiformes, onde a
diretriz da AAD de 2024 exclui o tema do próprio escopo: registrar isso custa
espaço e não deixa a arte mais bonita, mas é a diferença entre ensinar e afirmar.

## Direitos de imagem

Imagem de terceiro só entra com crédito visível na peça. Se a licença não permitir
redistribuição, prefira redesenhar o achado em SVG a hospedar o original — além de
resolver o direito, um vetor fica nítido em qualquer tamanho e é editável depois.
