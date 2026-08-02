# Estudos de Medicina

Materiais de estudo — cards clínicos, ECGs e resumos.

## Cards

### Card PPT Hipocalemia

Card de ECG sobre **hipocalemia grave e paralisia periódica tireotóxica (PPT)**.

| Arquivo | O que é |
| --- | --- |
| `Card PPT Hipocalemia.dc.html` | O componente: template `x-dc` + classe `DCLogic` |
| `support.js` | O `dc-runtime` que o card carrega via `script src` |
| `assets/ecg.png` | ECG de 12 derivações, 1350×900 |
| `assets/800x400.gif` | O mesmo traçado em resolução menor (não referenciado pelo card) |

O card traz o K⁺ sérico no cabeçalho, a figura do ECG, um batimento esquemático em SVG (achatamento de T, onda U, fusão T–U) e três seções numeradas — achados no ECG, fisiopatologia e tratamento — fechando com a pérola.

**Props** (definidas em `data-props`, viram CSS custom properties na raiz):

- `paletteLead` — `Terracota` / `Sálvia`
- `shapeStyle` — `Redondo` / `Suave` / `Nítido`
- `decorShapes` — liga/desliga as formas de fundo

**Para visualizar:** o card precisa ser servido por HTTP (o runtime faz `fetch` do próprio arquivo, o que não funciona em `file://`):

```bash
python3 -m http.server 8000
# abrir http://localhost:8000/Card%20PPT%20Hipocalemia.dc.html
```

## Fonte do ECG

O traçado é o **caso 183** do [ECG Wave-Maven](https://ecg.bidmc.harvard.edu), do Beth Israel Deaconess Medical Center — K⁺ 1,9 mEq/L, taquicardia sinusal em repouso com prolongamento do PR, ondas P em DII sobrepostas às ondas TU, ondas U muito amplas (V3–V4), diagnóstico de paralisia periódica tireotóxica.

Imagem © Beth Israel Deaconess Medical Center, todos os direitos reservados. Mantida aqui em repositório privado para uso pessoal de estudo, com crédito à fonte na legenda do card.
