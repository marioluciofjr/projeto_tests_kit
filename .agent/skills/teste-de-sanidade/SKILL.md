---
name: teste-de-sanidade
description: >
  Guia o desenvolvedor em uma verificação rápida e focada de uma funcionalidade específica após
  uma mudança local ou correção de bug. Use esta skill SEMPRE que o objetivo for confirmar que uma
  funcionalidade específica ainda está funcionando após uma alteração pequena, sem executar a suíte
  completa de testes. Acione quando o usuário mencionar: "teste de sanidade", "sanity check",
  "sanity test", "quero verificar rapidamente se essa feature ainda funciona", "fiz uma pequena
  correção e quero testar só essa parte", "verificação rápida antes de passar para QA",
  "checar se minha mudança não quebrou a feature". Diferente da fumaça (sistema inteiro, superficial)
  e da regressão (abrangente, todas as funcionalidades afetadas), a sanidade foca em UMA
  funcionalidade com profundidade moderada. Dura entre 15 e 30 minutos.
categoria_ibm: Testes Funcionais de Método
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-de-fumaca
  - teste-de-regressao
---

# Teste de Sanidade

## O que é

O teste de sanidade é uma verificação rápida e focada em uma funcionalidade específica, realizada após uma mudança local para confirmar que ela ainda se comporta conforme esperado. "Sanidade" no sentido de "isso ainda faz sentido?" — um teste leve e direcionado que não precisa cobrir tudo, mas deve cobrir o essencial daquela funcionalidade.

## Quando usar

- Após uma correção de bug em uma funcionalidade específica
- Após uma pequena alteração no código de uma única feature
- Antes de passar o trabalho para code review ou QA
- Quando quer confirmar rapidamente que sua mudança não quebrou o fluxo principal
- Quando não tem tempo para regressão completa mas precisa de alguma validação

## Quando NÃO usar

- Para verificar se o sistema como um todo está de pé → use `teste-de-fumaca`
- Para verificar todas as funcionalidades afetadas por uma mudança → use `teste-de-regressao`
- Para testar em profundidade com casos de borda e edge cases → use caixa-branca ou caixa-preta

## Como funciona — Processo Passo a Passo

**Passo 1: Identificar a funcionalidade**
Qual funcionalidade específica foi tocada pela mudança? Qual é o seu fluxo principal?

**Passo 2: Definir os casos de sanidade**
Liste de 5 a 8 casos de teste que cobrem o caminho feliz e os 1-2 cenários de erro mais comuns dessa funcionalidade. Não inclua casos de borda ou edge cases — isso é para a regressão completa.

**Passo 3: Executar rapidamente**
Execute os casos. Objetivo: terminar em 15 a 30 minutos no máximo.

**Passo 4: Decisão Go / No-Go**
- Todos passaram → pode avançar para code review, QA ou merge
- Qualquer falha → investigate e corrija antes de avançar

## Critérios de Qualidade

- Foca em UMA funcionalidade específica (não o sistema todo)
- No máximo 5 a 8 casos de teste (não é regressão completa)
- Cobre o caminho feliz e os cenários de erro mais comuns
- Executável em até 30 minutos
- Resultado binário e claro: a feature está funcionando ou não

## Exemplo Conceitual

**Cenário:** Correção de bug no formulário de login — campo de senha aceitava espaços em branco.

Casos de sanidade (5 casos):
| Caso | Entrada | Resultado esperado |
|------|---------|-------------------|
| Caminho feliz | e-mail válido + senha válida | Login realizado com sucesso |
| Senha com espaços (bug corrigido) | e-mail válido + "   " | Erro: senha inválida |
| Credenciais inválidas | e-mail válido + senha errada | Erro: credenciais inválidas |
| E-mail inválido | "nao-e-email" + senha válida | Erro: e-mail inválido |
| Campos vazios | vazio + vazio | Erro: preencha todos os campos |

Tempo estimado: ~10 minutos para executar manualmente.

## Checklist de Conclusão

- [ ] Identifiquei qual funcionalidade específica foi alterada?
- [ ] Criei no máximo 5 a 8 casos focados nessa funcionalidade?
- [ ] Cobri o caminho feliz E os cenários de erro mais comuns?
- [ ] NÃO incluí casos de borda ou edge cases (isso é para regressão)?
- [ ] Executei em no máximo 30 minutos?
- [ ] Tomei a decisão de Go/No-Go com base nos resultados?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-fumaca` | Escopo maior — sistema inteiro, superficial | Quando quer verificar se o sistema todo está de pé, não só uma feature |
| `teste-de-regressao` | Escopo maior — todas as funcionalidades afetadas | Quando a mudança pode ter impactado outras áreas além da feature alterada |
