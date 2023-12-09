#_INIT_ E SELF"

class ControleRemoto: #Cria uma classe/objeto chamada controle remoto
    def _init_(self, cor, altura, profundidade, largura):
        
        #"def" cria uma função. 
        # "_init_" se refere a inicialização de uma classe, ele inicializa as caracteristicas do meu objeto, que no caso é ControleRemoto.
        #"self" se refere a uma instancia (uma variavel criada FORA da classe) de uma classe criada ou de uma CARACTERISTICA da classe. Pode ser lida como "próprio" ou "eu mesmo", precisamos dela para fazer referencia a nossa função quando estivermos fora da classe e quisermos exibir uma CARACTERISTICA da função, por exemplo.
        #Precisamos também colocar as CARACTERISTICAS que existirão dentro daquela função, como cor, altura, largura, etc.

        self.cor = cor 
        #"Self.cor" diz que "cor" é uma caracteristica do ControleRemoto, sem o self o Python não reconhece que cor é uma caracteristica, ele irá ler que ControleRemoto não tem a CARATERISTICA "cor"
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura 

controle_remoto = ControleRemoto("azul", "10cm", "2cm", "4cm")#Criamos uma variável que recebe a classe pronta e criada de ControleRemoto. Com seus atributos proprios, denifidos nesta própria variável (ex:azul, 10cm, etc)

controle_remoto2 = ControleRemoto("verde", "20cm", "4cm", "12cm")#Criamos uma segunda variável que recebe novamente a classe pré pronta ControleRemoto. Com seus atributos definidos.

print(controle_remoto.cor)#Vou pedir pro Python me mostrar a cor do primeiro controle remoto