// De acordo com a Wikipedia, um número feliz é definido pelo seguinte processo:
// "Começando com qualquer número inteiro positivo, substitua o número pela soma dos quadrados de seus dígitos e repita o processo até que o número seja igual a 1 (onde ficará) , ou faz um loop infinito em um ciclo que não inclui 1. Aqueles números para os quais esse processo termina em 1 são números felizes, enquanto aqueles que não terminam em 1 são números infelizes (ou números tristes)".
// Escreva um programa JavaScript para encontrar e imprimir os 5 primeiros números felizes.
function getSum(num) {
    let sum = 0;
    while (num != 0) {
        sum = sum + num % 10;
        num = parseInt(num / 10);
    }
    return sum;
}

for (num = 1; num <= 10; num++)
    console.log(getSum(num))