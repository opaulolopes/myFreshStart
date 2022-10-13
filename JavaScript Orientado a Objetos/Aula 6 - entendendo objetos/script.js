var pessoa = {};
pessoa.nome = 'Emilia';
pessoa.idade = 16;
pessoa.genero = 'Agênere';
pessoa.casada = false;

delete pessoa.idade;

if ('casada' in pessoa){
    delete pessoa.casada;
}

for (propriedade in pessoa) {
    console.log(propriedade);
    console.log(pessoa[propriedade]);
}

console.log(pessoa.hasOwnProperty('casada'));
console.log(pessoa);

var i, size;
var propriedade = Object.keys(pessoa);

for (i = 0, size = propriedade.length; i < size; i++) {
    console.log(propriedade[i])
    console.log(pessoa[propriedade[i]])
}
console.log(propriedade)