# Aula 5

## Relógios Físicos  
- Baseados no tempo real (UTC).  
- Podem estar fora de sincronização entre si.  
- Sincronização é necessária para coordenar eventos com base no horário.  
- Exemplo: decidir quem chegou primeiro ao banheiro pelo horário dos relógios.

## Relógios Lógicos  
- Não medem tempo real, apenas ordenam eventos de forma causal.  
- Garantem que a ordem dos eventos faça sentido entre processos.  
- Exemplo: mesmo sem relógios, sabemos quem entrou primeiro na fila do banheiro.

## Exclusão Mútua  
- Garante que apenas um processo (pessoa) use o recurso (banheiro) por vez.  
- Três regras importantes:  
  - Mutual Exclusion: um por vez.  
  - Progress: se o recurso está livre, alguém da fila deve entrar.  
  - Bounded Waiting: ninguém espera para sempre.  
- Implementações podem ser centralizadas (um coordenador) ou distribuídas (regras combinadas).  
- Exemplo: evitar que duas pessoas entrem no banheiro ao mesmo tempo.

## Algoritmos de Eleição  
- Escolhem um coordenador para organizar o acesso ao recurso.  
- Exemplos: Bully (quem tem maior autoridade decide) e Ring (decisão circula até consenso).  
- Exemplo: moradores decidem entre si quem será responsável pela fila.

## Sincronismo e Acesso à Seção Crítica  
- Organiza o acesso ao recurso para evitar conflitos.  
- Utiliza mecanismos como `synchronized` (Java) ou `lock` (C#/Python).  
- Relaciona relógios (ordem), exclusão mútua (uso exclusivo) e eleição (coordenação).  
- Exemplo: fila na porta garante que só uma pessoa use o banheiro por vez, respeitando a ordem.
