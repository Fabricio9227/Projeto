let valores = [8, 1, 7, 4, 2, 9]

valores.push('qualquer numero aqui')//irá acrescentar um valor depois da ultima posição da array
valores.length//irá contar o cumprimento da array
valores.sort()//irá ordenar em crescente

console.log(valores)



for(let pos=0; pos < valores.length; pos++) {
    console.log(`A posição ${pos} recebe o valor ${valores[pos]}`)
}


for(let pos in valores) {
    console.log(num[pos])
}

valores.indexOf(7)//busca valores dentro da array
valores.splice('n° posição, 0, novo_elemento')//posição é o onde o novo elemento vai ser incluído. 0 significa que nenhum elemento vai ser deletado. novo_elemento vai ser o elemento a ser add na array
valores.shift()//remove um elemento do inicio da array
valores.pop()//remove um elemento do final da array, atualizando o tamanho

