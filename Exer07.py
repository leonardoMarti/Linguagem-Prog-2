class Classe:
    def maiorMenor(self, lista):
        print(f"MAIOR = {max(lista)}")
        print(f"MENOR = {min(lista)}")

    def soma(self, lista):
        totalSoma = 0
        for item in lista:
            totalSoma += item;
        print(f"TOTAL = {totalSoma}")
    
    def media(self, lista):
        total = 0
        for item in lista:
            total += item;
        media = total / len(lista)
        print(f"MEDIA = {media}")
        
    
resposta = Classe();

lista = []
for item in range(10):
    valor = int(input("Digite um numero: "))
    lista.append(valor)

resposta.maiorMenor(lista)
resposta.soma(lista)
resposta.media(lista)


