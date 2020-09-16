import math

class Classe:
    def remove(self, dict):
       del dict['clodoaldo']
       print(f'RESULTADO = {dict}')

    
resposta = Classe();

dict = {'joao': 'pedreiro', 'maria': 'advogada', 'jose': 'telefonista', 'bianca': 'gerente', 'clodoaldo': 'piloto'}
resposta.remove(dict)


