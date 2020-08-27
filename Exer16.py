class Classe:
    def volume(self, comp, alt, larg):
        print(f"VOLUME = {comp * alt * larg}")

resposta = Classe();

comp = int(input('Digite o comprimento: '))
alt = int(input('Digite a altura: '))
larg = int(input('Digite a largura: '))

resposta.volume(comp, alt, larg)





