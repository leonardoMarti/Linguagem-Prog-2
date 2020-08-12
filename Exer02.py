class MostraExtenso:
    def numero(self, valor):
        if valor == 1:
            print('UM')
        elif valor == 2:
            print('DOIS')
        elif valor == 3:
            print('TRES')
        elif valor == 4:
            print('QUATRO')
        elif valor == 5:
            print('CINCO')
        else:
            print('Numero invalido')
        


resposta = MostraExtenso();

pergunta = int(input("Digite um valor de 1 a 5: "))
resposta.numero(pergunta)