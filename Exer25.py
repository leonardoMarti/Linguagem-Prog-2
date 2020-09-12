class Classe:
    def printMetade(self, lista):

        print(f"RESULTADO = {lista[5:] + lista[:5]}")

        
    
resposta = Classe();

lista = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

resposta.printMetade(lista)




