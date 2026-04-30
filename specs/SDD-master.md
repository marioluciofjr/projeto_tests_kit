# SDD Master — tests-kit

> **Versão:** 1.0 | **Data:** 2026-04-30
> **Metodologia:** Spec-Driven Development (SDD) — RFC Pragmático + LLM-First
> **Referência:** PRD v1.0 (`_reversa_sdd/PRD.md`) + IBM Software Testing Reference

---

## Propósito deste documento

Este documento define o **contrato arquitetural** que todas as skills do tests-kit devem seguir. Ele é a fonte da verdade para:

1. O **template padrão** de cada `SKILL.md`
2. As **fronteiras semânticas** entre skills similares
3. Os **critérios de aceite** que validam se uma skill está pronta
4. A **taxonomia IBM** que mapeia cada skill a uma categoria canônica

---

## Template Padrão de SKILL.md

Toda skill do tests-kit DEVE seguir esta estrutura exata. Desvios requerem justificativa documentada.

```markdown
---
name: [nome-da-skill-em-kebab-case]
description: [Descrição otimizada para triggering por LLMs — inclui: o que é, quando acionar, gatilhos verbais explícitos. Mínimo 3 frases. Máximo 8.]
categoria_ibm: [Técnica de Projeto | Funcional | Nível | Não-Funcional | Confiabilidade]
nivel_maturidade: [Iniciante | Intermediário | Avançado | Todos os níveis]
skills_relacionadas: [lista de slugs]
---

# [Nome Legível da Skill]

## O que é

[Definição em 2-4 frases. Linguagem acessível. Sem jargão desnecessário. Deve ser compreensível por um dev com 6 meses de experiência.]

## Quando usar

[Lista com 4-7 contextos específicos que devem acionar esta skill. Inclua situações reais do dia-a-dia do desenvolvedor.]

## Quando NÃO usar

[Lista com 3-5 anti-padrões. Inclua confusões comuns com skills similares.]

## Como funciona — Processo Passo a Passo

[Numerado. Agnóstico de linguagem. Cada passo deve ser acionável. Mínimo 4 passos, máximo 10.]

## Critérios de Qualidade

[O que diferencia um bom teste deste tipo de um ruim. Lista com 5-8 critérios mensuráveis.]

## Exemplo Conceitual

[Cenário real descrito em linguagem natural + pseudocódigo ou tabela. NÃO usar linguagem específica no bloco de código principal.]

## Checklist de Conclusão

[Lista de verificação antes de marcar os testes como concluídos. Mínimo 5 itens. Cada item é uma pergunta de sim/não.]

## Skills Relacionadas

[Tabela com: skill | relação | quando preferir aquela ao invés desta]
```

---

## Contrato de Triggering (Frontmatter Description)

A `description` de cada skill é o campo mais crítico — é o que determina se o LLM vai ativar a skill corretamente. Regras obrigatórias:

| Regra | Critério |
|-------|---------|
| **Verbo de ação** | Começa com verbo no infinitivo ("Guia...", "Orienta...", "Conduz...") |
| **Contextos de acionamento** | Lista pelo menos 3 frases/situações que devem acionar a skill |
| **Diferenciação** | Menciona explicitamente o que a skill NÃO é (para evitar conflito com skills similares) |
| **Nível** | Indica se é para iniciantes, experts ou todos |
| **Tamanho** | Entre 80 e 200 palavras |

---

## Fronteiras Semânticas entre Skills Similares

Um dos maiores riscos do tests-kit é a sobreposição entre skills similares. Estas fronteiras devem ser claras:

### Fumaca vs. Sanidade vs. Regressão

| Skill | Escopo | Gatilho Principal |
|-------|--------|-------------------|
| **Fumaça** | Sistema inteiro, superficial | "O build subiu?" / "O sistema responde?" |
| **Sanidade** | Uma funcionalidade, após mudança local | "Essa feature específica ainda funciona?" |
| **Regressão** | Funcionalidades existentes, após qualquer mudança | "Alguma coisa quebrou com minha mudança?" |

### Carga vs. Estresse vs. Desempenho

| Skill | Escopo | Gatilho Principal |
|-------|--------|-------------------|
| **Desempenho** | Tempo de resposta e throughput em condições normais | "Quão rápido é o sistema?" |
| **Carga** | Comportamento com volume crescente de usuários | "O sistema aguenta N usuários simultâneos?" |
| **Estresse** | Comportamento além dos limites definidos | "Qual é o ponto de colapso do sistema?" |

### Exploratório vs. Ad-hoc

