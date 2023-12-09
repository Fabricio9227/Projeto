let sliderElement = document.querySelector('#slider');
let buttonElement = document.querySelector('#button');

let sizePassword = document.querySelector('#valor');
let password = document.querySelector('#password');

let containerPassword = document.querySelector('#container-password');

let charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'; //Aqui, criamos um "dicionario" de letras que serão nossos charsets, eles irão fazer parte da senha gerada
let novaSenha = ""; //Novasenha recebe um valor vazio

sizePassword.innerHTML = sliderElement.value;

slider.oninput = function(){
    sizePassword.innerHTML = this.value;
}

function generatePassword(){
    
    let pass = "" //Definimos a variável pass como um valor vazio

    for(let i = 0, n = charset.length; i < sliderElement.value; ++i){ //"i" começa recebendo zero, "n" recebe a quantitude de caracteres em charset. Enquanto "i" for menor que o valor de sliderElement "i" continua recebendo valores
        pass += charset.charAt(Math.floor(Math.random() * n)); //cada vez que o "for" é executado, "pass" recebe mais um valor de charset. No charAt, usando o metodo math e random, ele gera um caractere qualquer da string "Charset".
    }

    containerPassword.classList.remove("hide"); //remove a classe hide do containerPassword
    password.innerHTML = pass; //password recebe o valor de "pass"

}

function copyPassword(){ //Função que irá copiar a senha
    alert('Senha copiada com sucesso!')
    navigator.clipboard.writeText(novaSenha); //Copia a nova senha após clicar na caixa indicativa
}