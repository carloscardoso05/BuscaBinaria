import matplotlib.pyplot as plt
import timeit
import random

def pesquisa_binaria(lista, item):
    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1   
    return -1

def testar_pesquisa_binaria(tamanho_entrada):
    repeticoes = 10
    tempo_total = 0
    for _ in range(repeticoes):
        lista = [random.randint(1, 100) for _ in range(tamanho_entrada)]
        alvo = random.randint(1, 100)
        inicio = timeit.default_timer()
        pesquisa_binaria(lista, alvo)
        fim = timeit.default_timer()
        tempo_total += fim - inicio
    tempo_individual = tempo_total / repeticoes
    return tempo_individual

tempos = []
tamanhos = []
for tamanho in range(1, 10 ** 5, 1000):
    tamanhos.append(tamanho)
    tempos.append(testar_pesquisa_binaria(tamanho))

print(tamanhos)

plt.plot(tamanhos, tempos)

plt.show()
