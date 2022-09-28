function mostraNome() {
    console.log('Paulo declaração')
}
mostraNome()

// Em funções do tipo expressão, o içamento não funciona, ou seja, se apresentar a função antes de sua declaração, ela não será conhecida.
var mostrarNome = function () {
    console.log('Paulo expressão')
}
mostrarNome()

var mostreNome = function (nome) {
    return nome
}

var nome = mostreNome('Paulo')
console.log(nome)

var showNome = function (nome, sobreNome) {
    var qtd = arguments.length
    var nomeCompleto = ''

    while (qtd > 0) {
        nomeCompleto += ' ' + arguments[qtd]
        qtd--
    }
    console.log(nomeCompleto)
    return arguments[1]
}
var nome = showNome('Paulo', 'Lopes', 'Filho')
console.log(nome)