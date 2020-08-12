class Troco:
    def resultado(self, valor, valor2):
        total = valor - valor2
        print(f"Troco =  ${total}")
    
resposta = Troco();

valor = int(input("Digite o valor a ser pago: "))
valor2 = int(input("Digite o preço do produto: "))
resposta.resultado(valor, valor2)
