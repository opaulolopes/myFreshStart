function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas`
    if (hora < 12) {
        img.src = 'imagens/morning.jpg'
        document.body.style.background = '#FFE56E'
    } else if (hora < 18) {
        img.src = 'imagens/afternoon.jpg'
        document.body.style.background = '#FB8D46'
    } else {
        img.src = 'imagens/evening.jpg'
        document.body.style.background = '#7C6093'
    }
}