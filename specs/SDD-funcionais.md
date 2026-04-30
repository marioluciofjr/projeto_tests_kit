# SDD — Testes Funcionais de Método

> **Categoria IBM:** Testes Funcionais
> **Skills:** Ad-hoc · API · Exploratório · Regressão · Sanidade · Fumaça
> **IDs PRD:** RF-10 a RF-15

---

## SPEC-03 — Skill: teste-ad-hoc

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-10 |
| **Nome** | teste-ad-hoc |
| **Categoria IBM** | Testes Funcionais de Método |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-exploratorio (estruturado), teste-de-fumaca (pós-build) |

### Comportamento Esperado

Quando ativada, esta skill conduz o agente a guiar o desenvolvedor em testes **completamente livres, sem script ou planejamento prévio**. Diferente do exploratório (que tem sessão e charter), o ad-hoc é pura intuição guiada pela experiência. O agente deve:

1. Confirmar que o usuário quer liberdade total (sem roteiro)
2. Sugerir áreas de maior risco para começar
3. Incentivar anotações rápidas de achados
4. Ajudar a documentar bugs encontrados

### Gatilhos de Ativação

- "testar sem planejamento", "teste ad-hoc", "teste livre"
- "quero só clicar por aí e ver o que quebra"
- "não tenho tempo para escrever testes formais agora"
- "quero fazer um teste rápido antes de entregar"
- Qualquer contexto de teste sem script predefinido e sem sessão estruturada

### Quando NÃO usar (Fronteira Semântica)

- Quando o objetivo é descoberta sistemática → usar `teste-exploratorio`
- Quando é pós-deploy e quer validar o básico → usar `teste-de-fumaca`
- Quando é validação de regressão → usar `teste-de-regressao`

### Fluxo de Execução

```
Passo 1: CONTEXTO RÁPIDO
  → Perguntar: o que foi mudado/construído?
  → Identificar: qual área tem maior risco?

Passo 2: EXPLORAÇÃO LIVRE
  → Sugerir começar pelos casos que "parecem óbvios mas ninguém testa"
  → Tentar: inputs inesperados, ordem diferente de ações, duplos cliques

Passo 3: REGISTRO DE ACHADOS
  → Anotar cada comportamento inesperado com: o que fiz → o que aconteceu → o que esperava

Passo 4: TRIAGEM
  → Classificar achados: bug crítico / comportamento estranho / melhoria
```

### Critérios de Aceite

- CA-01: A skill deixa claro que não há script predefinido
- CA-02: A skill sugere focar em áreas de maior risco
- CA-03: A skill incentiva registro de achados mesmo que informal
- CA-04: A skill diferencia-se do exploratório (sem sessão/charter/heurística formal)

---

## SPEC-04 — Skill: teste-de-API

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-11 |
| **Nome** | teste-de-API |
| **Categoria IBM** | Testes Funcionais de Método |
| **Nível** | Intermediário |
| **Skills relacionadas** | teste-de-caixa-preta, teste-de-integracao, teste-de-seguranca |

### Comportamento Esperado

Quando ativada, esta skill conduz o agente a guiar o desenvolvedor em validação completa de APIs — contratos, endpoints, payloads, autenticação, códigos de status e comportamento sob condições de erro. O agente deve trabalhar agnóstico de ferramenta (funciona com Postman, curl, insomnia, código, etc.).

### Gatilhos de Ativação

- "testar API", "teste de API", "API testing"
- "validar endpoints", "testar REST", "testar GraphQL", "testar contrato"
- "verificar se a API está retornando certo"
- "testar autenticação da API", "testar headers"
- "quero criar uma coleção de testes para minha API"
- "como testar meus endpoints antes de entregar"

### Contrato de Entrada

- Documentação da API (OpenAPI/Swagger, Postman Collection, ou descrição manual)
- Credenciais de autenticação (se houver)
- Ambiente a testar (dev, staging, produção)

### Contrato de Saída

- Lista de casos de teste por endpoint (método + path)
- Para cada caso: método HTTP, headers, body, status esperado, body de resposta esperado
- Casos de erro (401, 403, 404, 422, 500)
- Casos de autenticação (token válido, expirado, ausente, inválido)

### Fluxo de Execução

