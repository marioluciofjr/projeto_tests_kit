# SDD — Testes por Nível (Pirâmide de Testes)

> **Categoria IBM:** Testes por Nível
> **Skills:** Integração · Sistema · Aceitação do Usuário
> **IDs PRD:** RF-16, RF-17, RF-18

---

## SPEC-09 — Skill: teste-de-integracao

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-16 |
| **Nome** | teste-de-integracao |
| **Categoria IBM** | Testes por Nível — Integração |
| **Nível** | Intermediário |
| **Skills relacionadas** | teste-de-API, teste-de-sistema, teste-de-caixa-branca |

### Fronteira Semântica (crítica)

| | Unidade | Integração | Sistema |
|-|---------|-----------|---------|
| **Escopo** | Uma função/classe | 2+ módulos comunicando | Sistema completo |
| **Isolamento** | Total (mocks de tudo externo) | Parcial (integra os módulos testados, mocka externos) | Mínimo |
| **Velocidade** | Muito rápido | Médio | Lento |
| **Foco** | Lógica interna | Contrato entre módulos | Comportamento do usuário final |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor a validar a **comunicação e o contrato entre dois ou mais módulos, serviços ou componentes** que precisam trabalhar juntos. O foco é: "esses módulos conversam corretamente quando integrados?"

### Gatilhos de Ativação

- "teste de integração", "integration testing", "teste de integração entre serviços"
- "testar como dois módulos se comunicam"
- "validar a integração com o banco de dados"
- "testar a camada de serviço com o repositório"
- "meus módulos A e B precisam se comunicar, quero testar isso"
- "testar a integração com uma API externa"
- "verificar se o contrato entre componentes está correto"

### Quando NÃO usar

- Para testar lógica interna de um único módulo → usar agent `agent-testes-de-unidade`
- Para testar o sistema como um todo → usar `teste-de-sistema`
- Para testar apenas o contrato de uma API → usar `teste-de-API`

### Contrato de Entrada

- Descrição dos módulos a integrar e seus contratos (interfaces/APIs internas)
- Tipo de integração: módulo-módulo, serviço-banco, serviço-API externa, camadas arquiteturais
- Dados de teste disponíveis ou estratégia de setup

### Contrato de Saída

- Casos de teste para cada ponto de integração
- Estratégia de setup e teardown (como preparar e limpar o ambiente)
- Casos de erro de integração (o que acontece quando B falha enquanto A depende de B)
- Decisão sobre o que mockar vs. integrar de verdade

### Fluxo de Execução

```
Passo 1: MAPEAR OS PONTOS DE INTEGRAÇÃO
  → Listar quais módulos/serviços serão integrados no teste
  → Identificar: quem chama quem? Qual o contrato (interface/API) entre eles?
  → Definir: o que será testado de verdade vs. o que será simulado (mock/stub)

Passo 2: ESTRATÉGIA DE INTEGRAÇÃO
  → Big Bang: integrar tudo de uma vez (arriscado, difícil de debugar)
  → Incremental Top-Down: integrar de cima para baixo na hierarquia (usa stubs para baixo)
  → Incremental Bottom-Up: integrar de baixo para cima (usa drivers para cima)
  → Recomendação: incremental é mais seguro

Passo 3: SETUP DO AMBIENTE
  → O que é necessário antes de rodar os testes? (banco de dados, serviços externos, dados)
  → Como garantir que o ambiente está limpo antes de cada teste?
  → Como limpar após cada teste? (teardown)

Passo 4: DESIGN DOS CASOS DE TESTE
  → Cenário feliz: os módulos se comunicam corretamente com dados válidos
  → Cenário de falha no módulo dependente: A chama B, B está indisponível — o que acontece?
  → Cenário de dados incorretos: A envia dados mal formados para B — B rejeita corretamente?
  → Cenário de timeout: B demora demais — A trata isso adequadamente?

Passo 5: EXECUÇÃO E ANÁLISE
  → Executar em ambiente isolado (não produção)
  → Verificar logs de ambos os módulos
  → Confirmar que o estado do sistema após o teste é o esperado

Passo 6: DOCUMENTAÇÃO
  → Para cada caso: módulos envolvidos | cenário | input | comportamento esperado | resultado
```

### Critérios de Qualidade

- Cada ponto de integração tem pelo menos 1 caso de caminho feliz
- Cenários de falha do módulo dependente são testados
- Setup e teardown são explícitos — não há estado compartilhado entre testes
- Decisão de mock vs. real está documentada com justificativa
- Testes não acessam banco de produção

