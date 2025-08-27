# Diferença entre Processo e Thread — Resumo

## Processo vs Thread — Resumo

- **Processo:**  
  É um programa em execução com **espaço de memória próprio** e recursos independentes. Comunicação entre processos é complexa e custosa. Se um processo falha, não afeta os outros.

- **Thread:**  
  É uma unidade de execução dentro de um processo, que **compartilha o mesmo espaço de memória** com outras threads. Comunicação entre threads é rápida, mas uma falha pode comprometer o processo todo.

## Comparação rápida:

| Característica | Processo             | Thread              |
|----------------|---------------------|---------------------|
| Memória        | Espaço próprio      | Compartilhada       |
| Comunicação    | Complexa (IPC)      | Simples             |
| Criação        | Mais custosa         | Mais barata         |
| Robustez       | Mais isolado        | Pode comprometer o processo |

## Em sistemas distribuídos:

- Processos rodam em máquinas diferentes (ex.: microserviços).  
- Threads paralelizam tarefas dentro do mesmo processo.
