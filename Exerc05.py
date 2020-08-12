class Confere:
    def resultado(self, valor):
        if valor < 0:
            print(f"{valor} é negativo")
        else:
            print(f'{valor} é positivo')
    
resposta = Confere();

valor = int(input("Digite um numero: "))
resposta.resultado(valor)