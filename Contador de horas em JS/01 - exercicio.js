function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minutos = data.getMinutes()
    msg.innerHTML = `<strong>Agora são ${hora} horas e ${minutos} minutos</strong>`
    if (hora >= 0 && hora < 12) {
        img.scr = 'manha.jpg'
        document.body.style.background = '#332c22'

    } else if (hora >= 12 && hora < 18) {
        console.log('Boa tarde!')
        img.src = 'tarde.jpg'
        document.body.style.background = '#c4714b'
    } else {
        console.log('Boa noite!')
        img.src = 'noite.jpg'
        document.body.style.background = '#151c26'
    }
} 

