import random
import string

notas = {'tiririca': 0 , 'cleiton rasta': 0, 'padre quevedo': 0}

for i in notas:
    nota = int(input(f'Digite a nota: '))
    notas[i] = nota

print(notas)

rm = str(input('Digite o nome do aluno para remover a nota: ')).lower()
removido = False
for key, value in notas.items():
    if key == rm:
        notas[key] = None
        removido = True

if removido == True:
    print(f'Nota removida')
else:
    print('Aluno não matriculado')

print(notas)

alunoAt = str(input('Digite o nome do aluno que voce quer atualizar uma nota: ')).lower()
notaAt = int(input('Digite nota: '))
atualizado = False
for key, value in notas.items():
    if key == alunoAt:
        notas[key] = notaAt
        atualizado = True

if atualizado == True:
    print('Nota atualizada')
else:
    print('Aluno não matriculado')

print(notas)

alunoAd = str(input('Digite o nome do aluno que voce quer adicionar uma nota: ')).lower()
notaAd = int(input('Digite nota: '))
adicionado = False
for key, value in notas.items():
    if key == alunoAd:
        notas[key] = notaAd
        adicionado = True

if adicionado == True:
    print('Nota adicionada')
else:
    print('Aluno não matriculado')

for key, value in notas.items():
    print(f'O aluno {key} ficou com nota {value}')


