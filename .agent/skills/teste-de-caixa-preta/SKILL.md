---
name: teste-de-caixa-preta
description: >
  Guia o desenvolvedor na criação de testes baseados exclusivamente no comportamento externo do
  sistema, sem acesso ou análise do código-fonte. Use esta skill SEMPRE que o objetivo for
  validar se o sistema faz o que foi especificado, testar como um usuário ou consumidor de API,
  aplicar partição de equivalência ou análise de valor de borda. Acione quando o usuário mencionar:
  "teste funcional", "teste de caixa preta", "black box test", "testar sem ver o código", "testar
  como usuário", "partição de equivalência", "valor de borda", "boundary testing", "testar com
  base nos requisitos", "validar o comportamento esperado", "testar uma API sem saber como foi
  implementada". Diferente da caixa branca (que analisa caminhos internos do código), a caixa preta
  parte dos requisitos e especificações. Funciona para qualquer linguagem e é ideal quando o testador
  não tem ou não quer acessar a implementação interna.
categoria_ibm: Técnicas de Projeto de Teste
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-de-caixa-branca
  - teste-de-API
  - teste-de-aceitacao-do-usuario
---

# Teste de Caixa Preta

## O que é

O teste de caixa preta (ou teste funcional) é uma técnica em que o testador cria casos de teste baseando-se exclusivamente na especificação e no comportamento externo do sistema — sem nenhum acesso ou conhecimento do código interno. É chamado de "caixa preta" porque a implementação está oculta: o que importa é a entrada fornecida e a saída produzida. Essa é a técnica mais utilizada para validar se o software faz exatamente o que foi pedido, seja por um usuário, uma API ou um contrato de negócio.

## Quando usar

- Quando quer testar o comportamento de uma funcionalidade como um usuário real
- Quando não tem acesso ao código-fonte (biblioteca de terceiros, API externa, produto legado)
- Quando quer validar se os requisitos funcionais estão sendo atendidos
- Quando quer aplicar partição de equivalência para reduzir o número de casos de teste necessários
- Quando precisa cobrir os valores de borda (mínimo, máximo, limites) de um campo de entrada
- Quando quer criar testes de aceitação ou de regressão funcional
- Quando uma especificação ou user story define claramente o que deve acontecer

## Quando NÃO usar

- Quando quer verificar cobertura de caminhos internos do código → use `teste-de-caixa-branca`
- Quando o comportamento esperado não está documentado em nenhum lugar → defina o comportamento primeiro
- Quando quer analisar performance ou segurança em profundidade → use skills especializadas

## Como funciona — Processo Passo a Passo

**Passo 1: Análise de requisitos**
Leia a especificação, user story ou descrição do comportamento esperado. Identifique: quais são os dados de entrada aceitos, quais restrições existem, qual é o resultado esperado para cada cenário.

**Passo 2: Partição de equivalência**
Divida o domínio de entrada em classes (partições). Cada classe representa um conjunto de valores que devem ser tratados da mesma forma pelo sistema. Crie pelo menos:
- Uma partição **válida** (dados aceitos normalmente)
- Uma ou mais partições **inválidas** (dados que devem ser rejeitados)
- Um representante de cada partição é suficiente para um caso de teste

**Passo 3: Análise de valor de borda**
Para cada faixa ou limite: teste os valores exatamente nas bordas. Se o campo aceita de 1 a 100, teste: 0 (inválido), 1 (borda mínima), 2 (logo acima), 99 (logo abaixo), 100 (borda máxima), 101 (inválido). Os bugs se escondem nas bordas.

**Passo 4: Tabela de decisão (quando há regras)**
Se o comportamento depende de múltiplas condições combinadas, crie uma tabela onde cada coluna representa uma combinação de condições e o resultado esperado. Derive um caso de teste por coluna relevante.

**Passo 5: Casos de teste especiais**
Sempre inclua: valor nulo ou vazio, tipo de dado incorreto (texto onde espera número), valor típico do dia a dia, valor de pico esperado.

**Passo 6: Consolidação**
Agrupe todos os casos de teste em uma tabela: ID, partição ou borda que representa, entrada, saída esperada.

**Passo 7: Verificação de cobertura funcional**
Verifique se todas as regras de negócio da especificação têm pelo menos um caso de teste. Verifique se todos os cenários de erro têm um caso.

## Critérios de Qualidade

- Pelo menos uma partição válida e uma inválida por campo de entrada
- Todos os valores de borda identificados e representados por casos de teste
- Casos de teste incluem: nulo, vazio, valor mínimo, valor máximo, valor típico e valor inválido
- Nenhum caso de teste depende do conhecimento do código interno
- Cada caso documenta o comportamento de erro esperado (não apenas os casos de sucesso)
- Casos de teste são derivados de requisitos documentados (rastreáveis)

## Exemplo Conceitual

**Cenário:** Um campo de formulário que aceita a "idade do usuário" para cadastro.

Especificação: *Idade deve ser um número inteiro entre 18 e 120 anos.*

Partições de equivalência:
| Partição | Descrição | Representante |
|---------|-----------|--------------|
| Válida | Idade dentro do intervalo | 30 |
| Inválida (abaixo) | Menor de 18 | 15 |
| Inválida (acima) | Maior de 120 | 150 |
| Inválida (tipo) | Não é número | "abc" |
| Inválida (vazia) | Campo não preenchido | vazio |

Valores de borda do intervalo [18, 120]:
| Valor | Resultado esperado |
|-------|-------------------|
| 17 | Rejeitado — menor que o mínimo |
| 18 | Aceito — borda mínima |
| 19 | Aceito — logo acima do mínimo |
| 119 | Aceito — logo abaixo do máximo |
| 120 | Aceito — borda máxima |
| 121 | Rejeitado — acima do máximo |

## Checklist de Conclusão

- [ ] Identifiquei todas as partições de equivalência válidas e inválidas?
- [ ] Criei casos de teste para os valores de borda de cada campo?
- [ ] Tenho casos para: nulo, vazio, tipo errado, valor típico, valor extremo?
- [ ] Cada caso de teste especifica a entrada E a saída esperada?
- [ ] Os casos de erro descrevem o que o sistema DEVE fazer ao receber dados inválidos?
- [ ] Todas as regras de negócio da especificação têm pelo menos um caso de teste cobrindo-as?
- [ ] Os casos de teste são independentes do código interno (não assumo nada sobre a implementação)?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-caixa-branca` | Complementar — testa os caminhos internos do mesmo componente | Quando tem acesso ao código e quer garantir cobertura de ramos |
| `teste-de-API` | Especialização — aplica caixa preta em endpoints HTTP | Quando o objeto de teste é uma API REST ou similar |
| `teste-de-aceitacao-do-usuario` | Nível acima — validação com o usuário real | Quando quer que o próprio usuário/cliente execute os cenários |
