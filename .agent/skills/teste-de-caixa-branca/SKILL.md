---
name: teste-de-caixa-branca
description: >
  Guia o desenvolvedor na criação de testes baseados no conhecimento interno do código-fonte.
  Use esta skill SEMPRE que o objetivo for garantir cobertura de caminhos de execução, verificar
  branches, condicionais e loops, ou calcular métricas de cobertura de código. Acione quando o
  usuário mencionar: "cobertura de código", "code coverage", "teste estrutural", "teste de caixa
  branca", "white box test", "quero cobrir todos os caminhos do meu código", "como testar esse
  if/else", "análise de fluxo de controle", "path testing", "cobertura de ramos". Não confundir
  com caixa-preta (que não acessa o código) nem com testes de integração (que testam comunicação
  entre módulos). Esta skill é ideal para desenvolvedores que têm acesso ao código e querem
  garantir que todos os caminhos lógicos estão cobertos por testes. Funciona em qualquer linguagem.
categoria_ibm: Técnicas de Projeto de Teste
nivel_maturidade: Intermediário / Avançado
skills_relacionadas:
  - teste-de-caixa-preta
  - teste-de-integracao
  - teste-de-regressao
---

# Teste de Caixa Branca

## O que é

O teste de caixa branca (ou teste estrutural) é uma técnica em que o testador tem acesso ao código-fonte e cria casos de teste com base na estrutura interna do programa. O objetivo é garantir que todos os caminhos de execução, condições e ramificações do código sejam exercitados por pelo menos um teste. É chamado de "caixa branca" porque a implementação interna está visível — ao contrário da caixa preta, onde só o comportamento externo importa.

## Quando usar

- Quando você tem acesso ao código-fonte do componente a ser testado
- Quando quer garantir uma porcentagem específica de cobertura de código (ex: 80%, 90%)
- Quando existe lógica condicional complexa com múltiplos caminhos possíveis
- Quando quer verificar se casos de erro e exceções estão sendo tratados internamente
- Quando está praticando TDD e quer confirmar que seus testes cobrem toda a implementação
- Quando um code review identifica caminhos de código sem testes
- Quando a equipe tem um critério de cobertura mínima a cumprir

## Quando NÃO usar

- Quando não tem acesso ao código-fonte (ex: testando uma biblioteca de terceiros) → use `teste-de-caixa-preta`
- Quando o objetivo é validar o comportamento do sistema como um todo → use `teste-de-sistema`
- Quando quer testar a comunicação entre dois módulos → use `teste-de-integracao`
- Quando precisa de uma verificação rápida sem análise de código → use `teste-de-fumaca` ou `teste-de-sanidade`

## Como funciona — Processo Passo a Passo

**Passo 1: Análise estrutural**
Leia o código do componente a ser testado. Identifique: funções e métodos, condicionais (`if`/`switch`/`case`), laços de repetição (`for`/`while`/`do-while`), pontos de retorno e lançamento de exceções.

**Passo 2: Mapeamento de caminhos**
Trace todos os caminhos possíveis de execução do início ao fim do componente. Comece pelo caminho feliz (entrada válida → saída esperada), depois os caminhos de erro e condições de borda.

**Passo 3: Critério de cobertura**
Escolha o nível de cobertura a alcançar:
- **Cobertura de declaração:** cada linha de código executada ao menos uma vez
- **Cobertura de ramo:** cada resultado de condição (verdadeiro E falso) testado
- **Cobertura de condição:** cada sub-condição de expressões booleanas compostas testada
- **Cobertura de caminho:** todos os caminhos únicos do grafo de fluxo cobertos

**Passo 4: Design dos casos de teste**
Para cada caminho identificado, defina: qual entrada força esse caminho, qual é o resultado esperado. Para cada condição booleana: escreva um caso onde ela é verdadeira E outro onde é falsa. Para laços: zero iterações, uma iteração, múltiplas iterações.

**Passo 5: Cálculo de cobertura**
Após criar os casos, verifique quais linhas/ramos cada um cobre. Some a cobertura total. Identifique o que ainda está descoberto.

**Passo 6: Complementação**
Para cada trecho de código sem cobertura, crie casos de teste adicionais. Repita até atingir o critério mínimo definido.

**Passo 7: Documentação**
Registre cada caso com: identificador único, caminho que cobre, entrada utilizada, saída esperada e critério de cobertura atendido.

## Critérios de Qualidade

- Cada ramo de cada condicional tem pelo menos um teste para o resultado verdadeiro e um para o falso
- Laços de repetição têm casos para: nunca executar, executar uma vez, executar múltiplas vezes
- Cada ponto de lançamento de exceção tem um caso de teste dedicado
- Casos de teste são independentes entre si (sem dependência de ordem)
- A cobertura de declarações é ≥ 80% (mínimo aceitável)
- A cobertura de ramos é ≥ 70% (mínimo aceitável)
- Cada caso documenta explicitamente qual caminho do código está cobrindo

## Exemplo Conceitual

**Cenário:** Uma função que calcula desconto de um produto.

```
função calcular_desconto(valor, percentual):
  SE valor <= 0:                          # Caminho A: valor inválido
    lançar erro "Valor inválido"
  SE percentual < 0 OU percentual > 100:  # Caminho B: percentual inválido
    lançar erro "Percentual inválido"
  SE percentual == 0:                     # Caminho C: sem desconto
    retornar valor
  retornar valor - (valor * percentual / 100)  # Caminho D: desconto aplicado
```

Casos de teste derivados:
| ID | Entrada | Caminho | Saída esperada |
|----|---------|---------|---------------|
| TC-01 | valor=-10, %=10 | A | Erro "Valor inválido" |
| TC-02 | valor=100, %=-5 | B | Erro "Percentual inválido" |
| TC-03 | valor=100, %=101 | B | Erro "Percentual inválido" |
| TC-04 | valor=100, %=0 | C | 100 |
| TC-05 | valor=200, %=25 | D | 150 |

## Checklist de Conclusão

- [ ] Identifiquei todos os pontos de decisão (condicionais) no código?
- [ ] Criei casos de teste para o resultado verdadeiro E falso de cada condicional?
- [ ] Laços de repetição têm casos para 0, 1 e N iterações?
- [ ] Todos os caminhos de erro e exceções têm testes?
- [ ] Calculei a porcentagem de cobertura atingida?
- [ ] A cobertura está no nível mínimo definido pela equipe (≥ 80% de declarações)?
- [ ] Cada caso de teste documenta qual caminho do código ele cobre?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-caixa-preta` | Complementar — testa o mesmo componente sem ver o código | Quando não tem acesso ao código ou quer testar como usuário |
| `teste-de-integracao` | Nível acima — testa comunicação entre componentes | Quando o componente já tem cobertura unitária suficiente |
| `teste-de-regressao` | Uso conjunto — rode cobertura após mudanças | Quando quer garantir que a mudança não reduziu a cobertura |