### Edge Cases

| Situação | Como tratar |
|---------|------------|
| Serviço externo indisponível em teste | Usar mock/stub do serviço externo; testar o comportamento do sistema quando ele falha |
| Banco de dados compartilhado entre testes | Usar transações que fazem rollback, ou banco em memória para testes |
| Dados dependentes (teste B depende de dados criados em teste A) | Refatorar: cada teste cria seus próprios dados |
| Módulo ainda não implementado | Usar stubs/mocks com contrato definido; testar o contrato quando o módulo ficar pronto |

### Critérios de Aceite

- CA-01: A skill pergunta quais módulos serão integrados antes de criar casos de teste
- CA-02: A skill menciona as estratégias de integração (big bang vs. incremental)
- CA-03: A skill inclui casos de falha do módulo dependente
- CA-04: A skill define setup e teardown
- CA-05: A skill diferencia-se de testes unitários e de sistema

---

## SPEC-10 — Skill: teste-de-sistema

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-17 |
| **Nome** | teste-de-sistema |
| **Categoria IBM** | Testes por Nível — Sistema |
| **Nível** | Intermediário / Avançado |
| **Skills relacionadas** | teste-de-integracao (nível anterior), teste-de-aceitacao-do-usuario (nível seguinte) |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor a validar o **sistema completo como uma unidade**, verificando que todos os componentes integrados se comportam corretamente em conjunto e que os requisitos do sistema são atendidos. É o nível de teste antes do UAT.

### Gatilhos de Ativação

- "teste de sistema", "system testing", "teste end-to-end"
- "testar o sistema completo", "testar de ponta a ponta"
- "verificar se o sistema atende os requisitos"
- "testar o fluxo completo de uma funcionalidade"
- "antes de entregar para o cliente testar, quero testar por completo"
- "validar o sistema em ambiente de staging"

### Quando NÃO usar

- Para testar comunicação entre módulos específicos → usar `teste-de-integracao`
- Para validação com o usuário/negócio → usar `teste-de-aceitacao-do-usuario`
- Para verificar se o build subiu → usar `teste-de-fumaca`

### Fluxo de Execução

```
Passo 1: DEFINIR ESCOPO DO SISTEMA
  → Quais funcionalidades/fluxos serão testados?
  → Em qual ambiente? (staging, pré-produção — NUNCA produção)
  → Quais são os requisitos funcionais e não-funcionais a validar?

Passo 2: IDENTIFICAR FLUXOS CRÍTICOS (User Journeys)
  → Mapear os principais caminhos que um usuário real percorreria
  → Priorizar: fluxos de negócio principais > fluxos secundários > casos de borda
  → Exemplos: "usuário se cadastra → faz login → realiza ação principal → faz logout"

Passo 3: PREPARAR DADOS E AMBIENTE
  → Dados de teste realistas (sem dados de produção)
  → Ambiente de sistema completo (banco, serviços externos, integrações)
  → Condições iniciais do sistema definidas

Passo 4: EXECUTAR CASOS DE SISTEMA
  → Testar cada fluxo crítico do início ao fim
  → Verificar comportamento funcional: o resultado está correto?
  → Verificar comportamento não-funcional: está rápido? Seguro? Compatível?

Passo 5: CENÁRIOS NEGATIVOS
  → O que acontece quando o usuário faz algo errado no meio do fluxo?
  → O que acontece com dados inválidos em qualquer ponto?
  → O sistema se recupera de erros durante o fluxo?

Passo 6: RELATÓRIO
  → Status de cada fluxo: Passou / Falhou / Bloqueado
  → Bugs encontrados com: passo a passo de reprodução, comportamento esperado vs. real
  → Métricas de cobertura dos requisitos: quantos requisitos foram validados?
```

### Critérios de Qualidade

- Cada requisito funcional principal tem pelo menos um caso de teste de sistema
- Fluxos são testados de ponta a ponta (não apenas partes)
- Ambiente de teste é representativo do ambiente de produção
- Testes incluem verificação funcional E não-funcional básica
- Bugs são documentados com steps de reprodução completos

### Edge Cases

| Situação | Como tratar |
|---------|------------|
| Fluxos muito longos | Dividir em fluxos menores com estados intermediários verificáveis |
| Dependência de serviços externos em produção | Usar mocks estáveis ou ambientes de sandbox fornecidos pelo serviço |
| Dados de teste que "sujam" o sistema | Implementar rollback ou usar ambiente descartável |

