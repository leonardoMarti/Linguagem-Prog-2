lista = []
maior = menor = 0
for n in range(5):
    lista.append(int(input(f"Digite o numero de presos no {n + 1}º mês: ")))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]

print(f'A maior quantidade de capturados em um mês foi de {maior}')
print(f'A menor quantidade de capturados em um mês foi de {menor}')

total = 0
for item in lista:
    total += item;
media = total / len(lista)
print(f"A media de capturados ficou em {media}")

diffList = []
for n in range(5):
    diffList.append(abs(media - lista[n]))

menorAprox = indexMenor = None
for key, value in enumerate(diffList):
    if key == 0:
        menorAprox = value
    else:
        if value < menorAprox:
            menorAprox = value
            indexMenor = key

print(f'O valor mais próximo da média de capturados foi de {lista[indexMenor]}')

