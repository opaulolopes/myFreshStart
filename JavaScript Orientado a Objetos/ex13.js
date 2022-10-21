var names = ['Paulo', 'Julia', 'Tania', 'Jose', 'Mariana']

function firstArrayElement(arr, num = 1) {
    if (num < 0) {
        num = 0
    }
    return arr.slice(0, num);
}

console.log(firstArrayElement(names.concat, 2))