### Critérios de Aceite

- CA-01: A skill foca em fluxos completos (não módulos isolados)
- CA-02: A skill menciona a necessidade de ambiente representativo
- CA-03: A skill inclui cenários negativos nos fluxos
- CA-04: A skill menciona cobertura de requisitos (não só cobertura de código)

---

## SPEC-11 — Skill: teste-de-aceitacao-do-usuario

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-18 |
| **Nome** | teste-de-aceitacao-do-usuario |
| **Categoria IBM** | Testes por Nível — Aceitação |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-de-sistema (nível anterior), teste-de-usabilidade |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor ou Product Manager a estruturar o **processo de validação com o usuário final ou stakeholder do negócio** — o momento em que o software é avaliado por quem pediu, segundo os critérios de aceitação definidos. O agente deve facilitar o processo de UAT, não apenas criar casos de teste.

### Gatilhos de Ativação

- "UAT", "User Acceptance Testing", "teste de aceitação"
- "o cliente vai testar o sistema", "entregar para homologação"
- "quero preparar o UAT", "critérios de aceitação"
- "o usuário precisa aprovar a entrega"
- "homologação com o cliente"
- "BDD", "Given-When-Then" (no contexto de aceitação)

### Quando NÃO usar

- Para validação técnica sem envolvimento do usuário/negócio → usar `teste-de-sistema`
- Para avaliar experiência e usabilidade → usar `teste-de-usabilidade`

### Fluxo de Execução

```
Passo 1: DEFINIR CRITÉRIOS DE ACEITAÇÃO
  → Quais são os critérios que o usuário/negócio definiu para aceitar a entrega?
  → Se não existem: facilitar a criação usando o formato:
    "Dado [contexto], Quando [ação], Então [resultado esperado]"

Passo 2: PREPARAR O AMBIENTE DE UAT
  → Ambiente estável, com dados representativos (não de produção)
  → Guia de acesso para o usuário testador
  → Template de feedback/bug report simplificado (para não-técnicos)

Passo 3: CRIAR ROTEIRO DE TESTES PARA O USUÁRIO
  → Cenários escritos em linguagem de negócio (sem jargão técnico)
  → Cada cenário: contexto → passos a seguir → o que verificar → resultado esperado
  → Máximo 10-15 cenários por sessão de UAT

Passo 4: CONDUZIR A SESSÃO DE UAT
  → Usuário executa os cenários (com ou sem facilitador presente)
  → Coletar feedback: funciona como esperado? É fácil de usar?
  → Registrar bugs encontrados + sugestões

Passo 5: CLASSIFICAR RESULTADOS
  → Aceite: todos os critérios de aceitação atendidos
  → Aceite condicional: pequenos ajustes necessários antes do aceite final
  → Recusa: critérios críticos não atendidos — nova rodada de desenvolvimento necessária

Passo 6: DOCUMENTAR ACEITE
  → Assinatura formal (ou registro) de aceite da entrega
  → Lista de itens pendentes acordados (se aceite condicional)
```

### Critérios de Qualidade

- Cenários escritos em linguagem de negócio (não técnica)
- Critérios de aceitação são mensuráveis e verificáveis pelo usuário não-técnico
- Há um processo claro de aprovação/rejeição da entrega
- Feedback do usuário é coletado estruturadamente

### Critérios de Aceite

- CA-01: A skill usa linguagem de negócio nos cenários (não termos técnicos)
- CA-02: A skill inclui o formato Given-When-Then ou equivalente acessível
- CA-03: A skill define o que acontece em caso de rejeição (não apenas aprovação)
- CA-04: A skill diferencia UAT de testes de sistema (quem testa e com qual critério)

---

## Score deste SDD

| Dimensão | Score | Status |
|----------|-------|--------|
| Completude | 29/30 | Fronteiras semânticas bem definidas entre os 3 níveis |
| Testabilidade | 25/25 | Todos os CAs são verificáveis |
| Clareza | 20/20 | Pirâmide de testes contextualizada |
| Escopo | 15/15 | Non-goals explícitos em cada skill |
| Edge Cases | 9/10 | Cobertos nas principais |
| **TOTAL** | **98/100** | ✅ PRONTO PARA IMPLEMENTAÇÃO |
