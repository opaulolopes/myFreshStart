# Trabalhando com bases de dados

# Definindo área de trabalho
setwd("/Users/paulolopes/Documents/GitHub/myFreshStart/R")

# Importanto base de dados
df <- read.csv("DataFrame.csv")

# Analisando um data frame
View(df)
# Tipos de dados
str(df)
summary(df)

# Selecionando variáveis
df
df[6]
df$John

Col1 <- df[1]
Col2 <- df$John

class(df$John)
class(Col2)
class(Col1)

# Modificando o DF
## Excluindo variável
df$X120.jefferson.st. <- NULL

## Alterando o tipo da variável
df$John
summary(df$John)
df$John <- as.factor(df$John)
df$John
summary(df$John)

## Criando uma nova variável
df$Nova <- "a"
df$Nova <- c(2,5,10, NA, NA)
df$Nova <- NULL
df$Nova <- NA
df$Nova[1:3] <- c(2,5,10)
class(df$Nova)
