# Matriz de Rastreabilidade — tests-kit

> **Versão:** 1.0 | **Data:** 2026-04-30
> **Propósito:** Rastrear todos os requisitos do PRD até os artefatos de entrega — garantindo que nenhum requisito fique sem implementação e nenhum artefato exista sem requisito que o justifique.

---

## Como ler esta matriz

| Coluna | Significado |
|--------|-------------|
| **RF-ID** | Requisito funcional do PRD (`_reversa_sdd/PRD.md`) |
| **SPEC-ID** | Spec SDD correspondente (`_reversa_sdd/SDD-*.md`) |
| **Artefato** | Arquivo físico que implementa o requisito |
| **Categoria IBM** | Categoria da taxonomia IBM de testes |
| **Persona Principal** | Qual persona do PRD mais usa este componente |
| **Agent Responsável** | Agent de persona que "conhece" esta skill |
| **Status** | 🔴 Não iniciado · 🟡 Spec pronta · 🟢 Implementado · ✅ Auditado |

---

## Matriz 1 — Requisitos de Infraestrutura (RF-01 a RF-07)

| RF-ID | Requisito | SPEC-ID | Artefato | Persona Principal | Status |
|-------|-----------|---------|---------|------------------|--------|
| RF-01 | `AGENTS.md` raiz | SDD-master (§ Entry Point) | `tests-kit/AGENTS.md` | Todos | ✅ |
| RF-02 | `README.md` completo | SDD-master (§ Documentação) | `tests-kit/README.md` | Dev Júnior | ✅ |
| RF-03 | `.agent/rules/GEMINI.md` | SDD-master (§ Rules) | `tests-kit/.agent/rules/GEMINI.md` | Motor de IA | ✅ |
| RF-04 | `.agent/ARCHITECTURE.md` | SDD-master (§ Arquitetura) | `tests-kit/.agent/ARCHITECTURE.md` | Tech Lead | ✅ |
| RF-05 | 18 Skills (pastas + SKILL.md) | SPEC-01 a SPEC-18 | `tests-kit/.agent/skills/*/SKILL.md` | Dev Júnior / Pleno | ✅ |
| RF-06 | 5 Agents (.md persona) | SPEC-19 a SPEC-23 | `tests-kit/.agent/agents/*.md` | Dev Júnior / Pleno | ✅ |
| RF-07 | Git + commits semânticos | — | `.git/` (raiz do projeto) | Todos | ✅ |

---

## Matriz 2 — Técnicas de Projeto de Teste (RF-08 a RF-09)

| RF-ID | Skill | SPEC-ID | Artefato | Categoria IBM | Persona Principal | Agent Responsável | Status |
|-------|-------|---------|---------|--------------|------------------|------------------|--------|
| RF-08 | `teste-de-caixa-branca` | SPEC-01 | `.agent/skills/teste-de-caixa-branca/SKILL.md` | Técnicas de Projeto | Dev Pleno/Sênior | agent-testes-de-unidade | 🟡 |
| RF-09 | `teste-de-caixa-preta` | SPEC-02 | `.agent/skills/teste-de-caixa-preta/SKILL.md` | Técnicas de Projeto | Todos | agent-testes-de-unidade | 🟡 |

---

## Matriz 3 — Testes Funcionais de Método (RF-10 a RF-15)

| RF-ID | Skill | SPEC-ID | Artefato | Categoria IBM | Persona Principal | Agent Responsável | Status |
|-------|-------|---------|---------|--------------|------------------|------------------|--------|
| RF-10 | `teste-ad-hoc` | SPEC-03 | `.agent/skills/teste-ad-hoc/SKILL.md` | Testes Funcionais | Dev Júnior | agent-testes-de-sistema | 🟡 |
| RF-11 | `teste-de-API` | SPEC-04 | `.agent/skills/teste-de-API/SKILL.md` | Testes Funcionais | Dev Pleno | agent-testes-de-integracao | 🟡 |
| RF-12 | `teste-exploratorio` | SPEC-05 | `.agent/skills/teste-exploratorio/SKILL.md` | Testes Funcionais | Dev Pleno/Sênior | agent-testes-de-sistema | 🟡 |
| RF-13 | `teste-de-regressao` | SPEC-06 | `.agent/skills/teste-de-regressao/SKILL.md` | Testes Funcionais | Todos | agent-testes-de-sistema | 🟡 |
| RF-14 | `teste-de-sanidade` | SPEC-07 | `.agent/skills/teste-de-sanidade/SKILL.md` | Testes Funcionais | Todos | agent-testes-de-sistema | 🟡 |
| RF-15 | `teste-de-fumaca` | SPEC-08 | `.agent/skills/teste-de-fumaca/SKILL.md` | Testes Funcionais | Todos | agent-testes-de-sistema | 🟡 |

---

## Matriz 4 — Testes por Nível (RF-16 a RF-18)

