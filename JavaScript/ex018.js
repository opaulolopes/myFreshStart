let num = [5, 8, 2, 9, 3]
num[2] = 10
num.push(7)
num.length
num.sort()

console.log(`Nosso vetor é o ${num}`)
console.log(`O primeiro valor do vetor é ${num[0]}`)
console.log(`O vetor tem ${num.length} posições`)
console.log(`Nosso vetor em ordem crescente é ${num.sort()}`)
for (let pos = 0; pos < num.length; pos++) {
    console.log(`A posição ${pos} tem o valor ${num[pos]}`)
}
for (pos in num) {
    console.log(`A posição ${pos} tem o valor ${num[pos]}`)
}
console.log(`O valor 10 está na posição ${pos}`)