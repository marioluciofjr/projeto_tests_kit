---
name: teste-de-recuperacao
description: >
  Guia o desenvolvedor a validar como o sistema se comporta e se recupera diante de falhas —
  crashes, perda de conectividade, indisponibilidade de serviços dependentes, corrupção de dados
  ou interrupção abrupta. Use esta skill SEMPRE que o objetivo for verificar a resiliência e
  tolerância a falhas do sistema. Acione quando o usuário mencionar: "teste de recuperação",
  "recovery testing", "chaos engineering básico", "o que acontece quando o banco cai", "e se o
  sistema falhar no meio de uma transação", "resiliência do sistema", "fallback", "circuit breaker",
  "testar tolerância a falhas", "o sistema precisa se recuperar de quedas", "o que acontece em
  caso de falha". Este é um teste avançado que NUNCA deve ser executado em produção. Requer
  ambiente isolado com capacidade de restauração rápida. Agnóstico de linguagem.
categoria_ibm: Testes de Confiabilidade
nivel_maturidade: Avançado
skills_relacionadas:
  - teste-de-sistema
  - teste-de-estresse
---

# Teste de Recuperação

## O que é

O teste de recuperação verifica como o sistema se comporta diante de falhas e se ele consegue se recuperar dentro de um tempo aceitável. O objetivo é responder: quando algo inevitavelmente der errado, o sistema falha de forma controlada (gracefully) e volta ao normal automaticamente? Os dados ficam íntegros após a falha?

## Quando usar

- Quando o sistema tem requisitos de alta disponibilidade ou SLAs de uptime
- Quando quer validar estratégias de fallback e circuit breaker
- Quando quer verificar o comportamento com dependências indisponíveis
- Quando precisa definir e validar RTO (Recovery Time Objective) e RPO (Recovery Point Objective)
- Antes de systems críticos irem para produção (financeiro, saúde, infraestrutura)

## Quando NÃO usar

- Em ambiente de produção (nunca — risco de impacto real aos usuários)
- Sem um ambiente isolado e restaurável disponível
- Como substituto para tratamento de erros no código (é um complemento, não um substituto)

## Como funciona — Processo Passo a Passo

**Passo 1: Mapear pontos de falha**
Quais serviços o sistema depende? (banco de dados, APIs externas, filas, cache, armazenamento). Quais são os RTO e RPO definidos? Se não existirem, defina-os antes de continuar.

**Passo 2: Categorizar os cenários de falha**
- Falha de infraestrutura: servidor indisponível, rede cai, disco cheio
- Falha de serviço dependente: banco fora do ar, API externa indisponível
- Falha de dados: transação incompleta, dados corrompidos
- Falha de aplicação: erro não tratado, deadlock, vazamento de memória

**Passo 3: Para cada cenário — definir o teste**
Como induzir a falha? O que o sistema deve fazer? Como verificar a recuperação?

**Passo 4: Documentar estado antes da falha**
Registre o estado do sistema antes de injetar a falha — dados existentes, usuários ativos, transações em aberto.

**Passo 5: Injetar a falha**
Em ambiente isolado. Registre o comportamento: o sistema exibe mensagem clara? Mantém dados íntegros? Tenta reconectar automaticamente?

**Passo 6: Verificar recuperação**
Após resolver a falha: o sistema volta automaticamente? Os dados permanecem íntegros? O tempo de recuperação está dentro do RTO?

**Passo 7: Documentar**
Cenário → falha injetada → comportamento observado → tempo de recuperação → dados afetados.

## Critérios de Qualidade

- RTO e RPO estão definidos antes de executar os testes
- Pelo menos 3 categorias de falha diferentes são testadas
- Cada teste é executado em ambiente isolado (nunca produção)
- A integridade dos dados é verificada após a recuperação
- O comportamento de falha é documentado: graceful (controlado) vs. abrupto (crash)

## Exemplo Conceitual

**Cenário:** Indisponibilidade do banco de dados durante uma transação ativa.

| Fase | O que acontece | Comportamento esperado |
|------|---------------|----------------------|
| Banco indisponível | Usuário tenta salvar um pedido | Exibe mensagem: "Sistema temporariamente indisponível. Tente novamente em alguns minutos." |
| Banco indisponível | Transação em andamento é interrompida | Transação é revertida (rollback) — nenhum dado parcial é salvo |
| Banco volta online | Sistema detecta a reconexão | Reconecta automaticamente sem necessidade de reiniciar |
| Após recuperação | Usuário tenta novamente | Pedido é salvo com sucesso — sem dados corrompidos da falha anterior |

## Checklist de Conclusão

- [ ] Defini RTO e RPO antes de começar?
- [ ] Listei todos os serviços dos quais o sistema depende?
- [ ] Cobri pelo menos 3 categorias de falha?
- [ ] Executei APENAS em ambiente isolado (nunca em produção)?
- [ ] Verifiquei a integridade dos dados após a recuperação?
- [ ] Documentei o comportamento de falha (graceful vs. abrupto) e o tempo de recuperação?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-sistema` | Pré-requisito — sistema funciona em condições normais | Antes de testar falhas, garanta que o sistema funciona normalmente |
| `teste-de-estresse` | Complementar — identifica o ponto de colapso | Quando quer empurrar o sistema além dos limites antes de testar recuperação |
