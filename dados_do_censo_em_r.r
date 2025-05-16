install.packages("readr")
install.packages("dplyr")
install.packages("stringr")
library(readr)
library(dplyr)
library(stringr)

dados <- read.csv2(
  file = "D:\\rafaeloliveira\\Documents\\Dados\\Demografia\\Dados_Censo_Envio\\Dados_TI\\dados_ind1.csv",
  encoding = "latin1",
  colClasses = c(
    codigo_ibge = "integer",
    municipio = "character",
    total_2010 = "character",
    branca_2010 = "character",
    preta_2010 = "character",
    amarela_201 = "character",
    parda_201 = "character",
    indigena_2010 = "character",
    total_2022 = "character",
    branca_2020 = "character",
    preta_2022 = "character",
    amarela_2022 = "character",
    parda_2022 = "character",
    indigena_2022 = "character"
  ),
  check.names = FALSE
)

colunas_numericas <- c("total_2010", "branca_2010", "preta_2010", "amarela_201", 
                       "parda_201", "indigena_2010", "total_2022", "branca_2020",
                       "preta_2022", "amarela_2022", "parda_2022", "indigena_2022")

dados[colunas_numericas] <- lapply(dados[colunas_numericas], function(x) {
  x[x == "-"] <- NA
  as.numeric(gsub(",", ".", x))  
})

dados[colunas_numericas][is.na(dados[colunas_numericas])] <- 0

dados <- dados %>%
  mutate(
    municipio_nome = str_match(municipio, "^(.+?)\\s*\\((..)\\)$")[,2],
    uf = str_match(municipio, "^(.+?)\\s*\\((..)\\)$")[,3]
  )

dados <- dados %>%
  select(
    codigo_ibge,
    municipio = municipio_nome,  
    uf,
    everything(),
    -municipio,       
    -municipio_nome   
  )

dados <- dados %>%
  select(
    codigo_ibge,
    municipio = municipio_nome,
    uf,
    total_2010,
    branca_2010,
    preta_2010,
    amarela_201,
    parda_201,
    indigena_2010,
    total_2022,
    branca_2020,
    preta_2022,
    amarela_2022,
    parda_2022,
    indigena_2022
  )

head(dados)

dados_povos_indigenas <- dados %>%
  select(
    codigo_ibge,
    total_2010,
    indigena_2010,
    total_2022,
    indigena_2022
    )
dados_povos_indigenas<- dados_povos_indigenas %>%
  filter(str_starts(as.character(codigo_ibge), "51"))

dados_povos_indigenas <- dados_povos_indigenas %>%
  mutate(
    variacao_percentual = (indigena_2022 - indigena_2010) / indigena_2010
  )
head(dados_povos_indigenas)
