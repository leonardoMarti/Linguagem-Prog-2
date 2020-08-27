class Classe:
    def mostraPalavra(self, valor, palavra):
        for index, item in enumerate(range(valor)):
            print(f"{index + 1} - {palavra}")
    
resposta = Classe();

valor = int(input('Digite um valor: '))
palavra = str(input('Digite uma palavra: '))


resposta.mostraPalavra(valor, palavra)





