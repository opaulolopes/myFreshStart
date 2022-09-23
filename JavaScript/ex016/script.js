function contar() {
    var inicio = document.getElementById('txti')
    var fim = document.getElementById('txtf')
    var passo = document.getElementById('txtp')
    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
        res.innerHTML = 'Impossível contar!'
        window.alert('[ERRO] Faltam dados!')
    } else {
        res.innerHTML = `Contando: <br>`
        let i = Number(inicio.value)
        let f = Number(fim.value)
        let p = Number(passo.value)
        if (p <= 0) {
            window.alert('Passo inválido!')
            p = 1
        }
        if (i < f) {
            for (var c = i; c <= f; c += p) {
                res.innerHTML += `${c} 👉🏼`
            }
        } else {
            for (let c = i; c >= f; c -= p) {
                res.innerHTML += `${c} 👉🏼`
            }
        }
        res.innerHTML += ` 🍕`
    }
}