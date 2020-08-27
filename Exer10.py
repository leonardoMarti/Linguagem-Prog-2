class Classe:
    def notas(self, lista):
        if sum(lista) >= 18:
            print(f"APROVADO = {sum(lista)}") 
        else:
            print(f"REPROVADO = {sum(lista)}") 

resposta = Classe();

lista = [];
for item in range(3):
    valor = int(input('Digite uma nota[1 a 10]: '))
    lista.append(valor);
resposta.notas(lista)