| Skill | Escopo | Gatilho Principal |
|-------|--------|-------------------|
| **Exploratório** | Estruturado com sessão, charter e heurísticas | "Quero explorar sistematicamente esta funcionalidade" |
| **Ad-hoc** | Completamente livre, sem roteiro | "Quero simplesmente testar sem planejamento" |

### Caixa Branca vs. Caixa Preta

| Skill | Escopo | Gatilho Principal |
|-------|--------|-------------------|
| **Caixa Branca** | Acesso ao código fonte | "Quero verificar cobertura de código" |
| **Caixa Preta** | Sem acesso ao código, testa comportamento | "Quero testar como usuário/consumidor da API" |

### Integração vs. Sistema

| Skill | Escopo | Gatilho Principal |
|-------|--------|-------------------|
| **Integração** | Comunicação entre 2+ módulos/serviços | "Esses dois módulos conversam corretamente?" |
| **Sistema** | Sistema completo como uma unidade | "O sistema inteiro funciona de ponta a ponta?" |

---

## Taxonomia IBM — Mapeamento Completo

| Categoria IBM | Skills | IDs PRD |
|--------------|--------|---------|
| **Técnicas de Projeto de Teste** | Caixa Branca, Caixa Preta | RF-08, RF-09 |
| **Testes Funcionais de Método** | Ad-hoc, Exploratório, API, Regressão, Sanidade, Fumaça | RF-10 a RF-15 |
| **Testes por Nível (Pirâmide)** | Integração, Sistema, UAT | RF-16 a RF-18 |
| **Testes Não-Funcionais** | Desempenho, Carga, Estresse, Segurança, Usabilidade, Compatibilidade | RF-20 a RF-25 |
| **Testes de Confiabilidade** | Recuperação | RF-19 |

---

## Critérios de Aceite de Cada SKILL.md

Uma skill está PRONTA quando atende **todos** os critérios abaixo:

| Critério | Verificação |
|---------|------------|
| CA-01 | Frontmatter YAML completo com todos os campos obrigatórios |
| CA-02 | `description` entre 80-200 palavras com gatilhos explícitos |
| CA-03 | Seção "Quando NÃO usar" com pelo menos 3 itens e diferenciação de skills similares |
| CA-04 | Processo passo-a-passo com mínimo 4 e máximo 10 passos, todos agnósticos |
| CA-05 | Checklist de conclusão com mínimo 5 perguntas de sim/não |
| CA-06 | Exemplo conceitual que NÃO usa nenhuma linguagem específica no corpo principal |
| CA-07 | Tabela "Skills Relacionadas" preenchida |
| CA-08 | Revisão do revisor-gramatical aplicada |
| CA-09 | Auditoria skill-injection-auditor com resultado SEGURO |
| CA-10 | Referência à categoria IBM correspondente no frontmatter |

**Score mínimo para release:** 10/10 critérios atendidos.

---

## Contrato dos Agents (.md de Persona)

Os arquivos de agent são diferentes das skills. Eles definem uma **persona especializada** que o LLM deve assumir. Cada agent DEVE conter:

```markdown
# [Nome do Agente]

## Identidade

[Quem é este agente: especialidade, tom de voz, abordagem pedagógica]

## Especialidade Técnica

[Em quais tipos de teste este agente é especialista. Referência à categoria da pirâmide de testes.]

## Comportamento

[Como o agente age: proativo ou reativo, nível de detalhe, estilo de comunicação]

## Contexto de Ativação

[Em quais situações o usuário deve chamar este agente]

## Roteiro de Atendimento

[Passo a passo de como o agente conduz uma sessão de testes com o usuário]

## Skills que domina

[Lista das skills do kit que este agente conhece profundamente]

## O que o agente NÃO faz

[Limitações explícitas — o que está fora do escopo desta persona]
```

---

## Índice de Specs SDD

| Arquivo | Conteúdo |
|---------|---------|
| `SDD-master.md` | Este documento — template e contrato |
| `SDD-tecnicas.md` | Caixa Branca + Caixa Preta |
| `SDD-funcionais.md` | Ad-hoc, API, Exploratório, Regressão, Sanidade, Fumaça |
| `SDD-niveis.md` | Integração, Sistema, Aceitação do Usuário |
| `SDD-especializados.md` | Recuperação, Desempenho, Carga, Estresse, Segurança, Usabilidade, Compatibilidade |
| `SDD-agents.md` | 4 Agents de Persona |

---

## Score de Qualidade deste SDD Master

| Dimensão | Score | Status |
|----------|-------|--------|
| Completude | 30/30 | ✅ |
| Testabilidade | 25/25 | ✅ |
| Clareza | 20/20 | ✅ |
| Escopo | 15/15 | ✅ |
| Edge Cases | 10/10 | ✅ |
| **TOTAL** | **100/100** | ✅ PRONTO |
