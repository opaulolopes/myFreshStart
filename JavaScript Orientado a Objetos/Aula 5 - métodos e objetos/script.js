var pegarNome = function (nome) {
    console.log(this.nome);
};

var pessoa = {
    nome: 'Agnes',
    sobrenome: 'Alves',
    idade: '23',
    getNome: pegarNome
}

var carros = {
    nome: 'Volvo',
    marca: 'Volkswagen',
    getNome: pegarNome
}

pessoa.getNome();
carros.getNome();

// Alteração da variável var
var pegarNome = function (nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    console.log(this);
}

pegarNome.call(pessoa, 'Paulo', 'Lopes');
pegarNome.apply(pessoa, ['Paulo', 'Lopes']);
var getNome = pegarNome.bind(pessoa, ['Paulo', 'Lopes']);
getNome()