| RF-ID | Skill | SPEC-ID | Artefato | Categoria IBM | Persona Principal | Agent Responsável | Status |
|-------|-------|---------|---------|--------------|------------------|------------------|--------|
| RF-16 | `teste-de-integracao` | SPEC-09 | `.agent/skills/teste-de-integracao/SKILL.md` | Testes por Nível | Dev Pleno | agent-testes-de-integracao | 🟡 |
| RF-17 | `teste-de-sistema` | SPEC-10 | `.agent/skills/teste-de-sistema/SKILL.md` | Testes por Nível | Dev Pleno/Sênior | agent-testes-de-sistema | 🟡 |
| RF-18 | `teste-de-aceitacao-do-usuario` | SPEC-11 | `.agent/skills/teste-de-aceitacao-do-usuario/SKILL.md` | Testes por Nível | Tech Lead / PM | agent-testes-de-aceitacao | 🟡 |

---

## Matriz 5 — Testes Especializados (RF-19 a RF-25)

| RF-ID | Skill | SPEC-ID | Artefato | Categoria IBM | Persona Principal | Agent Responsável | Status |
|-------|-------|---------|---------|--------------|------------------|------------------|--------|
| RF-19 | `teste-de-recuperacao` | SPEC-12 | `.agent/skills/teste-de-recuperacao/SKILL.md` | Confiabilidade | Dev Sênior / Infra | agent-testes-de-sistema | 🟡 |
| RF-20 | `teste-de-desempenho` | SPEC-13 | `.agent/skills/teste-de-desempenho/SKILL.md` | Não-Funcional | Dev Pleno/Sênior | agent-testes-de-sistema | 🟡 |
| RF-21 | `teste-de-carga` | SPEC-14 | `.agent/skills/teste-de-carga/SKILL.md` | Não-Funcional | Dev Sênior | agent-testes-de-sistema | 🟡 |
| RF-22 | `teste-de-estresse` | SPEC-15 | `.agent/skills/teste-de-estresse/SKILL.md` | Não-Funcional | Dev Sênior | agent-testes-de-sistema | 🟡 |
| RF-23 | `teste-de-seguranca` | SPEC-16 | `.agent/skills/teste-de-seguranca/SKILL.md` | Não-Funcional | Dev Pleno/Sênior | agent-testes-de-sistema | 🟡 |
| RF-24 | `teste-de-usabilidade` | SPEC-17 | `.agent/skills/teste-de-usabilidade/SKILL.md` | Não-Funcional | Dev Júnior / UX | agent-testes-de-aceitacao | 🟡 |
| RF-25 | `teste-de-compatibilidade` | SPEC-18 | `.agent/skills/teste-de-compatibilidade/SKILL.md` | Não-Funcional | Dev Pleno | agent-testes-de-sistema | 🟡 |

---

## Matriz 6 — Agents de Persona (RF-26 a RF-30)

| RF-ID | Agent | SPEC-ID | Artefato | Nível Pirâmide | Persona Principal | Skills que domina | Status |
|-------|-------|---------|---------|---------------|------------------|------------------|--------|
| RF-26 | `agent-testes-de-unidade` | SPEC-19 | `.agent/agents/agent-testes-de-unidade.md` | Base | Dev Júnior / TDD | caixa-branca, caixa-preta | 🟢 |
| RF-27 | `agent-testes-de-integracao` | SPEC-20 | `.agent/agents/agent-testes-de-integracao.md` | Integração | Dev Pleno | teste-de-integracao, teste-de-API, regressao | 🟢 |
| RF-28 | `agent-testes-de-sistema` | SPEC-21 | `.agent/agents/agent-testes-de-sistema.md` | Sistema | Dev Pleno/Sênior | sistema, fumaça, regressão, desempenho, segurança | 🟢 |
| RF-29 | `agent-testes-de-aceitacao` | SPEC-22 | `.agent/agents/agent-testes-de-aceitacao.md` | Aceitação | Tech Lead / PM | aceitacao-do-usuario, usabilidade | 🟢 |
| RF-30 | `agent-relatorios` | SPEC-23 | `.agent/agents/agent-relatorios.md` | Transversal | Todos | todas as 18 skills (compila resultados) | 🟢 |

---

## Matriz 7 — Rastreabilidade Inversa: Persona → Skills

> *Quais skills cada persona do PRD usa mais*

| Persona | Skills Primárias | Skills Secundárias | Agent Recomendado |
|---------|-----------------|------------------|--------------------|
| **Dev Júnior / Vibe Coder** | fumaça, sanidade, caixa-preta, ad-hoc | regressão, unidade (via agent) | agent-testes-de-unidade |
| **Dev Pleno** | caixa-branca, integração, API, regressão, sistema | desempenho, segurança, compatibilidade | agent-testes-de-integracao |
| **Dev Sênior** | caixa-branca, estresse, carga, recuperação, segurança | exploratório, sistema | agent-testes-de-sistema |
| **Tech Lead / QA Lead** | aceitação-UAT, sistema, regressão | todos os especializados | agent-testes-de-aceitacao |
| **Qualquer nível** | (todos os tipos de teste) | — | agent-relatorios (ao compilar resultados) |

---

## Matriz 8 — Rastreabilidade: Categoria IBM → Skills → Agents