```
Passo 1: MAPEAMENTO DE ENDPOINTS
  → Listar todos os endpoints a testar
  → Agrupar por recurso (ex: /users, /products, /orders)

Passo 2: TESTES DE CONTRATO BÁSICO
  → Para cada endpoint: testar o caminho feliz (request válido → response esperado)
  → Verificar: status code correto, estrutura do response, campos obrigatórios presentes

Passo 3: TESTES DE AUTENTICAÇÃO
  → Sem token → deve retornar 401
  → Token expirado → deve retornar 401
  → Token de outro usuário → deve retornar 403 (se dados são privados)
  → Token válido → deve retornar 200

Passo 4: TESTES DE VALIDAÇÃO DE INPUT
  → Campos obrigatórios ausentes → deve retornar 400/422
  → Tipos errados (string onde espera número) → deve retornar 400/422
  → Valores extremos (strings muito longas, números negativos) → comportamento definido

Passo 5: TESTES DE ERRO E RESILIÊNCIA
  → Recurso inexistente → deve retornar 404
  → Método HTTP errado → deve retornar 405
  → Payload malformado (JSON inválido) → deve retornar 400

Passo 6: TESTES DE IDEMPOTÊNCIA (se aplicável)
  → PUT/DELETE: chamar duas vezes → mesmo resultado?
  → POST: chamar duas vezes → cria duplicata ou retorna erro?

Passo 7: DOCUMENTAÇÃO
  → Consolidar todos os casos em tabela: endpoint | método | cenário | input | status esperado | body esperado
```

### Critérios de Qualidade

- Pelo menos 1 caso de caminho feliz por endpoint
- Todos os cenários de autenticação testados
- Códigos de erro documentados com comportamento esperado
- Testes de validação de input para todos os campos obrigatórios
- Casos de teste são independentes (não dependem de estado de outros testes)

### Edge Cases

| Situação | Como tratar |
|---------|------------|
| API sem documentação | Usar caixa-preta: descobrir comportamento via chamadas exploratórias |
| API com estado (ex: workflow) | Definir ordem dos testes + setup/teardown explícito |
| API com rate limiting | Incluir caso de teste específico para limite de requisições |
| Payloads muito grandes | Testar limites de tamanho (413 Payload Too Large) |

### Critérios de Aceite

- CA-01: A skill lista endpoints a testar antes de criar casos de teste
- CA-02: A skill inclui casos de autenticação (válida, inválida, ausente)
- CA-03: A skill inclui casos de validação de input (campos ausentes, tipos errados)
- CA-04: A skill cobre pelo menos: 200, 400, 401, 404
- CA-05: Os casos de teste são agnósticos de ferramenta (funcionam em qualquer HTTP client)

---

## SPEC-05 — Skill: teste-exploratorio

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-12 |
| **Nome** | teste-exploratorio |
| **Categoria IBM** | Testes Funcionais de Método |
| **Nível** | Intermediário / Avançado |
| **Skills relacionadas** | teste-ad-hoc (livre), teste-de-usabilidade |

### Comportamento Esperado

Quando ativada, esta skill estrutura o processo de teste exploratório em **sessões com charter definido**, aplicando heurísticas conhecidas (HICCUPPS, SFDPOT, mnemonics de Michael Bolton/James Bach). É sistemático mas flexível.

### Gatilhos de Ativação

- "teste exploratório", "explorar o sistema", "session-based testing"
- "quero descobrir bugs que não sabia que existiam"
- "teste com heurísticas", "testar com charter"
- "preciso investigar essa funcionalidade profundamente"
- "testar como um usuário mal-intencionado/criativo"

### Quando NÃO usar

- Quando quer liberdade total sem estrutura → usar `teste-ad-hoc`
- Quando já sabe exatamente o que quer testar → usar skill específica (ex: `teste-de-API`)

### Fluxo de Execução

