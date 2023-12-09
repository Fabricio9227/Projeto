//CONDIÇÕES MULTIPLAS

var hoje = new Date()
var diaSem = hoje.getDay() 

   switch(diaSem) {
        case 0:
            console.log('Domingo')
            break
        case 1:
            console.log('Segunda-feira')
            break
        case 2:
            console.log('Terça-feira')
            break
        case 3:
            console.log('Quarta-freira')
            break
        case 4:
            console.log('Quinta-feira')
            break
        case 5:
            console.log('Sexta-feira')
            break
        case 6:
            console.log('Sabado-feira')
            break
        default:
            break
   }
