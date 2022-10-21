function isBlank(param) {
    if (param === '') {
        return true
    }
    return false
}

console.log(isBlank(''))
console.log(isBlank('abc'))