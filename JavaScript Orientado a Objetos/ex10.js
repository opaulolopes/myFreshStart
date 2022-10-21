var n1 = 3
var n2 = 5
var sum = 0;
for (c = 1; c < 1000; c++) {
    if (c % n1 == 0 && c % n2 == 0) {
        sum += c;
    }
}
console.log(`A soma dos múltiplos de ${n1} e ${n2} abaixo de 1000 é ${sum}.`)