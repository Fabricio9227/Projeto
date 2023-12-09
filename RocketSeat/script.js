function toggleMode() {
    const html = document.documentElement
    html.classList.toggle('light')

    //Pega a tag IMG
    const img = document.querySelector("#profile img")

    //substituir a imagem
    if (html.classList.contains("light")) {
        //se tiver light mode, add a img light
        img.setAttribute('src', './assets/assets/image.png')
    }
    else {
        img.setAttribute('src', './assets/assets/foto-dark.jpg')
    }
}