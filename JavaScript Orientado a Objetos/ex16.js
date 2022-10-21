function isString(param) {
    if (typeof(param) === 'string') {
        return true
    }
    return false
}

console.log(isString('w3resource'))
console.log(isString([1, 2, 4, 0]))