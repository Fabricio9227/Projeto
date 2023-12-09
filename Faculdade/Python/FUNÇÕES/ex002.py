lista = [1, 2, 3, 4]
soma = somar_par(lista)
print(f"Os valores pares da lista são: [{soma}]")

def e_par(n):
    r = (n%2==0)
    return r

def somar_par(lista):
    soma = 0
    for num in lista:
        if(e_par(num)):
            soma = soma + num
        return soma
    
