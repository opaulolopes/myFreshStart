# Por Didática Tech
# Para atribuir variáveis, será utilizado <-
a <- 5
b <- 'Paulo'

# Para atribuir funções, será utilizado =
# Funções fazem parte de um pacote
# Pacotes têm muitas funções e precisam ser instalados

c <- c(a,b)
a <- c(10,5,15,20)
a[1]

# Para Help, utiliza-se ?
?c

# Para dados da varivável, chama-se o summary
summary(a)
summary(c)

# Não sendo um pacote padrão, o pacote precisa ser chamado (rdocumentation.org)
?str_c

install.packages('stringr')
library(stringr)

Nome <- 'Paulo'
Sobrenome <- 'Lopes'

NomeCompleto <- str_c(Nome, ' ', Sobrenome)

# Dados numéricos
Salario <- 1444
Horas <- 25
SH <- Salario/Horas
?SHint <- as.integer(SH)
SHround <- round(SH)

# Quantas vezes a variável aparece
CargaHoraria <- c(220,220,150,100,100)
summary(CargaHoraria)

CargaHoraria <- as.factor(CargaHoraria)
summary(CargaHoraria)
mode(CargaHoraria)
class(CargaHoraria)

# Listas
a <- c(1,2,3,4,5)
b <- c(1,"2",3,4,5)
b <- as.numeric(b)

b <- c(1,"a",3,4,5)
b <- as.numeric(b)

is.list(a)
is.list(b)

is.vector(a)
is.vector(b)

b <- list(10,"2",8)
is.list(b)
mode(b)
class(b)
str(b)

e <- list(c(10,6,51,5),"2",8)
str(e)
e[[3]]
e[[1]][3]

# Matrizes
m <- matrix(1:9, nrow = 3)
m
mode(m)
class(m)

m[1,3]
m[1,3] <- "a"
