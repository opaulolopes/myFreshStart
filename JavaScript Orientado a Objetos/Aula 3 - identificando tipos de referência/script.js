/*
Instanceof: é usado para testar o tipo de dado;

typeof: mostra o tipo de dado de alguma variável ou qualquer outra coisa
*/

function mostraNome() {
    return 'Paulo'
}
// SOBRESCREVENDO
var mostraNome = {'nome':'Paulo'}

var teste = (typeof mostraNome)
if(teste === 'function') {
    var recebeNome = mostraNome()
} else {
    console.log('mostraNome não é uma função.')
}

console.log(recebeNome)
console.log(teste)

function showName() {
    return 'Sérgio'
}

if(showName instanceof Function) {
    var nome = showName()
}

console.log(nome)