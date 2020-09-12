class Classe:
    def maior(self, lista):
        print(f"MAIOR = {max(lista)}")

    def soma(self, lista):
        totalSoma = 0
        for item in lista:
            totalSoma += item;
        print(f"TOTAL = {totalSoma}")
    
    def ocorrencia(self, lista):
        totalOcorrencia = 0
        for  item in lista:
            if lista[0] == item:
                totalOcorrencia += 1;
        print(f"OCORRENCIAS = {totalOcorrencia}")
    
    def media(self, lista):
        total = 0
        for item in lista:
            total += item;
        media = total / len(lista)
        print(f"MEDIA = {media}")
        
    
resposta = Classe();

lista = [1, 4, 1, 5, 6, 8, 4, 9, 22, 77, 88, 1]
print(f'LISTA = {lista}')
resposta.maior(lista)
resposta.soma(lista)
resposta.ocorrencia(lista)
resposta.media(lista)


