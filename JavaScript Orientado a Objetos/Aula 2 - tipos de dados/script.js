// TIPOS PRIMITIVOS
var idade = 18
var sexo = 'f'
var nome = 'Paulo'
var existe = true
var endereco = null
var primeiroChar = nome.charAt(2)
var nomeMaiusculo = nome.toUpperCase()

console.log(typeof idade)
console.log(typeof sexo)
console.log(typeof nome)
console.log(typeof existe)
console.log(typeof endereco)
console.log(endereco === null)
console.log(!!existe)
console.log(primeiroChar)
console.log(nomeMaiusculo)
console.log(idade.toFixed(2))

// TIPOS DE REFERÊNCIA
var pessoa = new Object()
var pessoa2 = {
    'nome': 'Paulo',
    'idade': '24',
    'sexo': 'M'
}

// FORMAS DE CRIAÇÃO DE FUNÇÕES
console.log(typeof pessoa)
var mostraNome = new Function("console.log('Paulo')")
mostraNome()

function mostraIdade() {
    console.log('Idade é igual a ' + 15)
}
mostraIdade()

// FORMAS DE CRIAÇÃO DE ARRAYS
var carro = new Array('Gol', 'Uno', 'Corolla')
console.log(carro)

var carros = ['Gol', 'Uno', 'Corolla']
console.log(carros)