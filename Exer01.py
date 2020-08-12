class Idade:
    def maior(self, idade):
        if idade > 18:
            print("MAIOR")
        else:
            print("MENOR")


resposta = Idade();

pergunta = int(input("Digite uma idade: "))
resposta.maior(pergunta)