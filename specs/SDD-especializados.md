# SDD — Testes Especializados (Não-Funcionais + Confiabilidade)

> **Categorias IBM:** Não-Funcionais · Confiabilidade
> **Skills:** Recuperação · Desempenho · Carga · Estresse · Segurança · Usabilidade · Compatibilidade
> **IDs PRD:** RF-19 a RF-25

---

## SPEC-12 — Skill: teste-de-recuperacao

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-19 |
| **Nome** | teste-de-recuperacao |
| **Categoria IBM** | Testes de Confiabilidade |
| **Nível** | Avançado |
| **Skills relacionadas** | teste-de-sistema, teste-de-estresse |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor a validar **como o sistema se comporta e se recupera diante de falhas** — crashes, perda de conectividade, falha de serviço externo, corrupção de dados ou interrupção abrupta. O foco é: o sistema falha graciosamente e se recupera de forma aceitável?

### Gatilhos de Ativação

- "teste de recuperação", "recovery testing", "chaos engineering básico"
- "o que acontece quando o banco cai?", "e se o sistema falhar no meio de uma transação?"
- "resiliência do sistema", "fallback", "circuit breaker"
- "testar tolerância a falhas"
- "o sistema precisa se recuperar de quedas"
- "quero testar o que acontece em caso de falha"

### Fluxo de Execução

```
Passo 1: MAPEAR PONTOS DE FALHA
  → Quais serviços/recursos o sistema depende? (banco, APIs externas, filas, cache)
  → O que acontece se cada um falhar?
  → Quais são os RTO (Recovery Time Objective) e RPO (Recovery Point Objective) definidos?

Passo 2: CATEGORIZAR CENÁRIOS DE FALHA
  → Falha de infraestrutura: servidor cai, rede cai, disco cheio
  → Falha de serviço dependente: banco indisponível, API externa fora do ar
  → Falha de dados: dados corrompidos, transação incompleta
  → Falha de aplicação: exception não tratada, deadlock, memory leak

Passo 3: DESIGN DE CASOS DE RECUPERAÇÃO
  → Para cada cenário: Como forçar a falha? O que o sistema deve fazer? Como verificar a recuperação?
  → Verificar: o sistema exibe mensagem de erro clara? Os dados permanecem íntegros? O sistema volta ao normal quando a falha é resolvida?

Passo 4: EXECUTAR EM AMBIENTE SEGURO
  → NUNCA em produção
  → Usar ambiente isolado com capacidade de restauração rápida
  → Documentar estado antes de injetar falha

Passo 5: VERIFICAR RECUPERAÇÃO
  → Após a falha ser resolvida: o sistema volta automaticamente?
  → Dados perdidos ou corrompidos durante a falha?
  → Tempo de recuperação está dentro do RTO definido?

Passo 6: DOCUMENTAR
  → Cenário → falha injetada → comportamento observado → tempo de recuperação → dados afetados
```

### Critérios de Aceite

- CA-01: A skill pergunta pelos RTO/RPO definidos (se não existirem, sugere definir)
- CA-02: A skill cobre pelo menos 3 categorias de falha diferentes
- CA-03: A skill alerta explicitamente: executar APENAS em ambiente isolado
- CA-04: A skill verifica integridade dos dados pós-recuperação

---

## SPEC-13 — Skill: teste-de-desempenho

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-20 |
| **Nome** | teste-de-desempenho |
| **Categoria IBM** | Testes Não-Funcionais — Desempenho |
| **Nível** | Intermediário / Avançado |
| **Skills relacionadas** | teste-de-carga (volume), teste-de-estresse (limites) |

### Fronteira Semântica (crítica)

| | Desempenho | Carga | Estresse |
|-|-----------|-------|---------|
| **Pergunta** | "Quão rápido?" | "Aguenta quantos?" | "Onde quebra?" |
| **Volume** | Normal (1 usuário ou típico) | Crescente até o limite | Além do limite |
| **Objetivo** | Medir métricas de tempo/throughput | Encontrar degradação de desempenho | Encontrar ponto de colapso |

### Gatilhos de Ativação

- "teste de desempenho", "performance testing", "performance test"
- "quão rápido está a API?", "tempo de resposta"
- "medir throughput", "latência", "TPS (transações por segundo)"
- "baseline de performance", "benchmark"
- "o sistema está lento — quero medir"

### Fluxo de Execução

