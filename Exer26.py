class Classe:
    def igualdade(self, lista1, lista2):
        if lista1 == lista2:
            print('TRUE')
        else:
            print('FALSE')

    def ocorrencia(self, lista1, lista2):
        totalOcorrencia = 0
        for  item in lista1:
            if lista1[0] == item:
                totalOcorrencia += 1;
        print(f"OCORRENCIAS lista1 = {totalOcorrencia}") 

        totalOcorrencia2 = 0
        for item in lista2:
            if lista2[0] == item:
                totalOcorrencia2 += 1;
        print(f"OCORRENCIAS lista2 = {totalOcorrencia2}") 
    
resposta = Classe();

lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 4, 6, 8, 2]
resposta.igualdade(lista1, lista2)
resposta.ocorrencia(lista1, lista2)





