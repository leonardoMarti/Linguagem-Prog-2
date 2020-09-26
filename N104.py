import time
import random

def f1(func):
    def wrapper():
        before = time.time()
        func()
        print(f'Finalizou em {time.time() - before} segundos')
    
    return wrapper

@f1 
def f():
    soma = 0
    for i in range(4):
        soma += random.randint(0, 100)
    print(f'TOTAL = {soma}')
f()