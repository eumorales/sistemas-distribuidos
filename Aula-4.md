
# Threads com e sem Memória Compartilhada em Java

## Com Memória Compartilhada

- Quando várias threads manipulam **o mesmo recurso** (como uma lista ou objeto).  
- É preciso utilizar `synchronized` para evitar problemas.  
- Pode oferecer **maior desempenho em certas situações**, mas traz riscos como deadlocks e race condition.

### Exemplo de código:

```java
class ListaCompartilhada {
    private final List<Integer> numeros = new ArrayList<>();

    public synchronized void adicionarNumero(int umNumero) {
        numeros.add(umNumero);
        System.out.println(Thread.currentThread().getName() + " adicionou: " + umNumero);
    }
}
```

Uso no `main`:

```java
ListaCompartilhada listaCompartilhada = new ListaCompartilhada();
Thread t1 = new ThreadDeTrabalho(listaCompartilhada, 5);
Thread t2 = new ThreadDeTrabalho(listaCompartilhada, 5);

t1.start();
t2.start();
```

---

## Sem Memória Compartilhada

- Cada thread trabalha com **seus próprios dados e variáveis**.  
- Não existe acesso conjunto entre elas.  
- O desenvolvimento é **mais simples**, dispensando mecanismos de sincronização.  
- Esse modelo reduz a chance de **erros de concorrência**.  

### Exemplo do código:

```java
class PopulaLista extends Thread {
    private List<Integer> lista;
    Integer tamanho;

    public PopulaLista(List<Integer> lista, Integer tamanho) {
        this.lista = lista;
        this.tamanho = tamanho;
    }

    @Override
    public void run() {
        Random random = new Random();
        for (int i = 0; i < tamanho; i++) {
            lista.add(random.nextInt(tamanho));
        }
    }
}
```

Uso na `main`:

```java
List<Integer> lista1 = new ArrayList<>();
List<Integer> lista2 = new ArrayList<>();

PopulaLista threadPopula1 = new PopulaLista(lista1, 10000);
PopulaLista threadPopula2 = new PopulaLista(lista2, 1000);

threadPopula1.start();
threadPopula2.start();
```

---