```
Passo 1: DEFINIR MÉTRICAS ALVO
  → Tempo de resposta: < X ms para 95% das requisições (p95)
  → Throughput: N transações por segundo
  → Taxa de erro: < X% das requisições podem falhar
  → Uso de recursos: CPU < X%, Memória < Y MB

Passo 2: DEFINIR PERFIL DE CARGA (baseline)
  → Quantos usuários simultâneos é "normal"?
  → Qual é o padrão de uso típico? (tempo de think entre ações)

Passo 3: CRIAR SCRIPT DE TESTE
  → Definir os cenários a medir (quais endpoints/fluxos)
  → Definir a sequência de ações de um "usuário virtual"
  → Ferramenta: agnóstica — pode ser k6, JMeter, Locust, Gatling, ou chamadas manuais

Passo 4: EXECUTAR BASELINE
  → Rodar com número normal de usuários
  → Coletar: p50, p95, p99 de tempo de resposta, throughput, taxa de erro

Passo 5: ANALISAR E DOCUMENTAR
  → As métricas atendem os targets definidos?
  → Onde estão os gargalos? (banco? Rede? CPU? Código?)
  → Comparar com baseline anterior (se existir)
```

### Critérios de Aceite

- CA-01: A skill define métricas alvo ANTES de executar testes
- CA-02: A skill menciona percentis (p50, p95, p99) — não apenas média
- CA-03: A skill diferencia-se de teste de carga e estresse
- CA-04: A skill menciona a necessidade de ambiente representativo

---

## SPEC-14 — Skill: teste-de-carga

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-21 |
| **Nome** | teste-de-carga |
| **Categoria IBM** | Testes Não-Funcionais — Carga |
| **Nível** | Avançado |
| **Skills relacionadas** | teste-de-desempenho (baseline), teste-de-estresse (além do limite) |

### Gatilhos de Ativação

- "teste de carga", "load testing", "carga de usuários"
- "o sistema aguenta N usuários simultâneos?"
- "quero testar com X requisições por segundo"
- "antes do lançamento, testar com a carga esperada"
- "quero saber quando o sistema começa a degradar"
- "escalar usuários gradualmente e ver o comportamento"

### Fluxo de Execução

```
Passo 1: DEFINIR PERFIS DE CARGA
  → Carga normal: N usuários (baseline do dia-a-dia)
  → Carga de pico: M usuários (maior carga esperada — ex: Black Friday)
  → Carga de crescimento: estratégia de ramp-up (quantos usuários adicionar por quanto tempo)

Passo 2: DEFINIR CRITÉRIOS DE ACEITAÇÃO SOB CARGA
  → Tempo de resposta aceitável com N usuários: < X ms
  → Taxa de erro aceitável: < Y%
  → Recursos aceitáveis: CPU < Z%, Memória < W MB

Passo 3: EXECUTAR EM FASES
  → Fase 1 (Warm-up): 10-20% da carga esperada
  → Fase 2 (Ramp-up): aumentar gradualmente até 100% da carga esperada
  → Fase 3 (Sustentação): manter carga máxima por 15-30 minutos
  → Fase 4 (Cool-down): reduzir carga gradualmente

Passo 4: MONITORAR DURANTE EXECUÇÃO
  → Tempo de resposta por percentil (p50, p95, p99)
  → Taxa de erro (requisições com falha)
  → CPU, memória, I/O do servidor
  → Conexões ativas do banco de dados

Passo 5: ANALISAR RESULTADOS
  → O sistema degradou com o aumento de carga? (quando?)
  → O sistema se recuperou na fase de cool-down?
  → Onde está o gargalo? (identificar o bottleneck)

Passo 6: RELATÓRIO
  → Gráfico de tempo de resposta ao longo do tempo
  → Ponto de degradação identificado
  → Recomendações de capacidade
```

### Critérios de Aceite

- CA-01: A skill define perfis de carga (normal, pico) antes de executar
- CA-02: A skill usa estratégia de ramp-up (não começa com carga total imediatamente)
- CA-03: A skill inclui fase de sustentação (não apenas subida de carga)
- CA-04: A skill menciona monitoramento de recursos do servidor (não apenas tempo de resposta)

---

## SPEC-15 — Skill: teste-de-estresse

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-22 |
| **Nome** | teste-de-estresse |
| **Categoria IBM** | Testes Não-Funcionais — Estresse |
| **Nível** | Avançado |
| **Skills relacionadas** | teste-de-carga (dentro dos limites), teste-de-recuperacao (após colapso) |

### Gatilhos de Ativação

- "teste de estresse", "stress testing", "stress test"
- "quero saber o limite do sistema", "ponto de ruptura"
- "o que acontece quando o sistema colapsa?"
- "testar além da capacidade"
- "soak testing", "durabilidade do sistema"

### Quando NÃO usar

- Para medir desempenho normal → usar `teste-de-desempenho`
- Para validar capacidade planejada → usar `teste-de-carga`

### Fluxo de Execução

