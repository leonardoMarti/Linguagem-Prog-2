import math

class Classe:
    def media(self, lista):
        total = 0
        for item in lista:
            total += item;
        media = total / len(lista)

        print('media',media)
        for item in lista:
            if math.isclose(item, media, abs_tol = 0.50):
                print(f'Valor mais proximo da media({media}) = {item}')

    
resposta = Classe();

lista = [1.5, 5.5, 3.4, 7.9, 10]
resposta.media(lista)


