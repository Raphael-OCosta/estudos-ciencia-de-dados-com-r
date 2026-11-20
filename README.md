# Estudos — *Ciência de Dados com R: Introdução* (Oliveira, Guerra & McDonnell)

> **A melhor forma de estudar um livro técnico é ler e praticar ao mesmo tempo.**
> Leia uma seção, feche o livro e escreva o código com as próprias mãos. Só depois confira o gabarito.

Este repositório registra meu estudo do livro *Ciência de Dados com R: Introdução*. O livro vai do básico do R ao `tidyverse`, ao `ggplot2`, aos modelos e a um projeto de revisão com o Titanic.
Cada capítulo virou um caderno Jupyter **em R**. As seções têm a página do PDF e, quando cabe, um exercício original. As seções "Exercícios" do livro ganharam uma célula para resolvê-los ali mesmo.

## O método

| Passo | O que fazer | Onde |
|---|---|---|
| 1. Ler | Ler a seção indicada | PDF do livro (página no caderno) |
| 2. Praticar | Fazer o exercício e os exercícios do livro **sem olhar a resposta** | `praticar/capXX_*.ipynb` |
| 3. Conferir | Comparar com o gabarito | `resolvidos/capXX_*.ipynb` |
| 4. Resumir | Explicar com as próprias palavras nas células | `praticar/` |
| 5. Registrar | Commit + push | GitHub |

## Conteúdo (36 exercícios em R)

| Capítulos | Temas praticados |
|---|---|
| 2–4 | objetos e funções, estruturas de dados, `readr`, conversão de tipos, `if/else` × `case_when`, loops × vetorização, R base × `dplyr`, `starwars` |
| 5–8 | dados *tidy*, `pivot_longer`/`pivot_wider`, `separate_wider_delim`, `stringr`, `bind_rows`, joins com `nycflights13`, CSV × RDS, Excel e JSON, JSON de API |
| 9 | `ggplot2`: estética, camadas, escalas, facetas, tema próprio, barras ordenadas, histograma × freqpoly, violino + jitter, Cleveland dot plot, funções, `ggsave` |
| 12–13 | regressão linear e resíduos; Titanic: contagens → passageiros, taxas de sobrevivência, gráfico e regressão logística |

## Melhorias em relação ao livro

- O livro usa o RStudio. Aqui uso **VS Code + Jupyter com kernel R**: leitura, código e anotações no mesmo arquivo.
- Pipe nativo `|>` (R ≥ 4.1) e funções atuais do tidyr: `pivot_*` e `separate_wider_delim`, que substituem `gather`/`spread`/`separate`.
- Só dados que já vêm no R ou nos pacotes (`mpg`, `economics`, `starwars`, `nycflights13`, `Titanic`). Não é preciso baixar arquivos, e os arquivos de exercício vão para `tempfile()`, sem sujar a pasta.
- Gabarito executado inteiro por `ferramentas/testar_cadernos.py` (R 4.6, dplyr/tidyr/ggplot2 atuais).

## Como usar

```powershell
# R 4.x (winget install RProject.R) e Python 3.12 (para o Jupyter)
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r ferramentas\requirements-ferramentas.txt
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"; Rscript ferramentas\instalar_pacotes.R
.venv\Scripts\python.exe ferramentas\testar_cadernos.py   # opcional: roda o gabarito
```

No VS Code, abra `praticar/cap01_introducao.ipynb` → **Select Kernel → Jupyter Kernel… → R**.
O [Guia de Estudos (PDF)](Guia_de_Estudos.pdf) explica o passo a passo.

## Direitos autorais

O livro **não** está neste repositório. Para estudar, use a sua própria cópia.
Os exercícios, os cadernos, os scripts e o guia são autorais e estão sob licença [MIT](LICENSE).
