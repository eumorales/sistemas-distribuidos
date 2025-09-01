import threading
import random

# Variáveis              
total_numeros = 100000   # quantidade total de números
num_listas = 10           # quantidade de listas
valor_min = 1000         # valor mínimo dos números gerados
valor_max = 100000       # valor máximo dos números gerados

numeros_por_lista = total_numeros // num_listas
listas = [[] for _ in range(num_listas)]

# Popular listas
def popula_lista(lista, quantidade):
    for _ in range(quantidade):
        lista.append(random.randint(valor_min, valor_max))
      
# Threads
threads = []

for i in range(num_listas):
    thread = threading.Thread(target=popula_lista, args=(listas[i], numeros_por_lista))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

# Cálculo da média geral
todos_numeros = [num for lista in listas for num in lista]
media = sum(todos_numeros) / len(todos_numeros)

# Saída
print(f"Total de listas criadas: {num_listas}")
print(f"Tamanho de cada lista: {numeros_por_lista}")
print(f"Quantidade total de números: {len(todos_numeros)}")
print(f"Média geral: {media:.2f}")
