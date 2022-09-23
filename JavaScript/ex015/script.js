function verificar() {
    var data = new Date()
    var ano_atual = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano_atual) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano_atual - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'imagens/foto-bebe-m.jpg')
            } else if (idade < 21) {
                img.setAttribute('src', 'imagens/foto-jovem-m.jpg')
            } else if (idade < 50) {
                img.setAttribute('src', 'imagens/foto-adulto-m.jpg')
            } else {
                img.setAttribute('src', 'imagens/foto-idoso-m.jpg')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src', 'imagens/foto-bebe-f.jpg')
            } else if (idade < 21) {
                img.setAttribute('src', 'imagens/foto-jovem-f.jpg')
            } else if (idade < 50) {
                img.setAttribute('src', 'imagens/foto-adulto-f.jpg')
            } else {
                img.setAttribute('src', 'imagens/foto-idoso-f.jpg')
            }
        }
        res.innerHTML = `Detectamos ${genero} com ${idade} anos<br>`
        res.appendChild(img)
    }
}