```
Passo 1: DEFINIR CHARTER DA SESSÃO
  → Missão: "Explorar [área/funcionalidade] para encontrar [tipo de problema]"
  → Duração: 60-90 minutos (timeboxed)
  → Recursos necessários: ambiente, dados, ferramentas

Passo 2: ESCOLHER HEURÍSTICAS
  → SFDPOT: Structure, Function, Data, Platform, Operations, Time
  → HICCUPPS: History, Image, Claims, Comparable, User, Product, Purpose, Statutes
  → Ou mnemonics: CRUD (Create, Read, Update, Delete) + extremos

Passo 3: EXECUTAR SESSÃO
  → Explorar seguindo as heurísticas escolhidas
  → Anotar: ação → comportamento observado → esperado → bug? (sim/não)
  → Registrar tempo em cada área

Passo 4: DEBRIEFING
  → Resumir: o que foi testado, o que foi encontrado, o que ficou sem testar
  → Classificar achados
  → Planejar próxima sessão se necessário

Passo 5: DOCUMENTAÇÃO
  → Session report: charter, duração, % de execução vs. investigação, bugs encontrados
```

### Critérios de Aceite

- CA-01: A skill define um charter antes de explorar
- CA-02: A skill menciona ao menos uma heurística de teste
- CA-03: A skill usa sessão timeboxed
- CA-04: A skill produz session report ao final

---

## SPEC-06 — Skill: teste-de-regressao

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-13 |
| **Nome** | teste-de-regressao |
| **Categoria IBM** | Testes Funcionais de Método |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-de-fumaca (subconjunto rápido), teste-de-sanidade (pós-mudança local) |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor a **garantir que funcionalidades existentes continuam funcionando** após uma mudança (novo código, refatoração, correção de bug). O foco é: o que foi mudado pode ter quebrado o que já funcionava?

### Gatilhos de Ativação

- "teste de regressão", "regression testing"
- "quero garantir que não quebrei nada"
- "fiz uma mudança e quero verificar o que impactou"
- "validar depois de um merge/PR"
- "o que testar antes de um release?"
- "minha refatoração pode ter quebrado algo"

### Quando NÃO usar

- Para validar apenas uma funcionalidade específica → usar `teste-de-sanidade`
- Para validar se o sistema sobe → usar `teste-de-fumaca`
- Para testar funcionalidade nova → usar skill de técnica (caixa-preta ou caixa-branca)

### Fluxo de Execução

```
Passo 1: IDENTIFICAR IMPACTO DA MUDANÇA
  → O que foi alterado? (arquivo, módulo, serviço)
  → Quais funcionalidades dependem do que foi alterado?
  → Análise de dependências: o que chama ou é chamado pelo código modificado

Passo 2: PRIORIZAR SUÍTE DE REGRESSÃO
  → Prioridade Alta: funcionalidades diretamente afetadas
  → Prioridade Média: funcionalidades que dependem das afetadas
  → Prioridade Baixa: funcionalidades não relacionadas (smoke test suficiente)

Passo 3: EXECUTAR REGRESSÃO SELETIVA
  → Rodar testes de Prioridade Alta primeiro
  → Se passarem: rodar Prioridade Média
  → Se passarem: smoke test nas demais

Passo 4: ANÁLISE DE FALHAS
  → Algum teste falhou? → Documentar: qual teste, mensagem de erro, provável causa
  → A falha é na funcionalidade mudada ou em algo inesperado?

Passo 5: ATUALIZAR SUÍTE
  → Se a mudança muda o comportamento intencionalmente: atualizar testes antigos
  → Se bugs foram encontrados: criar novos testes para os cenários descobertos
```

### Critérios de Aceite

- CA-01: A skill pede qual mudança foi feita antes de definir o escopo
- CA-02: A skill categoriza testes por impacto (alta/média/baixa prioridade)
- CA-03: A skill distingue regressão seletiva de regressão completa
- CA-04: A skill menciona quando atualizar testes existentes

---

## SPEC-07 — Skill: teste-de-sanidade

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-14 |
| **Nome** | teste-de-sanidade |
| **Categoria IBM** | Testes Funcionais de Método |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-de-fumaca (sistema inteiro), teste-de-regressao (abrangente) |

### Fronteira Semântica (crítica)

| | Fumaça | Sanidade | Regressão |
|-|--------|----------|-----------|
| **Escopo** | Sistema inteiro | Uma funcionalidade | Funcionalidades afetadas |
| **Profundidade** | Superficial | Moderada | Profunda |
| **Gatilho** | Novo build | Mudança local | Qualquer mudança |
| **Duração** | < 15 min | 15-30 min | 30 min - horas |

### Gatilhos de Ativação

- "teste de sanidade", "sanity check", "sanity test"
- "quero verificar rapidamente se essa feature ainda funciona"
- "fiz uma pequena correção e quero testar só essa parte"
- "verificação rápida antes de passar para QA"

