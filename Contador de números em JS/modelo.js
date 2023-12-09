function contar() { 
    let i = document.getElementById('inicio')
    let f = document.getElementById('fim')
    let p = document.getElementById('passo')
    let res = document.getElementById('res') 

    if (i.value.length == 0 || f.value.length == 0 || p.value.length == 0) {
        window.alert('[ERRO] Insira os dados.')
    } else {
        res.innerHTML = 'Contando: '
        let n1 = Number(i.value)
        let n2 = Number(f.value)
        let r = Number(p.value)

        for(let c = n1; c <= n2; c += r) {
            res.innerHTML += `${c} \👍 `
        }
    }
}