# SDD — Técnicas de Projeto de Teste

> **Categoria IBM:** Técnicas de Projeto de Teste
> **Skills:** Caixa Branca · Caixa Preta
> **IDs PRD:** RF-08, RF-09
> **Score mínimo para implementação:** 80/100

---

## SPEC-01 — Skill: teste-de-caixa-branca

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-08 |
| **Nome** | teste-de-caixa-branca |
| **Categoria IBM** | Técnicas de Projeto de Teste |
| **Nível** | Intermediário / Avançado |
| **Skills relacionadas** | teste-de-caixa-preta, teste-de-unidade (agent), teste-de-integracao |

### Comportamento Esperado

Quando ativada, esta skill conduz o agente a guiar o desenvolvedor em um processo sistemático de criação de testes baseados no **conhecimento interno do código-fonte**. O agente deve:

1. Solicitar ou analisar o código a ser testado
2. Mapear todos os caminhos de execução possíveis (paths)
3. Identificar condições, loops, branches e decisões no código
4. Propor casos de teste que cubram cada caminho identificado
5. Calcular ou estimar a cobertura de código obtida
6. Identificar caminhos não cobertos e propor testes adicionais

### Gatilhos de Ativação (para description)

A skill DEVE ser acionada quando o usuário mencionar:
- "cobertura de código", "code coverage"
- "teste estrutural", "teste de caixa branca", "white box test"
- "quero testar todos os caminhos do meu código"
- "como cobrir esse if/else/loop com testes"
- "análise de fluxo de controle"
- "teste de caminho", "path testing"
- Situações em que o desenvolvedor tem o código e quer testá-lo internamente

### Contrato de Entrada

O agente deve coletar ou ter acesso a:
- O código-fonte do componente a ser testado (ou uma descrição estrutural dele)
- O critério de cobertura desejado (declaração, ramo, caminho, condição)
- O nível de cobertura mínimo aceitável (ex: 80%, 90%, 100%)

Se não fornecidos, o agente DEVE perguntar antes de prosseguir.

### Contrato de Saída

A skill DEVE produzir:
- Lista de casos de teste (input → caminho percorrido → output esperado)
- Mapa de caminhos identificados no código
- Estimativa de cobertura por critério (declaração, ramo, condição)
- Lista de caminhos não cobertos (se houver)
- Sugestão de casos de teste adicionais para cobertura total

### Fluxo de Execução (Passo a Passo)

```
Passo 1: ANÁLISE ESTRUTURAL
  → Receber ou analisar o código
  → Identificar: funções/métodos, condicionais (if/switch), loops (for/while), retornos e exceções
  → Construir grafo de fluxo de controle mental/visual

Passo 2: IDENTIFICAÇÃO DE CAMINHOS
  → Listar todos os caminhos possíveis do início ao fim
  → Priorizar: Caminho Feliz (happy path) → Caminhos de Erro → Casos de Borda

Passo 3: DESIGN DE CASOS DE TESTE
  → Para cada caminho: definir entrada que força aquele caminho
  → Para cada condição booleana: testar TRUE e FALSE
  → Para cada loop: testar 0 iterações, 1 iteração, N iterações

Passo 4: VERIFICAÇÃO DE COBERTURA
  → Mapear quais declarações cada teste cobre
  → Calcular % de cobertura por critério
  → Identificar buracos na cobertura

Passo 5: COMPLETAR COBERTURA
  → Propor casos de teste para caminhos não cobertos
  → Verificar se cobertura mínima foi atingida

Passo 6: DOCUMENTAÇÃO
  → Listar todos os casos com: ID, caminho coberto, input, output esperado
  → Apresentar mapa de cobertura final
```

### Critérios de Qualidade

- Pelo menos um caso de teste para cada ramo de decisão (TRUE e FALSE)
- Cada loop tem casos para: não executar, executar uma vez, executar múltiplas vezes
- Casos de teste incluem explicitamente qual caminho cobrem
- Cobertura de declarações ≥ 80% (mínimo aceitável)
- Cobertura de ramos ≥ 70% (mínimo aceitável)
- Casos de exceção/erro têm testes dedicados

### Edge Cases

| Situação | Como tratar |
|---------|------------|
| Código sem condicionais | Informar que um único teste pode cobrir 100% — verificar se há casos de borda de entrada |
| Loops infinitos | Identificar como risco; propor testes com condição de saída garantida |
| Código muito complexo (ciclomática > 10) | Sugerir refatoração + testar incrementalmente |
| Sem acesso ao código (só à descrição) | Basear-se na descrição + perguntar sobre ramificações conhecidas |
| Recursão | Testar: caso base, caso recursivo simples, recursão profunda |

### Critérios de Aceite (Testáveis)

- CA-01: A skill pergunta pelo código ou sua descrição antes de começar
- CA-02: A skill identifica pelo menos 3 tipos de estruturas (condicionais, loops, retornos)
- CA-03: A skill propõe teste para o caminho feliz E para pelo menos um caminho de erro
- CA-04: A skill calcula ou estima cobertura (não apenas lista testes)
- CA-05: A skill menciona explicitamente a diferença entre cobertura de declaração e ramo
- CA-06: A skill diferencia-se da caixa preta na seção "Quando NÃO usar"

