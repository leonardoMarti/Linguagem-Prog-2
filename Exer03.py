class Calculadora:
    def soma(self, valor, valor2):
        total = valor + valor2
        print("Resultado soma = ", total)
    
    def subtracao(self, valor, valor2):
        total = valor - valor2
        print("Resultado subtracao= ", total)

    def multiplicacao(self, valor, valor2):
        total = valor * valor2
        print("Resultado multiplicacao= ", total)

    def divisao(self, valor, valor2):
        total = valor / valor2
        print("Resultado divisao= ", total)


resposta = Calculadora();

valor = int(input("Digite um valor: "))
valor2 = int(input("Digite mais um valor: "))
resposta.soma(valor, valor2)
resposta.subtracao(valor, valor2)
resposta.multiplicacao(valor, valor2)
resposta.divisao(valor, valor2)
