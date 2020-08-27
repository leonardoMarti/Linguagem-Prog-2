class Classe:
    def idades(self, h1, h2, m1, m2):
        if h1 > h2 and m1 > m2:
            print(f"SOMA = {h1 + m2}")
            print(f"PRODUTO = {h2 * m1}")

        else:
            print(f"SOMA = {h2 + m1}")
            print(f"PRODUTO = {h1 + m2}")

resposta = Classe();


h1 = int(input('Digite a idade do primeiro homem: '))
h2 = int(input('Digite a idade do segundo homem: '))
m1 = int(input('Digite a idade da primeira mulher: '))
m2 = int(input('Digite a idade da segunda mulher: '))


resposta.idades(h1, h2, m1, m2)





