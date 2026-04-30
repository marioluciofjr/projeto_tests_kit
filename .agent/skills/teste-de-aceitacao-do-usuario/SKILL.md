---
name: teste-de-aceitacao-do-usuario
description: >
  Guia o desenvolvedor ou Product Manager na estruturação do processo de validação com o usuário
  final ou stakeholder do negócio — o UAT (User Acceptance Testing). Use esta skill SEMPRE que o
  objetivo for preparar e conduzir a homologação de uma entrega com o cliente ou usuário real.
  Acione quando o usuário mencionar: "UAT", "User Acceptance Testing", "teste de aceitação",
  "o cliente vai testar o sistema", "entregar para homologação", "quero preparar o UAT", "critérios
  de aceitação", "o usuário precisa aprovar a entrega", "homologação com o cliente", "BDD",
  "Given-When-Then" (no contexto de aceitação de entrega), "aceite do cliente", "aprovação do
  stakeholder". Diferente do teste de sistema (feito pelo time técnico), o UAT envolve o usuário
  final ou negócio como principal validador. Usa linguagem de negócio, não técnica. Agnóstico
  de linguagem de programação.
categoria_ibm: Testes por Nível
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-de-sistema
  - teste-de-usabilidade
---

# Teste de Aceitação do Usuário (UAT)

## O que é

O UAT (User Acceptance Testing) é o nível final de validação antes do go-live: o software é avaliado pelo usuário final ou pelo representante do negócio para verificar se atende ao que foi solicitado. É o momento em que "quem pediu" confirma que "o que foi entregue" está correto. O UAT usa critérios de aceitação definidos pelo negócio, não pelo time técnico.

## Quando usar

- Quando uma entrega precisa ser aprovada pelo cliente ou stakeholder antes de ir para produção
- Quando quer estruturar um processo de homologação formal com o usuário final
- Quando quer criar cenários de aceitação em formato Given-When-Then (BDD)
- Quando quer garantir que os critérios de aceitação definidos estão sendo atendidos
- Quando precisa de evidência formal de aprovação da entrega

## Quando NÃO usar

- Para validação técnica sem envolvimento do usuário → use `teste-de-sistema`
- Para avaliar apenas experiência e facilidade de uso → use `teste-de-usabilidade`
- Como substituto para testes técnicos — o UAT complementa, não substitui

## Como funciona — Processo Passo a Passo

**Passo 1: Levantar critérios de aceitação**
Quais são os critérios que o usuário/negócio definiu para aceitar esta entrega? Se não existem formalmente, facilite a criação usando o formato Given-When-Then:
> *"Dado [contexto inicial], Quando [ação do usuário], Então [resultado esperado]."*

**Passo 2: Validar os critérios**
Cada critério é mensurável e verificável por um usuário não-técnico? Se não, refine. Um bom critério: "Dado que estou logado, Quando clico em Exportar, Então recebo um arquivo CSV com os dados do relatório em menos de 30 segundos."

**Passo 3: Preparar o ambiente**
Ambiente estável com dados representativos (não dados reais de produção). Guia de acesso simples para o usuário testador. Template de feedback simplificado (não use jargão técnico).

**Passo 4: Criar roteiro de UAT**
Escreva os cenários em linguagem de negócio — sem termos técnicos. Para cada cenário: contexto → passos do usuário → o que verificar → resultado esperado. Máximo de 10 a 15 cenários por sessão.

**Passo 5: Conduzir a sessão**
O usuário executa os cenários (com ou sem facilitador presente). Colete feedback: funciona como esperado? É fácil de usar? Registre bugs encontrados e sugestões.

**Passo 6: Classificar o resultado**
- **Aceite:** todos os critérios de aceitação atendidos → pode ir para produção
- **Aceite condicional:** pequenos ajustes acordados → nova validação dos itens pendentes
- **Recusa:** critérios críticos não atendidos → nova rodada de desenvolvimento

**Passo 7: Documentar o aceite**
Registro formal (escrito) de aprovação ou lista de itens pendentes para aceite condicional.

## Critérios de Qualidade

- Cenários escritos em linguagem de negócio (sem jargão técnico)
- Critérios de aceitação mensuráveis e verificáveis por não-técnicos
- Há processo claro de aprovação, aceite condicional ou rejeição
- Feedback do usuário é coletado de forma estruturada
- O aceite é documentado formalmente

## Exemplo Conceitual

**Critério de aceitação:**
> "Dado que sou gerente de vendas e estou logado, Quando acesso 'Relatório Mensal' e clico em 'Gerar', Então o relatório é baixado em formato PDF com as vendas do mês atual, incluindo total por vendedor."

**Roteiro de UAT (linguagem de negócio):**

| Passo | O que fazer | O que verificar |
|-------|------------|-----------------|
| 1 | Faça login com seu usuário de gerente | A tela inicial carrega e exibe seu nome |
| 2 | Clique em "Relatórios" no menu lateral | A seção de relatórios abre |
| 3 | Clique em "Relatório Mensal" | A tela de geração de relatório aparece |
| 4 | Clique em "Gerar Relatório" | Um arquivo PDF é baixado automaticamente |
| 5 | Abra o PDF baixado | O PDF contém as vendas do mês atual com total por vendedor |

## Checklist de Conclusão

- [ ] Os critérios de aceitação foram definidos antes da sessão de UAT?
- [ ] Cada critério é verificável por um usuário não-técnico?
- [ ] O ambiente de teste tem dados representativos (não reais)?
- [ ] O roteiro usa linguagem de negócio (sem termos técnicos)?
- [ ] O resultado foi classificado: Aceite, Aceite condicional ou Recusa?
- [ ] O aceite (ou lista de pendências) foi documentado formalmente?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-sistema` | Nível anterior — validação técnica | Quando quer que o time técnico valide antes de enviar para o cliente |
| `teste-de-usabilidade` | Complementar — foco em experiência | Quando quer avaliar especificamente a facilidade de uso junto ao usuário |
