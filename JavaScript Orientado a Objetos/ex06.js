function happy_number(num) {
    var remainderSquare, remainderPart;
    var c = [];

    while (num != 1 && c[num] !== true) {
        c[num] = true;
        while (num > 0) {
            remainderPart = num % 10;
            remainderSquare = remainderPart ** 2;
            num = (num - remainderPart) / 10;
        }
        num = remainderSquare;
    }
    return (num == 1);
}

var num = 1;
var counter = 5;
var first5 = '';
while (counter-- > 0) {
    while (!happy_number(num))
        num++;
    first5 += (" " + num);

    num++;
}
console.log('First 5 happy numbers are' + first5);