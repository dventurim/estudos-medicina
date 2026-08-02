# MedRam — Memória Clínica

Infográficos e cards clínicos construídos sobre literatura primária. Um tema por peça, com o raciocínio inteiro visível — semiologia, fisiopatologia, algoritmo de decisão e a armadilha que derruba a questão de prova.

**Daniel Venturim Ramos** — Faculdade de Medicina, Universidade Federal de Minas Gerais (UFMG), desde 2018.
[ORCID 0000-0002-1910-6062](https://orcid.org/0000-0002-1910-6062) · [Currículo Lattes](http://lattes.cnpq.br/1211641598704539) · [@medramnews](https://www.instagram.com/medramnews/) · [Blog](https://medram-news.blogspot.com/)

## 🌐 Galeria

### **https://dventurim.github.io/medram/**

No ar. Cada peça tem endereço próprio e permanente:

| Peça | Endereço |
| --- | --- |
| Hipocalemia e ECG | [`/infograficos/hipocalemia-ecg/`](https://dventurim.github.io/medram/infograficos/hipocalemia-ecg/) |
| Crise de sequestro esplênico | [`/infograficos/sequestro-esplenico/`](https://dventurim.github.io/medram/infograficos/sequestro-esplenico/) |
| Hipocalemia grave e PPT (card) | [`/cards/hipocalemia-ppt/`](https://dventurim.github.io/medram/cards/hipocalemia-ppt/) |

Cada peça mora na própria pasta, com tudo que precisa dentro dela, e o arquivo principal chama-se sempre `index.html` — é isso que deixa a URL limpa (`…/cards/hipocalemia-ppt/`, sem `.html` no fim).

<details>
<summary>Estrutura de pastas</summary>

```
index.html                        galeria (a página que o Pages serve)
baralho/
  index.html                      MedRam Cards — amostra e lista de espera
  assets/                         imagens da página
cards/
  hipocalemia-ppt/
    index.html                    o card
    support.js                    runtime dos Design Components
    assets/ecg.png                ECG do caso 183 do Wave-Maven
infograficos/
  README.md                       como adicionar uma peça
  hipocalemia-ecg/index.html
  sequestro-esplenico/index.html
```

</details>

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
