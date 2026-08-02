# Progresso — MedRam Cards

> **Este arquivo é a memória entre as sessões diárias.** Cada sessão começa lendo
> ele e termina atualizando ele. Sem isso, cada dia recomeça do zero.
>
> Ao encerrar uma sessão: mova o que foi feito para o registro, atualize os
> contadores, e escreva a próxima ação de forma que amanhã ela seja executável
> sem precisar reconstruir o raciocínio de hoje.

**Última atualização:** 2026-08-02

---

## 🎯 Onde estamos

**MedRam Cards** — baralho de Anki com cerca de 8.000 flashcards cloze, ~6 GB
com mídia. Em revisão editorial antes da venda. Sem data de lançamento
anunciada, e essa é uma decisão deliberada (ver abaixo).

| Frente | Estado |
| --- | --- |
| Galeria pública | no ar — [dventurim.github.io/medram](https://dventurim.github.io/medram/) |
| Página do produto | no ar — [`/baralho/`](https://dventurim.github.io/medram/baralho/) |
| Amostra publicada | 7 cards (via aérea difícil), clique para revelar |
| Lista de espera | formulário ligado e funcionando |
| Auditoria de imagem | **não iniciada** — Daniel |
| Auditoria de texto | **não iniciada** — falta a exportação |
| Revisão editorial do baralho | em andamento — Daniel |

---

## 🔜 Próxima ação

**Exportar o baralho como texto e mandar para análise.**
No Anki: *Notas → Exportar notas como texto*, sem mídia. O baralho inteiro
deve caber em poucos megabytes. Com isso saem de uma vez: duplicatas, cloze
quebrado, cards sem referência e higiene de tags.

Em paralelo, rodar `auditar_midia.py` na `collection.media` e começar a
triagem pelos baldes `CDN` e `COLADO`, que são poucos e mais prováveis.

---

## 📋 Pendências

- [ ] **Divergência no card 4 do LEMON.** O enunciado pergunta a distância
  "entre a cartilagem tireoide e a mandíbula → 2 dedos". O painel autoral
  publicado na mesma página diz "hioide à cartilagem tireoide · 2". São
  medidas diferentes, e o painel é o que bate com o 3-3-2 clássico. Resolver
  antes que a ilustração nova consolide a versão errada.
- [ ] **Ilustração nova do 3-3-2.** Criada, ainda não anexada como arquivo.
  Imagem colada no corpo da mensagem não chega ao disco — precisa vir como
  `.png` anexado.
- [ ] **Auditoria de procedência da mídia** dos ~8.000 cards, antes de abrir
  venda. Na amostra de 13 imagens, 2 eram arte de publicação e 1 tinha marca
  d'água de gerador.
- [ ] **Currículo Lattes** parado desde 26/10/2022 — sem Liga de Cardiologia,
  MedRam, infográficos nem blog. Decidido: resolver na semana da inscrição da
  prova.
- [ ] **Renomear o tipo de nota** para `MedRam Cloze`. Hoje é
  `Cloze-one by one USPanki (ParmegiAnki / lukammh21)`, que fica visível para
  quem comprar e sugere associação com projetos de terceiros.
- [ ] **Limpar assets do template.** `_AnKingRound.png` e
  `_radiopaedia_links.js` estão referenciados no template do tipo de nota, não
  nos cards — por isso acompanham toda exportação. Removem-se em
  *Ferramentas → Gerenciar tipos de nota → Cartões*.

---

## 🧭 Decisões já tomadas

Registradas para não serem rediscutidas a cada sessão.

**Nome do produto:** MedRam Cards. O repositório e a marca são `medram`
(minúsculo no repo, `MedRam` no texto).

**Sem preço e sem data de lançamento**, só o tamanho (~8.000). O baralho ainda
está em ajuste, e prometer data que escorrega custa credibilidade — que é
exatamente o que o MedRam vende.

**A amostra concentra num só tópico de propósito.** Sete cards do mesmo
mnemônico demonstram o método (um conceito por card) melhor que sete cards
soltos demonstrariam.

**Divisão de trabalho:** Daniel audita a procedência das imagens (o volume não
sobe para a sessão). Claude cuida do texto e de dúvidas pontuais.

**Direito de imagem é questão de venda, não de estudo.** Usar figura de
terceiro para estudar é uma coisa; distribuí-la dentro de um pacote pago é
outra. O caminho preferido para o que for insubstituível é redesenhar em SVG —
resolve o direito e fica melhor que o original.

**Nada de link não testado.** Todo endereço publicado é verificado antes. Já
houve dois casos de link quebrado no ar por pular esse passo.

---

## 📅 Registro

### 2026-08-02
- Galeria MedRam criada e publicada via GitHub Pages; repositório renomeado de
  `estudos-medicina` para `medram`, com as URLs acompanhando.
- Página do produto `/baralho/` publicada: posicionamento, painel LEMON
  autoral, amostra de 7 cards com clique para revelar, argumento do "um
  conceito por card" e formulário de lista de espera.
- Dois infográficos migrados do Instagram para HTML com endereço permanente:
  hipocalemia e ECG, crise de sequestro esplênico.
- Card de hipocalemia e PPT movido para `/cards/hipocalemia-ppt/`; ECG
  identificado como caso 183 do Wave-Maven.
- README do perfil reescrito em torno do MedRam, com ORCID, Lattes e produção
  acadêmica.
- Amostra do baralho analisada: 3 das 13 imagens não deviam ir para peça
  pública paga.
- `auditar_midia.py` entregue para a triagem local.
