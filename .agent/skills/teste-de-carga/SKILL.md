---
name: teste-de-carga
description: >
  Guia o desenvolvedor a validar o comportamento do sistema sob volumes crescentes de usuários e
  requisições, identificando o ponto de degradação de desempenho e a capacidade máxima suportada.
  Use esta skill SEMPRE que o objetivo for responder "o sistema aguenta N usuários simultâneos?"
  ou "a partir de quantos usuários o desempenho degrada?". Acione quando o usuário mencionar:
  "teste de carga", "load testing", "carga de usuários", "o sistema aguenta N usuários simultâneos",
  "quero testar com X requisições por segundo", "antes do lançamento testar com a carga esperada",
  "quero saber quando o sistema começa a degradar", "escalar usuários gradualmente e ver o
  comportamento", "carga de pico". Diferente do teste de desempenho (condições normais) e de
  estresse (além dos limites), a carga vai do normal até o máximo planejado. Requer ambiente
  representativo.
categoria_ibm: Testes Não-Funcionais
nivel_maturidade: Avançado
skills_relacionadas:
  - teste-de-desempenho
  - teste-de-estresse
---

# Teste de Carga

## O que é

O teste de carga verifica o comportamento do sistema quando submetido a volumes crescentes de usuários e requisições, até atingir a carga máxima esperada (e um pouco além, para ter margem de segurança). O objetivo é identificar: a partir de que volume o desempenho começa a degradar, qual é a capacidade máxima do sistema e onde estão os gargalos sob pressão.

## Quando usar

- Antes de lançamentos ou grandes eventos que trarão tráfego elevado
- Quando quer validar se a infraestrutura atual suporta a demanda esperada
- Quando quer encontrar o ponto exato onde o desempenho começa a piorar
- Quando quer validar estratégias de escalonamento automático (auto-scaling)
- Como pré-requisito antes de testes de estresse

## Quando NÃO usar

- Para medir desempenho em condições normais → use `teste-de-desempenho` primeiro
- Para encontrar o ponto de colapso absoluto → use `teste-de-estresse`
- Em ambiente de produção (nunca — use ambiente de staging representativo)

## Como funciona — Processo Passo a Passo

**Passo 1: Definir perfis de carga**
- Carga normal: N usuários (uso diário médio)
- Carga de pico esperada: M usuários (Black Friday, lançamento, horário de pico)
- Carga de segurança: 20-30% acima do pico esperado (margem de conforto)

**Passo 2: Definir critérios de aceitação sob carga**
O que é aceitável com a carga máxima? Ex: p95 < 500ms, taxa de erro < 1%, CPU < 80%.

**Passo 3: Estratégia de ramp-up**
Não comece com carga total imediatamente — suba gradualmente:
- Warm-up: 10-20% da carga esperada por 2 minutos
- Ramp-up: aumentar gradualmente até 100% da carga em 5-10 minutos
- Sustentação: manter a carga máxima por 15 a 30 minutos
- Cool-down: reduzir gradualmente

**Passo 4: Monitorar durante a execução**
Colete em tempo real: tempo de resposta por percentil, taxa de erro, CPU e memória do servidor, conexões ativas do banco de dados, throughput (requisições por segundo).

**Passo 5: Identificar o ponto de degradação**
Em qual nível de carga o tempo de resposta começa a aumentar? Em qual nível a taxa de erro começa a subir? Esse é o "knee point" — o ponto de inflexão da curva de capacidade.

**Passo 6: Analisar e reportar**
Gráfico de tempo de resposta × volume de usuários. Identificação do gargalo (banco? CPU? Rede? Pool de conexões?). Recomendação de capacidade necessária.

## Critérios de Qualidade

- Perfis de carga definidos (normal, pico, segurança) antes de executar
- Estratégia de ramp-up usada (não começa com carga total imediatamente)
- Fase de sustentação presente (mínimo 15 minutos em carga máxima)
- Monitoramento de recursos do servidor além de tempo de resposta
- Ponto de degradação identificado e documentado

## Exemplo Conceitual

**Sistema de e-commerce com pico esperado de 500 usuários simultâneos:**

| Fase | Usuários | Duração | Observação |
|------|----------|---------|------------|
| Warm-up | 50 | 2 min | Sistema estável, p95 = 120ms |
| Ramp-up | 50 → 500 | 8 min | Degradação começa em ~350 usuários |
| Sustentação | 500 | 20 min | p95 = 480ms, taxa de erro = 0.3% |
| Cool-down | 500 → 0 | 5 min | Sistema se recupera completamente |

Conclusão: o sistema aguenta 500 usuários dentro dos critérios de aceite, mas o ponto de degradação em 350 usuários indica que ajustes no pool de conexões do banco podem ampliar essa margem.

## Checklist de Conclusão

- [ ] Defini os perfis de carga (normal, pico, segurança) antes de executar?
- [ ] Usei estratégia de ramp-up (não comecei com carga total)?
- [ ] Mantive a carga máxima por pelo menos 15 minutos (fase de sustentação)?
- [ ] Monitorei recursos do servidor (CPU, memória, banco) além do tempo de resposta?
- [ ] Identifiquei o ponto de degradação de desempenho?
- [ ] Documentei o gargalo e recomendações de capacidade?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-desempenho` | Pré-requisito — baseline em condições normais | Sempre execute antes do teste de carga para ter um ponto de referência |
| `teste-de-estresse` | Próximo nível — além do limite | Quando quer saber o que acontece quando o sistema colapsa, não apenas degrada |
