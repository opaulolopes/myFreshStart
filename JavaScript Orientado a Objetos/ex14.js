var input = '025468';
var output = '';

for (c = 0; c < input.length; c++) {
    currentDigit = Number(input.charAt(c))
    nextDigit = Number(input.charAt(c + 1))
    if (currentDigit % 2 == 0 && nextDigit % 2 == 0) {
        output += currentDigit + '-'
    } else {
        output += currentDigit
    }
}
console.log(output)