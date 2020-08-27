class Classe:
    def maior(self, lista):
        print(f"MAIOR = {max(lista)}")

resposta = Classe();

lista = [];
for item in range(10):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

resposta.maior(lista)





