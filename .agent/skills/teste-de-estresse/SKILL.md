---
name: teste-de-estresse
description: >
  Guia o desenvolvedor a identificar o ponto de colapso do sistema, testando-o além de seus
  limites operacionais definidos para verificar como ele falha e se consegue se recuperar. Use
  esta skill SEMPRE que o objetivo for encontrar o limite máximo do sistema, verificar se a falha
  é graceful ou abrupta, ou realizar soak testing (carga sustentada por longos períodos). Acione
  quando o usuário mencionar: "teste de estresse", "stress testing", "stress test", "quero saber
  o limite do sistema", "ponto de ruptura", "o que acontece quando o sistema colapsa", "testar
  além da capacidade", "soak testing", "durabilidade do sistema", "o sistema aguenta horas sob
  carga?". Diferente do teste de carga (que valida dentro dos limites planejados), o estresse
  vai propositalmente além deles. Requer ambiente isolado e pré-requisito de baseline de carga.
categoria_ibm: Testes Não-Funcionais
nivel_maturidade: Avançado
skills_relacionadas:
  - teste-de-carga
  - teste-de-recuperacao
---

# Teste de Estresse

## O que é

O teste de estresse empurra o sistema além de seus limites definidos para identificar: qual é o ponto de colapso, como o sistema falha (graciosamente ou abruptamente) e se ele consegue se recuperar quando a pressão diminui. É uma análise de resiliência extrema — diferente do teste de carga, que valida dentro da capacidade planejada.

## Quando usar

- Quando quer saber o limite máximo real do sistema (não o limite planejado)
- Quando quer verificar se a falha é controlada (mensagem de erro clara) ou abrupta (crash)
- Quando quer testar durabilidade sob carga alta sustentada por horas (soak testing)
- Quando quer simular situações de recursos reduzidos (CPU limitada, memória limitada)
- Quando quer validar que o sistema se recupera após sobrecarga

## Quando NÃO usar

- Como primeiro teste de performance → faça `teste-de-desempenho` e `teste-de-carga` antes
- Para validar a capacidade dentro do planejado → use `teste-de-carga`
- Em ambiente de produção (nunca)

## Como funciona — Processo Passo a Passo

**Passo 1: Estabelecer baseline**
Tenha em mãos os resultados do teste de carga. Saiba: onde o sistema funciona bem, onde começa a degradar, qual é a capacidade máxima planejada.

**Passo 2: Definir o plano de estresse**
Escolha a abordagem:
- **Volume extremo:** aumentar usuários/requisições muito além do máximo planejado até o sistema colapsar
- **Soak test:** manter carga alta (80-90% da capacidade) por horas ou dias — detecta vazamentos de memória e degradação progressiva
- **Recursos reduzidos:** reduzir CPU ou memória disponível e verificar comportamento

**Passo 3: Executar gradualmente**
Mesmo no estresse, aumente a pressão gradualmente. Registre o comportamento em cada nível.

**Passo 4: Identificar o ponto de colapso**
Em qual carga o sistema colapsa? Como ele falha?
- Falha graceful: retorna erros com mensagens claras (503, timeout com mensagem amigável)
- Falha abrupta: crash, travamento, corrupção de dados — isso é crítico

**Passo 5: Reduzir a carga e observar a recuperação**
Após o colapso: o sistema se recupera automaticamente? Os dados permanecem íntegros? Quanto tempo leva para voltar ao normal?

**Passo 6: Documentar o ponto de ruptura**
Volume de usuários/RPS onde colapsou, tipo de falha, comportamento de recuperação, dados afetados.

## Critérios de Qualidade

- Parte de resultados de testes de carga (não começa do zero)
- Abordagem de estresse definida antes de executar (volume, soak, recursos reduzidos)
- Tipo de falha identificado (graceful vs. abrupta)
- Recuperação verificada após a redução de carga
- Ponto de ruptura documentado com evidências

## Exemplo Conceitual

**Continuando o exemplo do sistema de e-commerce (carga máxima: 500 usuários):**

| Usuários | Comportamento | Tipo de falha |
|----------|--------------|--------------|
| 500 | Funciona — p95 = 480ms | — |
| 700 | Degradação severa — p95 = 2.1s, erros = 3% | Graceful (503) |
| 900 | Sistema retorna 503 para 40% das requisições | Graceful — correto |
| 1200 | Banco de dados trava por esgotamento do pool | Abrupta — necessita correção |

Após reduzir para 0: sistema se recupera em 45 segundos. Dados íntegros.

**Soak test (70% da carga por 4 horas):**
- Horas 1-2: estável ✅
- Hora 3: memória subindo progressivamente ⚠️
- Hora 4: restart automático por OOM (Out of Memory) — vazamento de memória identificado 🚨

## Checklist de Conclusão

- [ ] Tenho resultados de testes de carga como baseline antes de começar?
- [ ] Defini qual abordagem de estresse usar (volume extremo, soak test, recursos reduzidos)?
- [ ] Documentei o ponto de colapso (carga e tipo de falha)?
- [ ] Identifiquei se a falha foi graceful (controlada) ou abrupta (crash)?
- [ ] Verifiquei a recuperação: o sistema volta automaticamente? Os dados estão íntegros?
- [ ] Executei em ambiente isolado (nunca em produção)?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-carga` | Pré-requisito — valida dentro dos limites | Execute antes do estresse para ter um baseline claro |
| `teste-de-recuperacao` | Complementar — foco na recuperação após falhas | Quando quer investigar profundamente o comportamento pós-falha |
