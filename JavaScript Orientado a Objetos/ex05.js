for (c = 1; c <= 100; c++) {
    if(c%3==0 && c%5==0) {
        console.log('FizzBuzz')
    } else if(c%3==0) {
        console.log('Fizz')
    } else {
        console.log(c)
    }
}