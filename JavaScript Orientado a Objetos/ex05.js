// Escreva um programa JavaScript que itere os inteiros de 1 a 100. Mas para múltiplos de três imprima "Fizz" em vez do número e para os múltiplos de cinco imprima "Buzz". Para números que são múltiplos de três e cinco, imprima "FizzBuzz".
for (c = 1; c <= 100; c++) {
    if(c%3==0 && c%5==0) {
        console.log('FizzBuzz')
    } else if(c%3==0) {
        console.log('Fizz')
    } else {
        console.log(c)
    }
}