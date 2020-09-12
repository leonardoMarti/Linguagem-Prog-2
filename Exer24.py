class Classe:
    def uniao(self, lista1, lista2):
        print(f"UNIAO = {lista1 + lista2}")
    
    def intercalacao(self, lista1, lista2):
        novaLista = []
        for i in range(len(lista1)): 
            novaLista.append( lista1[i])
            novaLista.append( lista2[i])
        print(f'INTERCALAÇÂO = {novaLista}')
        
    
resposta = Classe();

lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

resposta.uniao(lista1, lista2)
resposta.intercalacao(lista1, lista2)




