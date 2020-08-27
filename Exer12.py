class Classe:
    def menorMaior(self, valor1, valor2):
        if valor1 > valor2:
            print(f"{valor1} > {valor2}")
        elif valor2 > valor1:
            print(f"{valor2} > {valor1}") 
        else:
            print("INVALIDO") 

resposta = Classe();


valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

resposta.menorMaior(valor1, valor2)





