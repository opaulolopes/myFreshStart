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

Object.defineProperty(pessoa, 'idade', {
    enumerable: false,
    configurable: false
});

Object.defineProperty(pessoa, 'nome', {
    enumerable: false,
    configurable: false,
    value: 'Paulo',
    writable: false
});

// Não vai ser deletado por causa da propriedade definida acima.
delete pessoa.nome;

// Vai retornar um erro porque a propriedade não pode ser redefinida.
// Object.defineProperty(pessoa, 'nome', {
//     configurable: true
// });

console.log(pessoa);
console.log(pessoa.propertyIsEnumerable('idade'));

for (propriedade in pessoa) {
    console.log(propriedade)
}