---

## SPEC-02 — Skill: teste-de-caixa-preta

### Metadados

| Campo | Valor |
|-------|-------|
| **ID PRD** | RF-09 |
| **Nome** | teste-de-caixa-preta |
| **Categoria IBM** | Técnicas de Projeto de Teste |
| **Nível** | Todos os níveis |
| **Skills relacionadas** | teste-de-caixa-branca, teste-de-API, teste-de-aceitacao-do-usuario |

### Comportamento Esperado

Quando ativada, esta skill conduz o agente a guiar o desenvolvedor em criação de testes baseados **exclusivamente no comportamento externo** do sistema — sem acesso ou análise do código interno. O agente deve:

1. Partir dos requisitos, especificações ou comportamento documentado
2. Aplicar técnicas de partição de equivalência para reduzir casos de teste
3. Aplicar análise de valor de borda para cobrir extremos
4. Criar tabelas de decisão para regras de negócio complexas
5. Definir os outputs esperados para cada combinação de input

### Gatilhos de Ativação

A skill DEVE ser acionada quando o usuário mencionar:
- "teste funcional", "teste de caixa preta", "black box test"
- "testar sem ver o código", "testar como usuário"
- "partição de equivalência", "valor de borda", "boundary testing"
- "testar com base nos requisitos"
- "validar o comportamento esperado"
- "testar uma API que recebi sem saber como foi implementada"
- Situações em que o testador não tem ou não quer acessar o código

### Contrato de Entrada

- Especificação funcional ou descrição do comportamento esperado
- Regras de negócio aplicáveis
- Formato de entrada e saída da função/sistema/API

### Contrato de Saída

- Tabela de partições de equivalência (válidas e inválidas)
- Lista de valores de borda identificados
- Casos de teste derivados de cada partição e borda
- Tabela de decisão (se aplicável)
- Casos de teste de caminho feliz + casos negativos

### Fluxo de Execução

```
Passo 1: ANÁLISE DE REQUISITOS
  → Ler e compreender a especificação/comportamento esperado
  → Identificar: entradas, saídas, restrições e regras

Passo 2: PARTIÇÃO DE EQUIVALÊNCIA
  → Dividir o domínio de entrada em classes válidas e inválidas
  → Regra: um representante de cada classe é suficiente
  → Ex: campo "idade" → [válido: 1-120] [inválido: <0] [inválido: >120] [inválido: não-numérico]

Passo 3: ANÁLISE DE VALOR DE BORDA
  → Para cada faixa: testar min, min+1, max-1, max
  → Testar exatamente nos limites (onde bugs costumam se esconder)

Passo 4: TABELA DE DECISÃO (se houver múltiplas regras)
  → Mapear combinações de condições → ações
  → Criar um caso de teste para cada coluna relevante da tabela

Passo 5: CASOS DE TESTE
  → Consolidar todos os casos com: input, classe/borda que representa, output esperado
  → Incluir: caminho feliz, entradas inválidas, bordas, nulos/vazios

Passo 6: VALIDAÇÃO DE COBERTURA FUNCIONAL
  → Verificar se todas as regras de negócio têm pelo menos um teste
  → Verificar se todos os cenários de erro têm um teste
```

### Critérios de Qualidade

- Pelo menos uma partição válida e uma inválida por parâmetro de entrada
- Todos os valores de borda identificados e testados
- Casos de teste incluem: nulo, vazio, valor mínimo, valor máximo, valor típico
- Nenhum caso de teste depende do conhecimento do código interno
- Casos negativos documentam o comportamento de erro esperado

### Edge Cases

| Situação | Como tratar |
|---------|------------|
| Sem especificação formal | Perguntar pelo comportamento observado/desejado; documentar assunções |
| Muitas combinações de entrada | Usar técnica de pairwise testing para reduzir casos |
| Output não determinístico | Testar propriedades (ex: "sempre retorna lista") ao invés de valores exatos |
| Regras de negócio contraditórias | Identificar e documentar — não criar testes para comportamento indefinido |

### Critérios de Aceite

- CA-01: A skill parte de requisitos/especificação, não de código
- CA-02: A skill explica partição de equivalência com exemplo do contexto do usuário
- CA-03: A skill identifica e testa valores de borda
- CA-04: A skill produz casos de teste com input E output esperado explícitos
- CA-05: A skill menciona casos negativos (entradas inválidas)
- CA-06: A skill diferencia-se da caixa branca na seção "Quando NÃO usar"

---

## Score deste SDD

| Dimensão | Score | Gaps |
|----------|-------|------|
| Completude | 29/30 | Sem exemplos de código em linguagem específica (intencional) |
| Testabilidade | 25/25 | Todos os CAs são sim/não verificáveis |
| Clareza | 20/20 | Fronteiras semânticas claras entre as duas técnicas |
| Escopo | 15/15 | Non-goals implícitos nas seções "Quando NÃO usar" |
| Edge Cases | 10/10 | Cobertos para ambas as skills |
| **TOTAL** | **99/100** | ✅ PRONTO PARA IMPLEMENTAÇÃO |
