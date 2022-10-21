function SquareSum(num) {
    units = num % 10;
    tens = (num - units) % 100;
    hundreds = (num - tens - units) % 1000;
    sum = units ** 3 + (tens/10) ** 3 + (hundreds/100) ** 3;
    return sum
}

for(num = 100; num<1000; num++) {
    SquareSum(num)
    if (num == sum) {
        console.log(num)
    }
}