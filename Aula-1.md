# Plano de Ensino 📚

### Unidade 1: Fundamentos 🧱
- Comunicação
- Processos e threads
- Sincronização

### Unidade 2: Comunicação 📡
- Fundamentos
- Comunicação por troca de mensagens
- Sistemas distribuídos baseados em objetos

### Unidade 3: Comunicação em Grupo 👥
- Fundamentos
- Multicast
- Comunicação confiável em grupo

### Unidade 4: Sistemas de Arquivos Distribuídos e Memória Compartilhada Distribuída 💾
- Fundamentos
- Modelo de consistência
- Estudo de casos

---

## Aula 1: Fundamentos e Processos 🌟

### Sistemas Distribuídos
- **Características**: Sistemas fracamente acoplados (ex.: Grid computacional)
  - Geograficamente distribuídos
  - Hardware e sistemas operacionais diferentes
  - Comunicação via modelo TCP/IP
- **Programação**: Programação distribuída
- **Arquitetura**:
  - Cliente-servidor
  - Ponto-a-ponto
- **Comunicação**:
  - Troca de mensagens: String → mensagem
  - Objetos: Serialização
- **Sincronismo**:
  - Relógio
  - Monitor ou Semáforo
- **Tolerância a falhas**

### Sistemas Paralelos
- **Características**: Sistemas fortemente acoplados (ex.: Cluster computacional)
  - Mesma localização geográfica
  - Hardware idêntico em todas as máquinas
  - Comunicação via fibra óptica
  - Sistema de nobreak robusto
  - Sistema de backup
- **Programação**: Programação paralela

### Processos
- **Definição**: Demanda recursos de hardware
  - Processador
  - Barramento
  - RAM + Cache
  - Periféricos

### Threads
- **Definição**: Mini processo
- **Gestão**:
  - Status: Stop, Sleep, Ready, Pause, Resume, **Sincronizar**
  - Atributos: Nome, ID, Prioridade
- **Tipos**:
  - Simples: Sem dependência de dados
  - Memória compartilhada: Dependência de um ou mais processos
