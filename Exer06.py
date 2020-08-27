class Classe:
    def sinal(self, valor):
        if valor < 0:
            print(f"{valor} é negativo")
        else:
            print(f'{valor} é positivo')

    def numero(self, valor):
        if valor % 2 == 0:
            print(f"{valor} é PAR")
        else:
            print(f'{valor} é IMPAR')
    
resposta = Classe();

valor = int(input("Digite um numero: "))
resposta.sinal(valor)
resposta.numero(valor)
