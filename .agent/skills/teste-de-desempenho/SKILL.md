---
name: teste-de-desempenho
description: >
  Guia o desenvolvedor na medição e validação de métricas de desempenho do sistema — tempo de
  resposta, throughput e uso de recursos em condições normais de uso. Use esta skill SEMPRE que o
  objetivo for medir quão rápido e eficiente o sistema é, estabelecer um baseline de performance
  ou identificar gargalos. Acione quando o usuário mencionar: "teste de desempenho", "performance
  testing", "performance test", "quão rápido está a API", "tempo de resposta", "medir throughput",
  "latência", "TPS", "transações por segundo", "baseline de performance", "benchmark", "o sistema
  está lento e quero medir", "quero definir SLAs de desempenho". Diferente do teste de carga (que
  aumenta o volume de usuários) e de estresse (que vai além dos limites), o desempenho mede em
  condições normais. Agnóstico de ferramenta e linguagem.
categoria_ibm: Testes Não-Funcionais
nivel_maturidade: Intermediário / Avançado
skills_relacionadas:
  - teste-de-carga
  - teste-de-estresse
---

# Teste de Desempenho

## O que é

O teste de desempenho mede o comportamento do sistema em termos de velocidade, capacidade de resposta e consumo de recursos em condições normais de uso. O objetivo é responder: "Quão rápido o sistema é?" — medindo tempos de resposta, taxas de transferência e uso de CPU/memória, para verificar se os requisitos de desempenho são atendidos.

## Quando usar

- Quando quer estabelecer um baseline de performance (para comparar futuras mudanças)
- Quando quer validar SLAs de tempo de resposta antes de um lançamento
- Quando o sistema está lento e quer identificar onde está o gargalo
- Quando quer medir o impacto de uma mudança no desempenho (comparação antes vs. depois)
- Antes de testes de carga e estresse (é o ponto de partida)

## Quando NÃO usar

- Para simular múltiplos usuários simultâneos → use `teste-de-carga`
- Para encontrar o ponto de colapso do sistema → use `teste-de-estresse`
- Para funcionalidade ou comportamento correto → use testes funcionais

## Como funciona — Processo Passo a Passo

**Passo 1: Definir métricas alvo**
Antes de qualquer execução, defina o que é "bom o suficiente":
- Tempo de resposta: < X ms para 95% das requisições (percentil p95)
- Throughput: pelo menos N requisições por segundo
- Taxa de erro: < Y% de requisições com falha
- Recursos: CPU < Z%, Memória < W MB durante uso normal

**Passo 2: Identificar os cenários a medir**
Quais endpoints ou fluxos são críticos para o desempenho? Priorize os mais usados e os mais lentos.

**Passo 3: Definir o perfil de carga do baseline**
Quantos usuários simultâneos é "normal" para o sistema? Qual o padrão de uso típico (tempo entre ações)?

**Passo 4: Executar com carga normal**
Execute com o volume de usuários típico. Colete durante pelo menos 5 a 10 minutos para estabilizar as métricas.

**Passo 5: Analisar por percentis**
Não use apenas a média — ela mascara outliers. Use:
- **p50:** mediana — metade das requisições são mais rápidas que isso
- **p95:** 95% das requisições são mais rápidas que isso (referência para SLA)
- **p99:** 99% das requisições — identifica os piores casos

**Passo 6: Identificar gargalos**
Onde está a lentidão? Banco de dados (queries lentas)? Rede? CPU? Código ineficiente? Analise os logs e monitore recursos durante a execução.

**Passo 7: Documentar o baseline**
Registre: cenário, volume de usuários, p50/p95/p99 de tempo de resposta, throughput, taxa de erro, uso de CPU/memória. Este baseline será o ponto de comparação para futuras mudanças.

## Critérios de Qualidade

- Métricas alvo definidas ANTES de executar os testes
- Análise usa percentis (p50, p95, p99) — não apenas média
- Baseline documentado para comparação futura
- Gargalos identificados com evidências (não apenas suposições)
- Testes executados em ambiente representativo do de produção

## Exemplo Conceitual

**Métricas alvo definidas para uma API de busca de produtos:**
- p95 de tempo de resposta: < 200ms
- Throughput mínimo: 500 requisições/segundo
- Taxa de erro: < 0.1%

**Resultado do baseline (100 usuários simultâneos, 10 minutos):**

| Métrica | Alvo | Resultado | Status |
|---------|------|-----------|--------|
| p50 (mediana) | — | 45ms | ✅ |
| p95 | < 200ms | 180ms | ✅ |
| p99 | — | 450ms | ⚠️ (investigar) |
| Throughput | ≥ 500 RPS | 620 RPS | ✅ |
| Taxa de erro | < 0.1% | 0.05% | ✅ |
| CPU (pico) | < 70% | 62% | ✅ |

Observação: p99 acima do esperado — 1% das requisições estão demorando mais de 450ms. Investigar queries de banco que podem estar causando isso.

## Checklist de Conclusão

- [ ] Defini as métricas alvo (p95 de tempo de resposta, throughput, taxa de erro) ANTES de executar?
- [ ] Usei percentis (p50, p95, p99) na análise — não apenas a média?
- [ ] Executei em ambiente representativo do de produção?
- [ ] Executei por tempo suficiente para as métricas estabilizarem (mínimo 5 minutos)?
- [ ] Identifiquei onde estão os gargalos de desempenho?
- [ ] Documentei o baseline para comparações futuras?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-carga` | Próximo nível — volume crescente de usuários | Quando quer saber com quantos usuários o sistema começa a degradar |
| `teste-de-estresse` | Nível extremo — além dos limites | Quando quer encontrar o ponto de colapso do sistema |
