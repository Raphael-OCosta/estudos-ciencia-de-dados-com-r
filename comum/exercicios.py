"""Exercícios práticos em R criados para estudar o livro, um ou mais por seção.

Formato: (capítulo, início do título da seção, nome, enunciado em Markdown, solução em R).
Usam bases que vêm com o R e com os pacotes (mtcars, iris, airquality, starwars, mpg, economics,
nycflights13, Titanic). Os exemplos são originais: complementam os exercícios do próprio livro.
"""

EXERCICIOS = [
    # ---------------- 2. Conceitos básicos ----------------
    (2, "Objetos", "Objetos e tipos",
     "Crie `nome` (texto), `idade` (número), `estuda` (lógico) e um vetor `notas` com 4 notas. "
     "Mostre a classe de cada um com `class()` e a média das notas.",
     r'''nome <- "Ana"; idade <- 31; estuda <- TRUE; notas <- c(7.5, 8, 9.2, 6.8)
sapply(list(nome = nome, idade = idade, estuda = estuda, notas = notas), class)
mean(notas)'''),
    (2, "Funções", "Sua primeira função",
     "Escreva `imc(peso, altura)` que devolve o IMC arredondado em 1 casa e outra `classifica_imc(imc)` que devolve "
     "\"abaixo\", \"normal\" ou \"acima\" (limites 18,5 e 25). Teste com 3 pessoas.",
     r'''imc <- function(peso, altura) round(peso / altura^2, 1)
classifica_imc <- function(x) ifelse(x < 18.5, "abaixo", ifelse(x < 25, "normal", "acima"))
v <- imc(c(50, 70, 95), c(1.70, 1.75, 1.80))
data.frame(imc = v, faixa = classifica_imc(v))'''),
    (2, "Pacotes", "Carregando pacotes",
     "Mostre a versão dos pacotes `dplyr`, `ggplot2` e `tidyr` com `packageVersion()` e liste quais pacotes estão "
     "carregados na sessão (`.packages()`).",
     r'''sapply(c("dplyr", "ggplot2", "tidyr"), function(p) as.character(packageVersion(p)))
.packages()'''),

    # ---------------- 3. Lendo os dados ----------------
    (3, "Tipos de Estrutura", "Vetor, matriz, lista e data frame",
     "Crie um exemplo de cada estrutura (vetor, matriz 2×3, lista com elementos de tipos diferentes e data frame "
     "com 3 colunas) e use `str()` em cada um.",
     r'''v <- 1:5; m <- matrix(1:6, 2); l <- list(a = 1, b = "texto", c = TRUE)
df <- data.frame(id = 1:3, cidade = c("SP", "RJ", "BH"), pop = c(12.3, 6.7, 2.5))
for (x in list(v, m, l, df)) str(x)'''),
    (3, "Pacote para leitura", "Ler um CSV com readr",
     "Escreva a base `airquality` num CSV temporário (`tempfile(fileext = \".csv\")`) e leia de volta com "
     "`read_csv`. Quantas linhas, colunas e valores `NA` existem?",
     r'''arq <- tempfile(fileext = ".csv")
write_csv(airquality, arq)
aq <- read_csv(arq, show_col_types = FALSE)
c(linhas = nrow(aq), colunas = ncol(aq), NAs = sum(is.na(aq)))'''),

    # ---------------- 4. Manipulando os dados ----------------
    (4, "Tipos de Variáveis", "Convertendo tipos",
     "O vetor `x <- c(\"10\", \"20\", \"trinta\", \"40\")` veio como texto. Converta para número, conte quantos "
     "viraram `NA` e transforme `c(\"baixo\", \"alto\", \"médio\", \"alto\")` em fator com a ordem baixo < médio < alto.",
     r'''x <- c("10", "20", "trinta", "40")
n <- suppressWarnings(as.numeric(x)); n; sum(is.na(n))
f <- factor(c("baixo", "alto", "médio", "alto"), levels = c("baixo", "médio", "alto"), ordered = TRUE)
f; table(f)'''),
    (4, "If e Else", "Faixa de consumo",
     "Para cada carro do `mtcars`, classifique o consumo (`mpg`) em \"econômico\" (≥ 25), \"médio\" (≥ 18) ou "
     "\"gastão\", primeiro com `if/else` dentro de uma função e depois com `case_when`. Os resultados batem?",
     r'''faixa <- function(m) if (m >= 25) "econômico" else if (m >= 18) "médio" else "gastão"
a <- sapply(mtcars$mpg, faixa)
b <- case_when(mtcars$mpg >= 25 ~ "econômico", mtcars$mpg >= 18 ~ "médio", TRUE ~ "gastão")
all(a == b); table(b)'''),
    (4, "Loops", "for, while e a versão vetorizada",
     "Some os quadrados de 1 a 1.000 com `for`, com `while` e com `sum((1:1000)^2)`. Meça o tempo da versão `for` "
     "e da vetorizada com `system.time` para 1 a 1e6.",
     r'''s1 <- 0; for (i in 1:1000) s1 <- s1 + i^2
s2 <- 0; i <- 1; while (i <= 1000) { s2 <- s2 + i^2; i <- i + 1 }
c(s1, s2, sum((1:1000)^2))
system.time({ s <- 0; for (i in 1:1e6) s <- s + i^2 })["elapsed"]
system.time(sum((1:1e6)^2))["elapsed"]'''),
    (4, "Manipulações com R base", "Filtrar e ordenar sem pacotes",
     "Só com R base: em `mtcars`, pegue os carros com 6 cilindros, mostre `mpg`, `hp` e `wt`, ordene por `mpg` "
     "decrescente e crie a coluna `potencia_por_peso = hp / wt`.",
     r'''d <- mtcars[mtcars$cyl == 6, c("mpg", "hp", "wt")]
d <- d[order(-d$mpg), ]
d$potencia_por_peso <- d$hp / d$wt
d'''),
    (4, "Pacote dplyr", "O mesmo com dplyr",
     "Refaça o exercício anterior com `filter`, `select`, `arrange` e `mutate`. Depois, para todos os carros, "
     "calcule por número de cilindros: quantidade, média de `mpg` e máximo de `hp`.",
     r'''mtcars |> filter(cyl == 6) |> select(mpg, hp, wt) |> arrange(desc(mpg)) |> mutate(potencia_por_peso = hp / wt)
mtcars |> group_by(cyl) |> summarise(n = n(), mpg_medio = mean(mpg), hp_max = max(hp))'''),
    (4, "Pacote dplyr", "Personagens de Star Wars",
     "Com `dplyr::starwars`: qual é a espécie com mais personagens? Qual é a altura média por gênero (ignorando NA)? "
     "Quem é o personagem mais pesado de cada planeta natal com 2 ou mais personagens?",
     r'''starwars |> count(species, sort = TRUE) |> head(3)
starwars |> group_by(gender) |> summarise(altura_media = mean(height, na.rm = TRUE))
starwars |> filter(!is.na(homeworld), !is.na(mass)) |> group_by(homeworld) |> filter(n() >= 2) |>
  slice_max(mass, n = 1) |> select(homeworld, name, mass)'''),

    # ---------------- 5. Limpando dados ----------------
    (5, "O formato ideal", "Dados arrumados (tidy)",
     "A tabela `notas <- data.frame(aluno = c(\"Ana\", \"Bia\"), prova1 = c(7, 9), prova2 = c(8, 6))` está no formato "
     "largo. Explique num comentário por que ela não é *tidy* e converta para o formato longo com `pivot_longer`.",
     r'''notas <- data.frame(aluno = c("Ana", "Bia"), prova1 = c(7, 9), prova2 = c(8, 6))
# "prova" é uma variável, mas está espalhada nos nomes das colunas
notas |> pivot_longer(starts_with("prova"), names_to = "prova", values_to = "nota")'''),
    (5, "Pacote tidyr", "pivot_wider, separate e valores ausentes",
     "Com `airquality`: calcule a temperatura média por mês (`Month`) e passe para o formato largo, com um mês "
     "por coluna. Depois, separe `c(\"2024-05-10\", \"2023-11-02\")` em ano, mês e "
     "dia com `separate_wider_delim` e troque os `NA` de `Ozone` pela mediana com `replace_na` (cuidado: `Ozone` é inteiro e a mediana pode ter decimais).",
     r'''airquality |> group_by(Month) |> summarise(temp = mean(Temp)) |> pivot_wider(names_from = Month, values_from = temp, names_prefix = "mes_")
tibble(data = c("2024-05-10", "2023-11-02")) |> separate_wider_delim(data, "-", names = c("ano", "mes", "dia"))
aq <- airquality |> mutate(Ozone = replace_na(as.numeric(Ozone), median(Ozone, na.rm = TRUE)))
sum(is.na(aq$Ozone))'''),
    (5, "Manipulação de texto", "Limpando textos com stringr",
     "Limpe o vetor `c(\"  São Paulo \", \"rio de JANEIRO\", \"Belo   Horizonte\")`: tire espaços extras, deixe só a "
     "1ª letra de cada palavra maiúscula, conte as letras de cada nome e extraia os números de "
     "`c(\"pedido 123\", \"nota 4567\")`.",
     r'''cid <- c("  São Paulo ", "rio de JANEIRO", "Belo   Horizonte")
limpo <- str_to_title(str_squish(cid)); limpo
str_length(str_remove_all(limpo, " "))
as.numeric(str_extract(c("pedido 123", "nota 4567"), "\\d+"))'''),

    # ---------------- 6. Juntando dados ----------------
    (6, "União de dados", "Empilhando tabelas",
     "Crie as vendas de janeiro e de fevereiro (2 data frames com as mesmas colunas) e empilhe com `bind_rows`, "
     "guardando de qual mês veio cada linha (`.id`).",
     r'''jan <- data.frame(produto = c("A", "B"), qtd = c(10, 4))
fev <- data.frame(produto = c("A", "C"), qtd = c(7, 2))
bind_rows(jan = jan, fev = fev, .id = "mes")'''),
    (6, "Cruzamento", "Joins com voos",
     "Com `nycflights13`: junte `flights` com `airlines` para ter o nome da companhia, calcule o atraso médio de "
     "chegada por companhia e mostre as 5 piores. Depois use `anti_join` para contar voos cujo avião (`tailnum`) "
     "não está na tabela `planes`.",
     r'''library(nycflights13)
flights |> left_join(airlines, by = "carrier") |> group_by(name) |>
  summarise(atraso_medio = mean(arr_delay, na.rm = TRUE)) |> arrange(desc(atraso_medio)) |> head(5)
flights |> anti_join(planes, by = "tailnum") |> nrow()'''),

    # ---------------- 7. Escrevendo dados ----------------
    (7, "Escrevendo csv", "Salvar e conferir um CSV",
     "Salve o resumo de consumo por cilindros do `mtcars` num CSV temporário com `write_csv`, leia de volta e "
     "confira com `all.equal` que nada mudou.",
     r'''resumo <- mtcars |> group_by(cyl) |> summarise(mpg = mean(mpg))
arq <- tempfile(fileext = ".csv"); write_csv(resumo, arq)
all.equal(as.data.frame(resumo), as.data.frame(read_csv(arq, show_col_types = FALSE)))'''),
    (7, "Rdata", "RDS guarda o objeto inteiro",
     "Transforme `Species` da `iris` em fator ordenado, salve com `saveRDS` e com `write_csv`, leia os dois e mostre "
     "que só o RDS preserva o tipo da coluna.",
     r'''d <- iris |> mutate(Species = factor(Species, ordered = TRUE))
rds <- tempfile(fileext = ".rds"); csv <- tempfile(fileext = ".csv")
saveRDS(d, rds); write_csv(d, csv)
c(rds = class(readRDS(rds)$Species)[1], csv = class(read_csv(csv, show_col_types = FALSE)$Species)[1])'''),
    (7, "Escrevendo outros", "Excel e JSON",
     "Salve as 5 primeiras linhas do `mtcars` em Excel (`writexl::write_xlsx`) e em JSON (`jsonlite::toJSON`) "
     "e mostre o JSON gerado.",
     r'''d <- head(mtcars, 5) |> tibble::rownames_to_column("carro")
writexl::write_xlsx(d, tempfile(fileext = ".xlsx"))
jsonlite::toJSON(d[, 1:4], pretty = TRUE)'''),

    # ---------------- 8. Obtendo dados ----------------
    (8, "API", "Lendo a resposta de uma API (JSON)",
     "Respostas de API costumam vir em JSON. Transforme o texto "
     "`'[{\"cidade\":\"SP\",\"temp\":24},{\"cidade\":\"POA\",\"temp\":17}]'` num data frame com `jsonlite::fromJSON` "
     "e mostre a cidade mais quente. (Para uma API real, troque o texto pela URL.)",
     r'''resp <- '[{"cidade":"SP","temp":24},{"cidade":"POA","temp":17}]'
d <- jsonlite::fromJSON(resp); d
d$cidade[which.max(d$temp)]'''),

    # ---------------- 9. ggplot2 ----------------
    (9, "Mapeamento Estético", "Cor e tamanho mapeados",
     "Com `ggplot2::mpg`, faça a dispersão `displ` × `hwy` com a cor mapeada em `class` e o tamanho em `cyl`.",
     r'''ggplot(mpg, aes(displ, hwy, colour = class, size = cyl)) + geom_point(alpha = 0.7)'''),
    (9, "Objetos geométricos", "Camadas de geoms",
     "No mesmo gráfico, junte `geom_point` e `geom_smooth(method = \"loess\")`; depois faça uma versão com uma "
     "reta por tipo de tração (`drv`).",
     r'''ggplot(mpg, aes(displ, hwy)) + geom_point() + geom_smooth(method = "loess", formula = y ~ x)
ggplot(mpg, aes(displ, hwy, colour = drv)) + geom_point() + geom_smooth(method = "lm", formula = y ~ x, se = FALSE)'''),
    (9, "Escalas", "Escalas e rótulos",
     "Com `economics`, desenhe o desemprego (`unemploy`) ao longo do tempo com eixo y em milhares formatado "
     "(`scales::label_comma`), eixo x de 10 em 10 anos e título.",
     r'''ggplot(economics, aes(date, unemploy)) + geom_line(colour = "steelblue") +
  scale_y_continuous(labels = scales::label_comma(big.mark = ".")) +
  scale_x_date(date_breaks = "10 years", date_labels = "%Y") +
  labs(title = "Desempregados nos EUA (milhares)", x = NULL, y = NULL)'''),
    (9, "Subplots", "Facetas",
     "Repita a dispersão `displ` × `hwy` com um painel por `drv` (`facet_wrap`) e depois uma grade `drv` × `cyl` "
     "(`facet_grid`).",
     r'''ggplot(mpg, aes(displ, hwy)) + geom_point() + facet_wrap(~ drv)
ggplot(mpg, aes(displ, hwy)) + geom_point() + facet_grid(drv ~ cyl)'''),
    (9, "Temas", "Tema próprio",
     "Crie um objeto `meu_tema` baseado em `theme_minimal(base_size = 13)` com legenda embaixo e título em negrito, "
     "e aplique num gráfico de barras de `class`.",
     r'''meu_tema <- theme_minimal(base_size = 13) + theme(legend.position = "bottom", plot.title = element_text(face = "bold"))
ggplot(mpg, aes(class, fill = drv)) + geom_bar() + labs(title = "Carros por classe") + meu_tema'''),
    (9, "Gráficos de Barras", "Barras ordenadas com valores",
     "Mostre o consumo médio na estrada (`hwy`) por fabricante, em barras horizontais ordenadas do maior para o "
     "menor e com o valor escrito em cada barra.",
     r'''mpg |> group_by(manufacturer) |> summarise(hwy = mean(hwy)) |>
  ggplot(aes(reorder(manufacturer, hwy), hwy)) + geom_col(fill = "seagreen") +
  geom_text(aes(label = round(hwy, 1)), hjust = -0.1, size = 3) + coord_flip() + labs(x = NULL)'''),
    (9, "Histogramas", "Histograma × freqpoly",
     "Compare a distribuição de `hwy` por `drv` com um histograma empilhado e com `geom_freqpoly`. Qual fica "
     "mais fácil de ler?",
     r'''ggplot(mpg, aes(hwy, fill = drv)) + geom_histogram(binwidth = 2)
ggplot(mpg, aes(hwy, colour = drv)) + geom_freqpoly(binwidth = 2, linewidth = 1)'''),
    (9, "Boxplots", "Boxplot, jitter e violino",
     "Para `hwy` por `class`, faça um violino com os pontos por cima (`geom_jitter(width = 0.15)`) e um boxplot "
     "ordenado pela mediana.",
     r'''ggplot(mpg, aes(class, hwy)) + geom_violin(fill = "grey90") + geom_jitter(width = 0.15, alpha = 0.5)
ggplot(mpg, aes(reorder(class, hwy, median), hwy)) + geom_boxplot() + labs(x = "class")'''),
    (9, "Cleveland", "Gráfico de pontos de Cleveland",
     "Faça um *dot plot* de Cleveland com a média de `hwy` e de `cty` por fabricante (dois pontos por linha, "
     "ligados por um segmento).",
     r'''d <- mpg |> group_by(manufacturer) |> summarise(cty = mean(cty), hwy = mean(hwy))
ggplot(d, aes(y = reorder(manufacturer, hwy))) + geom_segment(aes(x = cty, xend = hwy, yend = manufacturer), colour = "grey70") +
  geom_point(aes(x = cty), colour = "tomato", size = 3) + geom_point(aes(x = hwy), colour = "steelblue", size = 3) +
  labs(x = "milhas por galão (vermelho = cidade, azul = estrada)", y = NULL)'''),
    (9, "Plotando funções", "Desenhando funções",
     "Desenhe a densidade normal padrão e a t de Student com 3 graus de liberdade no mesmo gráfico, de −4 a 4, "
     "com `geom_function`.",
     r'''ggplot() + xlim(-4, 4) +
  geom_function(fun = dnorm, aes(colour = "Normal")) +
  geom_function(fun = dt, args = list(df = 3), aes(colour = "t (3 g.l.)")) + labs(colour = NULL)'''),
    (9, "Salvando Gráficos", "ggsave",
     "Salve um gráfico como PNG (8×5 polegadas, 150 dpi) num arquivo temporário com `ggsave` e mostre o tamanho "
     "do arquivo em KB.",
     r'''g <- ggplot(mpg, aes(displ, hwy)) + geom_point()
arq <- tempfile(fileext = ".png")
ggsave(arq, g, width = 8, height = 5, dpi = 150)
round(file.size(arq) / 1024)'''),

    # ---------------- 12. Modelos ----------------
    (12, "Modelo Linear", "Regressão linear e resíduos",
     "Ajuste `hwy ~ displ` e `hwy ~ displ + drv` na base `mpg`. Compare o R² ajustado e desenhe os resíduos do "
     "segundo modelo contra os valores previstos.",
     r'''m1 <- lm(hwy ~ displ, mpg); m2 <- lm(hwy ~ displ + drv, mpg)
c(m1 = summary(m1)$adj.r.squared, m2 = summary(m2)$adj.r.squared)
ggplot(data.frame(prev = fitted(m2), res = residuals(m2)), aes(prev, res)) + geom_point() + geom_hline(yintercept = 0, colour = "red")'''),

    # ---------------- 13. Revisão Titanic ----------------
    (13, "Carregando os Dados", "O Titanic que vem no R",
     "A base `Titanic` do R é uma tabela de contagens. Transforme em data frame com uma linha por passageiro "
     "(`as.data.frame` + `tidyr::uncount(Freq)`) e confira que são 2.201 pessoas.",
     r'''tit <- as.data.frame(Titanic) |> uncount(Freq)
nrow(tit); head(tit)'''),
    (13, "Manipulando os dados", "Taxas de sobrevivência",
     "Calcule a taxa de sobrevivência por classe e por sexo, e depois por classe × sexo × idade (criança/adulto).",
     r'''tit <- as.data.frame(Titanic) |> uncount(Freq) |> mutate(sobreviveu = Survived == "Yes")
tit |> group_by(Class) |> summarise(taxa = mean(sobreviveu))
tit |> group_by(Sex) |> summarise(taxa = mean(sobreviveu))
tit |> group_by(Class, Sex, Age) |> summarise(n = n(), taxa = round(mean(sobreviveu), 2)) |> arrange(desc(taxa))'''),
    (13, "Visualizações", "Gráfico da sobrevivência",
     "Faça barras empilhadas em proporção (`position = \"fill\"`) da sobrevivência por classe, com um painel por sexo.",
     r'''tit <- as.data.frame(Titanic) |> uncount(Freq)
ggplot(tit, aes(Class, fill = Survived)) + geom_bar(position = "fill") + facet_wrap(~ Sex) +
  scale_y_continuous(labels = scales::label_percent()) + labs(y = "proporção")'''),
    (13, "Modelo Preditivo", "Regressão logística no Titanic",
     "Separe 70% para treino e ajuste `glm(Survived ~ Class + Sex + Age, family = binomial)`. Calcule a acurácia "
     "nos 30% de teste e compare com o chute \"ninguém sobrevive\".",
     r'''set.seed(1)
tit <- as.data.frame(Titanic) |> uncount(Freq)
i <- sample(nrow(tit), 0.7 * nrow(tit))
m <- glm(Survived ~ Class + Sex + Age, family = binomial, data = tit[i, ])
prev <- ifelse(predict(m, tit[-i, ], type = "response") > 0.5, "Yes", "No")
c(modelo = mean(prev == tit$Survived[-i]), ninguem_sobrevive = mean(tit$Survived[-i] == "No"))'''),
]
