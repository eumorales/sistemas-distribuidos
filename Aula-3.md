# Aula 3

## Quando usar threads?

- Para executar múltiplas tarefas simultaneamente, aproveitando a concorrência.  
- Ideal quando se deseja realizar atividades ao mesmo tempo para melhorar a eficiência.

## Quando evitar threads?

- Em tarefas muito simples, de baixa complexidade computacional, onde o uso de threads não traz benefícios significativos.  
- Quando o ganho de desempenho é irrelevante ou o custo de gerenciar várias threads supera os benefícios obtidos.  
- Em situações onde o risco de problemas como deadlocks, condições de corrida e bugs relacionados à sincronização é alto, especialmente em aplicações simples ou com pouco compartilhamento de recursos.  
- Quando as tarefas dependem de dados sequenciais, onde o resultado de uma etapa é necessário para a próxima, dificultando a sincronização correta entre threads.

