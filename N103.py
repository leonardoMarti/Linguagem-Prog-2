valor = int(input('Digite uma nota entre 0-10: '))
while valor > 10 or valor < 0:
    print('Ops, acho que você se perdeu na leitura. Tente novamente!')
    valor = int(input('Digite uma nota entre 0-10: '))