```
Passo 1: ESTABELECER BASELINE
  → Primeiro rodar teste de carga normal (ou usar resultados existentes)
  → Saber: onde o sistema funciona bem, onde começa a degradar

Passo 2: EMPURRAR ALÉM DOS LIMITES
  → Aumentar carga gradualmente até o sistema falhar
  → Manter pressão por tempo estendido (soak test: horas ou dias em carga alta)
  → Reduzir recursos do servidor (simular degradação de infraestrutura)

Passo 3: OBSERVAR O COLAPSO
  → Como o sistema falha? (timeout? Crash? Corrupção de dados? Travamento?)
  → A falha é graceful (mensagem de erro clara) ou abrupta (crash sem aviso)?
  → Quais recursos se esgotam primeiro? (memória? Conexões? CPU? Disco?)

Passo 4: TESTAR RECUPERAÇÃO PÓS-ESTRESSE
  → Após reduzir a carga: o sistema se recupera automaticamente?
  → Os dados permanecem íntegros após o colapso?
  → Quanto tempo leva para recuperar (RTO)?

Passo 5: DOCUMENTAR O PONTO DE RUPTURA
  → N usuários / M RPS onde o sistema começa a falhar
  → Tipo de falha observado
  → Comportamento de recuperação
```

### Critérios de Aceite

- CA-01: A skill parte de baseline (não começa com estresse extremo direto)
- CA-02: A skill inclui análise do tipo de falha (graceful vs. abrupta)
- CA-03: A skill testa recuperação após o estresse
- CA-04: A skill documenta o ponto de ruptura (limite identificado)

---

## SPEC-16 — Skill: teste-de-seguranca

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-23 |
| **Nome** | teste-de-seguranca |
| **Categoria IBM** | Testes Não-Funcionais — Segurança |
| **Nível** | Intermediário / Avançado |
| **Skills relacionadas** | teste-de-API (contratos), teste-de-sistema (escopo completo) |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor a identificar e testar vulnerabilidades de segurança no sistema — com foco em práticas acessíveis e baseadas nas categorias OWASP Top 10, sem requerer que o usuário seja um especialista em segurança ofensiva.

### Gatilhos de Ativação

- "teste de segurança", "security testing", "pentest básico"
- "vulnerabilidades", "OWASP", "SQL injection", "XSS"
- "testar autenticação e autorização"
- "quero saber se minha API está segura"
- "auditoria de segurança básica"
- "dados dos usuários estão protegidos?"

### Fluxo de Execução

```
Passo 1: ESCOPO DE SEGURANÇA
  → Quais partes do sistema serão avaliadas? (API, frontend, banco, autenticação)
  → Qual nível de profundidade? (básico/OWASP Top 10 vs. pentest completo)
  → Nota: este guia cobre o nível básico — pentest profundo requer especialista

Passo 2: AUTENTICAÇÃO E AUTORIZAÇÃO
  → Acesso sem credenciais → deve ser bloqueado
  → Credenciais inválidas → deve ser bloqueado (sem mensagem que revele se usuário existe)
  → Acesso a recursos de outro usuário → deve ser bloqueado (IDOR)
  → Escalação de privilégio: usuário comum acessando área de admin → deve ser bloqueado

Passo 3: VALIDAÇÃO DE INPUT (INJEÇÃO)
  → SQL Injection: tentar inserir SQL em campos de texto
  → XSS: tentar inserir scripts em campos que renderizam HTML
  → Command Injection: tentar inserir comandos do SO em inputs processados pelo servidor
  → Regra geral: NUNCA confiar em input do cliente — sempre validar no servidor

Passo 4: PROTEÇÃO DE DADOS
  → Dados sensíveis são criptografados em trânsito (HTTPS)?
  → Dados sensíveis são criptografados em repouso?
  → Senhas são armazenadas com hash (nunca em texto plano)?
  → Tokens e API keys estão expostos em logs ou respostas?

Passo 5: HEADERS E CONFIGURAÇÕES
  → Headers de segurança presentes? (CSP, X-Frame-Options, etc.)
  → Informações de versão de servidor expostas?
  → CORS configurado corretamente?

Passo 6: DOCUMENTAR VULNERABILIDADES
  → Para cada vulnerabilidade encontrada: tipo | severidade | como reproduzir | impacto | sugestão de correção
  → Classificar por severidade: Crítica / Alta / Média / Baixa
```

### Critérios de Aceite

- CA-01: A skill menciona as categorias OWASP como referência
- CA-02: A skill cobre autenticação, autorização E validação de input
- CA-03: A skill menciona que pentest profundo requer especialista (escopo honesto)
- CA-04: A skill classifica vulnerabilidades por severidade

---

## SPEC-17 — Skill: teste-de-usabilidade

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-24 |
| **Nome** | teste-de-usabilidade |
| **Categoria IBM** | Testes Não-Funcionais — Usabilidade |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-de-aceitacao-do-usuario (validação de negócio), teste-de-compatibilidade |

### Gatilhos de Ativação

