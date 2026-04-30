---
name: teste-de-sistema
description: >
  Guia o desenvolvedor na validação do sistema completo como uma unidade, verificando que todos os
  componentes integrados se comportam corretamente em conjunto e que os requisitos do sistema são
  atendidos de ponta a ponta. Use esta skill SEMPRE que o objetivo for testar fluxos completos do
  usuário em um ambiente representativo do de produção. Acione quando o usuário mencionar: "teste
  de sistema", "system testing", "teste end-to-end", "testar o sistema completo", "testar de ponta
  a ponta", "verificar se o sistema atende os requisitos", "testar o fluxo completo de uma
  funcionalidade", "antes de entregar para o cliente quero testar por completo", "validar o sistema
  em staging". Diferente de integração (módulos específicos) e UAT (validação com o cliente), o
  teste de sistema é feito pelo time técnico no sistema completo. Agnóstico de linguagem e stack.
categoria_ibm: Testes por Nível
nivel_maturidade: Intermediário / Avançado
skills_relacionadas:
  - teste-de-integracao
  - teste-de-aceitacao-do-usuario
  - teste-de-fumaca
---

# Teste de Sistema

## O que é

O teste de sistema valida o software completo como uma unidade — todos os módulos integrados, em um ambiente representativo do de produção. O objetivo é confirmar que o sistema atende aos requisitos definidos, que os fluxos de ponta a ponta funcionam e que o comportamento sob condições reais está correto. É o penúltimo nível antes do UAT com o cliente.

## Quando usar

- Quando todos os módulos passaram nos testes de integração e quer validar o todo
- Antes de entregar o sistema para homologação com o cliente (pré-UAT)
- Quando quer validar fluxos completos do usuário no ambiente de staging
- Quando quer confirmar que os requisitos funcionais e não-funcionais básicos são atendidos
- Quando quer identificar problemas que só aparecem com o sistema completo (não em módulos isolados)

## Quando NÃO usar

- Para testar comunicação entre módulos específicos → use `teste-de-integracao`
- Para validação com o usuário/negócio → use `teste-de-aceitacao-do-usuario`
- Para verificar se o build básico subiu → use `teste-de-fumaca`
- Em ambiente de produção — o teste de sistema NUNCA deve ser executado em produção

## Como funciona — Processo Passo a Passo

**Passo 1: Definir escopo**
Quais funcionalidades/fluxos serão testados? Em qual ambiente? (staging, pré-produção — nunca produção). Quais requisitos funcionais precisam ser validados?

**Passo 2: Mapear jornadas do usuário (User Journeys)**
Identifique os principais caminhos que um usuário real percorreria. Priorize: fluxos de negócio principais > fluxos secundários > casos de borda. Exemplo: "usuário se cadastra → confirma e-mail → faz login → realiza a ação principal → encerra sessão."

**Passo 3: Preparar dados e ambiente**
Dados de teste realistas (sem dados reais de produção). Sistema completo ativo (banco, serviços externos, integrações). Condições iniciais definidas e documentadas.

**Passo 4: Executar casos de sistema**
Para cada jornada: execute do início ao fim. Verifique comportamento funcional (resultado correto?) e não-funcional básico (está dentro do tempo aceitável?).

**Passo 5: Cenários negativos**
O que acontece quando o usuário faz algo errado no meio do fluxo? O sistema recupera graciosamente? Mensagens de erro são claras?

**Passo 6: Relatório**
Para cada jornada: Passou / Falhou / Bloqueado. Para cada bug: passo a passo de reprodução, comportamento esperado vs. real. Percentual de requisitos validados.

## Critérios de Qualidade

- Cada requisito funcional principal tem pelo menos um caso de teste de sistema
- Fluxos testados de ponta a ponta (não apenas partes)
- Ambiente representativo do de produção
- Testes incluem verificação funcional e não-funcional básica
- Bugs documentados com steps de reprodução completos

## Exemplo Conceitual

**Jornada principal de um sistema de agendamento:**

```
1. Usuário acessa o sistema → carrega em < 2 segundos
2. Faz login com credenciais válidas → autenticado com sucesso
3. Visualiza agenda disponível → slots disponíveis listados
4. Seleciona data e horário → confirmação solicitada
5. Confirma o agendamento → agendamento criado, e-mail de confirmação enviado
6. Verifica "Meus agendamentos" → novo agendamento aparece na lista
7. Cancela o agendamento → slot liberado, e-mail de cancelamento enviado
```

Cenário negativo: no passo 4, o horário é ocupado por outro usuário simultaneamente → sistema informa que o slot não está mais disponível, sem criar agendamento duplicado.

## Checklist de Conclusão

- [ ] Defini as jornadas do usuário a testar (não módulos isolados)?
- [ ] Estou testando em ambiente representativo (staging, não produção)?
- [ ] Cada requisito funcional principal tem pelo menos um caso de teste?
- [ ] Incluí cenários negativos (usuário fazendo algo errado no meio do fluxo)?
- [ ] Documentei bugs com steps completos de reprodução?
- [ ] Produzi relatório com status de cada jornada (Passou/Falhou/Bloqueado)?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-integracao` | Nível anterior — módulos integrados | Quando quer testar a comunicação entre módulos específicos antes do sistema todo |
| `teste-de-aceitacao-do-usuario` | Nível seguinte — com o cliente | Quando quer que o usuário/negócio valide o sistema |
| `teste-de-fumaca` | Subconjunto — verificação básica | Quando quer apenas confirmar que o build está de pé, não o sistema completo |