### Fluxo de Execução

```
Passo 1: IDENTIFICAR A FUNCIONALIDADE
  → Qual funcionalidade específica foi tocada?
  → Quais são os casos de uso principais dessa funcionalidade?

Passo 2: EXECUTAR CENÁRIOS BÁSICOS
  → Testar apenas o caminho feliz da funcionalidade modificada
  → Testar 1-2 casos de erro mais comuns
  → NÃO testar casos de borda ou edge cases nesta fase

Passo 3: DECISÃO GO/NO-GO
  → Passou nos básicos? → Pode avançar para testes mais completos
  → Falhou nos básicos? → Reportar e não avançar
```

### Critérios de Aceite

- CA-01: A skill foca em UMA funcionalidade específica (não o sistema todo)
- CA-02: A skill propõe no máximo 5-8 casos de teste (sanidade, não regressão completa)
- CA-03: A skill diferencia claramente de fumaça e regressão

---

## SPEC-08 — Skill: teste-de-fumaca

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-15 |
| **Nome** | teste-de-fumaca |
| **Categoria IBM** | Testes Funcionais de Método |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-de-sanidade (funcionalidade), teste-de-regressao (completo) |

### Comportamento Esperado

Quando ativada, esta skill guia o desenvolvedor em um teste rápido e superficial do **sistema como um todo** — o objetivo é determinar se o build/deploy foi bem-sucedido e se as funcionalidades críticas básicas respondem. Se falhar na fumaça, não se avança para testes mais profundos.

### Gatilhos de Ativação

- "teste de fumaça", "smoke test", "smoke testing"
- "o sistema subiu?", "o deploy funcionou?"
- "validar o build", "checar se está de pé"
- "testes de build verification"
- "preciso saber se o sistema básico está ok antes de testar mais"
- Qualquer contexto pós-deploy ou pós-build

### Quando NÃO usar

- Para validar uma funcionalidade específica → usar `teste-de-sanidade`
- Para garantir que nada quebrou → usar `teste-de-regressao`
- Para testar profundamente → usar skill específica do tipo de teste

### Fluxo de Execução

```
Passo 1: IDENTIFICAR FUNCIONALIDADES CRÍTICAS
  → O que é ESSENCIAL para o sistema funcionar? (lista de 5-10 itens máximo)
  → Ex: login, home page carrega, operação principal responde, DB conecta

Passo 2: CRIAR SUÍTE DE FUMAÇA
  → Um caso de teste por funcionalidade crítica (caminho feliz APENAS)
  → Deve ser executado em < 15 minutos no total
  → Automático é preferível, mas manual é aceitável

Passo 3: EXECUTAR E DECIDIR
  → Todos passaram → sistema está "vivo" → avançar para testes mais profundos
  → Qualquer falha → PARAR — o build está quebrado — reportar antes de avançar

Passo 4: DOCUMENTAR RESULTADO
  → Registrar: data, versão do build, resultado (pass/fail), falhas encontradas
```

### Critérios de Qualidade

- Suíte de fumaça completa em < 15 minutos
- No máximo 10-15 casos de teste por suíte
- Cada caso testa apenas o caminho feliz
- Sem testes de casos de borda ou edge cases (isso é para regressão)
- Resultado é binário: PASS (avança) ou FAIL (para)

### Critérios de Aceite

- CA-01: A skill foca no sistema inteiro, não em uma funcionalidade
- CA-02: A skill propõe suíte que cabe em 15 minutos
- CA-03: A skill orienta a PARAR se qualquer caso falhar
- CA-04: A skill diferencia-se da sanidade e regressão

---

## Score deste SDD

| Dimensão | Score | Status |
|----------|-------|--------|
| Completude | 28/30 | Exemplos conceituais resumidos (sem pseudocódigo extenso) |
| Testabilidade | 25/25 | Todos CAs são verificáveis |
| Clareza | 20/20 | Fronteiras semânticas explícitas entre skills similares |
| Escopo | 14/15 | Workflows detalhados para todas as 6 skills |
| Edge Cases | 9/10 | Cobertos nas principais skills |
| **TOTAL** | **96/100** | ✅ PRONTO PARA IMPLEMENTAÇÃO |