- "teste de usabilidade", "usability testing", "UX testing"
- "o usuário consegue usar o sistema?", "teste com usuário real"
- "heurísticas de Nielsen", "avaliação heurística"
- "minha interface é intuitiva?"
- "quero testar a experiência do usuário"
- "facilidade de uso"

### Fluxo de Execução

```
Passo 1: DEFINIR OBJETIVOS DE USABILIDADE
  → O que o usuário deve conseguir fazer? (tarefas a testar)
  → Qual o perfil do usuário testador? (iniciante, experiente, com deficiência?)
  → Critérios: eficácia (consegue fazer?), eficiência (quanto tempo?) satisfação (ficou feliz?)

Passo 2: ESCOLHER ABORDAGEM
  → Avaliação Heurística: especialistas avaliam contra as 10 heurísticas de Nielsen (sem usuário)
  → Teste com Usuário: usuário real executa tarefas enquanto é observado
  → Teste de Primeiro Clique: onde o usuário clicaria para realizar uma tarefa?

Passo 3: PREPARAR TAREFAS
  → Escrever 5-8 tarefas realistas para o usuário executar
  → Formato: "Você quer [objetivo]. Como faria isso no sistema?"
  → Tarefas devem refletir uso real — não tours guiados

Passo 4: EXECUTAR SESSÃO (para teste com usuário)
  → Pedir ao usuário para "pensar em voz alta" enquanto navega
  → Observar (sem ajudar): onde trava? Onde clica errado? O que confunde?
  → Registrar: tempo por tarefa, erros, comentários verbais

Passo 5: ANALISAR E REPORTAR
  → Taxa de sucesso por tarefa (% de usuários que completaram)
  → Problemas de usabilidade encontrados com severidade
  → Sugestões de melhoria priorizadas
```

### Critérios de Aceite

- CA-01: A skill diferencia avaliação heurística de teste com usuário
- CA-02: A skill menciona as 10 heurísticas de Nielsen como referência
- CA-03: A skill foca na experiência do usuário (não no funcionamento técnico)
- CA-04: A skill produz problemas de usabilidade com severidade

---

## SPEC-18 — Skill: teste-de-compatibilidade

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-25 |
| **Nome** | teste-de-compatibilidade |
| **Categoria IBM** | Testes Não-Funcionais — Compatibilidade |
| **Nível** | Intermediário |
| **Skills relacionadas** | teste-de-sistema, teste-de-usabilidade |

### Gatilhos de Ativação

- "teste de compatibilidade", "compatibility testing", "cross-browser"
- "testar em diferentes browsers", "testar em diferentes sistemas operacionais"
- "funciona no Safari? No Firefox? No IE?"
- "compatível com mobile?", "responsivo?"
- "testar em diferentes versões da dependência"
- "backward compatibility"

### Fluxo de Execução

```
Passo 1: DEFINIR MATRIZ DE COMPATIBILIDADE
  → Browsers: Chrome, Firefox, Safari, Edge (versões mínimas suportadas)
  → Sistemas Operacionais: Windows, macOS, Linux, Android, iOS
  → Dispositivos: Desktop, Tablet, Mobile (resolução/tamanho de tela)
  → Versões de dependências: versões mínimas e máximas suportadas

Passo 2: PRIORIZAR COMBINAÇÕES
  → Identificar quais combinações são mais usadas pelo público-alvo
  → Focar em: combinações de alto uso + combinações com histórico de problemas

Passo 3: CRIAR CASOS DE COMPATIBILIDADE
  → Para cada combinação prioritária: testar os fluxos críticos
  → Verificar: renderização, funcionalidade, performance, responsividade

Passo 4: EXECUTAR E REGISTRAR
  → Screenshot de cada combinação onde encontrou problema
  → Registrar: combinação | componente | comportamento esperado | comportamento real

Passo 5: CLASSIFICAR E PRIORIZAR
  → Problemas em combinações de alto uso → alta prioridade
  → Problemas em combinações raras → baixa prioridade
  → Definir matrix de suporte oficial (o que é garantido vs. "best effort")
```

### Critérios de Aceite

- CA-01: A skill solicita definição da matriz de compatibilidade antes de testar
- CA-02: A skill prioriza por frequência de uso (não testa tudo com igual peso)
- CA-03: A skill inclui dispositivos móveis além de desktop
- CA-04: A skill menciona a importância de definir uma "matriz de suporte oficial"

---

## Score deste SDD

| Dimensão | Score | Status |
|----------|-------|--------|
| Completude | 29/30 | Todas as 7 skills com fluxos completos |
| Testabilidade | 24/25 | Todos CAs verificáveis |
| Clareza | 20/20 | Fronteira Desempenho/Carga/Estresse bem definida |
| Escopo | 15/15 | Non-goals explícitos |
| Edge Cases | 9/10 | Cobertos nas principais |
| **TOTAL** | **97/100** | ✅ PRONTO PARA IMPLEMENTAÇÃO |
