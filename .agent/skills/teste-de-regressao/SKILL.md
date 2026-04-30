---
name: teste-de-regressao
description: >
  Guia o desenvolvedor a garantir que funcionalidades existentes continuam funcionando corretamente
  após uma mudança de código. Use esta skill SEMPRE que o objetivo for verificar que uma alteração
  (nova feature, refatoração, correção de bug, atualização de dependência) não quebrou nada que
  funcionava antes. Acione quando o usuário mencionar: "teste de regressão", "regression testing",
  "quero garantir que não quebrei nada", "fiz uma mudança e quero verificar o impacto", "validar
  depois de um merge ou PR", "o que testar antes de um release", "minha refatoração pode ter
  quebrado algo", "validar que o código antigo ainda funciona". Diferente da sanidade (que testa
  uma funcionalidade específica) e da fumaça (que verifica só o básico do sistema), a regressão
  cobre todas as funcionalidades afetadas pela mudança. Funciona em qualquer linguagem.
categoria_ibm: Testes Funcionais de Método
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-de-fumaca
  - teste-de-sanidade
  - teste-de-caixa-branca
---

# Teste de Regressão

## O que é

O teste de regressão é executado após qualquer mudança no software para garantir que o que funcionava antes continua funcionando. "Regredir" significa voltar atrás — o risco é que uma mudança, mesmo bem-intencionada, introduza defeitos em funcionalidades que estavam corretas. A regressão é a proteção contra esse risco.

## Quando usar

- Após qualquer mudança de código: nova funcionalidade, correção de bug, refatoração
- Antes de merges ou pull requests em branchs principais
- Antes de cada release ou deploy para produção
- Após atualização de dependências ou bibliotecas
- Quando uma mudança em um módulo pode ter impacto em outros que dependem dele
- Periodicamente durante ciclos longos de desenvolvimento

## Quando NÃO usar

- Para validar apenas uma funcionalidade específica após mudança local → use `teste-de-sanidade`
- Para verificar se o sistema básico está de pé → use `teste-de-fumaca`
- Para testar funcionalidade completamente nova (sem histórico) → use caixa-preta ou caixa-branca

## Como funciona — Processo Passo a Passo

**Passo 1: Identificar o impacto da mudança**
O que foi alterado? (arquivo, módulo, serviço, dependência). Quais funcionalidades dependem do que foi alterado? Mapeie: o que chama o código modificado, o que é chamado por ele.

**Passo 2: Classificar o escopo da regressão**
- **Alta prioridade:** funcionalidades diretamente afetadas pela mudança
- **Média prioridade:** funcionalidades que dependem das afetadas (dependências indiretas)
- **Baixa prioridade:** funcionalidades sem relação aparente (smoke test suficiente)

**Passo 3: Definir estratégia**
- **Regressão seletiva:** apenas as funcionalidades afetadas (mais rápida, menor cobertura)
- **Regressão completa:** todas as funcionalidades do sistema (mais lenta, maior segurança)
- Use regressão completa antes de releases maiores; seletiva em deploys rotineiros

**Passo 4: Executar por prioridade**
Execute os testes de alta prioridade primeiro. Se passarem, execute a média. Se passarem, execute o smoke test nas demais. Pare e reporte se qualquer nível falhar.

**Passo 5: Analisar as falhas**
Para cada teste que falhou: o comportamento mudou intencionalmente (atualizar o teste) ou é um bug introduzido pela mudança (reportar e corrigir)?

**Passo 6: Atualizar a suíte**
Se a mudança altera o comportamento esperado de uma funcionalidade, atualize os testes correspondentes. Se bugs foram descobertos, crie novos casos de teste para os cenários encontrados.

## Critérios de Qualidade

- O escopo da regressão é definido com base no impacto da mudança (não "testar tudo sempre")
- Testes são executados em ordem de prioridade de impacto
- Falhas são classificadas: comportamento intencional vs. bug introduzido
- A suíte de regressão é atualizada quando o comportamento muda intencionalmente
- Novos casos de teste são criados para bugs encontrados durante a regressão

## Exemplo Conceitual

**Cenário:** Refatoração da função de cálculo de frete de um sistema de e-commerce.

Análise de impacto:
- **Alta prioridade:** cálculo de frete em si, exibição do frete no carrinho, finalização de pedido com frete
- **Média prioridade:** desconto de frete grátis, estimativa de frete na página do produto, relatórios de pedidos
- **Baixa prioridade:** cadastro de usuário, catálogo de produtos, área de login

Execução:
1. Rodar testes de alta prioridade → todos passaram ✅
2. Rodar testes de média prioridade → falha na estimativa de frete na página do produto ⚠️
3. Investigar: a refatoração mudou o arredondamento do valor — comportamento foi alterado intencionalmente?

## Checklist de Conclusão

- [ ] Identifiquei exatamente o que foi alterado (arquivo/módulo/serviço)?
- [ ] Mapeei as funcionalidades diretamente e indiretamente afetadas?
- [ ] Classifiquei o escopo em alta, média e baixa prioridade?
- [ ] Executei os testes na ordem de prioridade?
- [ ] Classifiquei cada falha: mudança intencional ou bug?
- [ ] Atualizei testes desatualizados pela mudança intencional de comportamento?
- [ ] Criei novos casos de teste para bugs descobertos durante a regressão?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-fumaca` | Subconjunto — verifica só o básico | Quando quer apenas confirmar que o sistema está de pé |
| `teste-de-sanidade` | Subconjunto — verifica uma funcionalidade | Quando quer validar apenas a feature tocada pela mudança |
| `teste-de-caixa-branca` | Complementar — analisa cobertura interna | Quando quer garantir que a mudança não reduziu a cobertura de código |
