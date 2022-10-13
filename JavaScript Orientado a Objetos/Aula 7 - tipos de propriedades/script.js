var pessoa = {
    nome: 'Emilia',
    _idade: 16,
    genero: 'Agênere',
    casada: false,
    // Propriedade de acesso: declaração explícita de getter
    get idade() {
        return this._idade;
    },
    // Propriedade de acesso: declaração explícita de setter
    set idade(value) {
        this._idade = value;
    }
};

// Declaração implícita de setter
pessoa.idade = 21
// Declaração implícita de getter
console.log(pessoa.idade);