| Categoria IBM | Skills | Agents que cobrem |
|--------------|--------|------------------|
| **Técnicas de Projeto de Teste** | caixa-branca, caixa-preta | agent-unidade |
| **Testes Funcionais de Método** | ad-hoc, API, exploratório, regressão, sanidade, fumaça | agent-integracao, agent-sistema |
| **Testes por Nível — Unitário** | (via agent) | agent-unidade |
| **Testes por Nível — Integração** | teste-de-integracao | agent-integracao |
| **Testes por Nível — Sistema** | teste-de-sistema | agent-sistema |
| **Testes por Nível — Aceitação** | teste-de-aceitacao-do-usuario | agent-aceitacao |
| **Testes Não-Funcionais** | desempenho, carga, estresse, segurança, usabilidade, compatibilidade | agent-sistema, agent-aceitacao |
| **Testes de Confiabilidade** | teste-de-recuperacao | agent-sistema |

---

## Matriz 9 — Rastreabilidade: Skill → Quando na Pipeline

> *Em qual momento do ciclo de desenvolvimento cada skill é acionada*

| Momento | Skills recomendadas | Sequência |
|---------|--------------------|---------  |
| **Durante o desenvolvimento** | caixa-branca, caixa-preta, ad-hoc, API | TDD: caixa-preta antes de codificar → caixa-branca após |
| **Antes do commit/PR** | sanidade, fumaça | Rápido: < 15 min |
| **Durante o code review** | caixa-branca (cobertura) | Análise estática assistida |
| **Após merge/integração** | regressão, integração | Verificar que nada quebrou |
| **Antes de staging** | sistema, exploratório | Validação completa |
| **Em staging** | desempenho, carga, segurança, compatibilidade | Não-funcionais exigem ambiente |
| **Antes do release** | estresse, recuperação | Validação de resiliência |
| **Com o cliente/PO** | aceitação-UAT, usabilidade | Envolve stakeholder externo |

---

## Matriz 10 — Cobertura de Critérios de Aceite

> *Mapeamento dos 10 critérios de aceite (CA) do SDD-master contra as 18 skills*

| Critério de Aceite | Aplicável a | Verificação |
|-------------------|------------|-------------|
| CA-01: Frontmatter YAML completo | Todas as 18 skills | grep por `name:` e `description:` em cada SKILL.md |
| CA-02: `description` 80-200 palavras com gatilhos | Todas as 18 skills | Contagem de palavras do campo `description` |
| CA-03: "Quando NÃO usar" com ≥ 3 itens | Todas as 18 skills | Verificar seção existe e tem ≥ 3 bullets |
| CA-04: Processo com 4-10 passos agnósticos | Todas as 18 skills | Contar passos; buscar por nomes de linguagens |
| CA-05: Checklist com ≥ 5 perguntas sim/não | Todas as 18 skills | Verificar seção existe e tem ≥ 5 itens de checklist |
| CA-06: Exemplo conceitual sem linguagem específica | Todas as 18 skills | Verificar ausência de `python`, `javascript`, `java`, etc. no bloco principal |
| CA-07: Tabela "Skills Relacionadas" | Todas as 18 skills | Verificar tabela existe e tem ≥ 1 linha |
| CA-08: Revisão gramatical aplicada | Todas as 18 skills | Executar revisor-gramatical e registrar resultado |
| CA-09: skill-injection-auditor resultado SEGURO | Todas as 18 skills | Executar auditoria e registrar veredicto |
| CA-10: Referência à categoria IBM | Todas as 18 skills | Verificar campo `categoria_ibm` no frontmatter |

---

## Legenda de Status

| Símbolo | Significado | Próxima ação |
|---------|-------------|--------------|
| 🔴 | Não iniciado | Criar o artefato |
| 🟡 | Spec pronta, implementação pendente | Implementar a skill/agent |
| 🟢 | Implementado, auditoria pendente | Executar skill-injection-auditor + revisor-gramatical |
| ✅ | Implementado e auditado | Nenhuma |

---

## Resumo de Cobertura

| Categoria | Total RF | Specs Prontas | Implementados | Auditados |
|-----------|---------|--------------|--------------|----------|
| Infraestrutura | 7 | 7 | 7 | 7 |
| Técnicas de Projeto | 2 | 2 | 2 | 2 |
| Funcionais de Método | 6 | 6 | 6 | 6 |
| Por Nível | 3 | 3 | 3 | 3 |
| Especializados | 7 | 7 | 7 | 7 |
| Agents | 5 | 5 | 5 | 5 |
| **TOTAL** | **30** | **30** | **30** | **30** |

**Cobertura de Specs:** 30/30 (100%) ✅  
**Cobertura de Implementação:** 30/30 (100%) ✅  
**Cobertura de Auditoria:** 30/30 (100%) ✅ — 18 skills auditadas com skill-injection-auditor | Veredicto: 18/18 SEGURO

> **Auditoria executada em:** 2026-04-30 | **Ferramenta:** skill-injection-auditor (análise heurística 7 vetores) | **Relatório:** `_reversa_sdd/audit-report.json`
