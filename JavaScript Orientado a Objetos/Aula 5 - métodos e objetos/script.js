var pegarNome = function (nome) {
    console.log(this.nome = nome)
}

var pessoa = {
    nome: 'Paulo',
    idade: '24',
    getNome: pegarNome
}

var carros = {
    nome: 'Gol',
    marca: 'VolksWagen',
    getNome: pegarNome
}

pessoa.getNome()
carros.getNome()

pegarNome.call(pessoa, 'Pedro')