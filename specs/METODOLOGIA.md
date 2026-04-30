# METODOLOGIA.md — Como o tests-kit foi construído

> Este documento registra a metodologia e as ferramentas utilizadas para criar o **tests-kit** — um kit de boas práticas de testes de software para engenheiros de todos os níveis.

---

## Visão geral do processo

O tests-kit foi construído usando **Spec-Driven Development (SDD)** — uma metodologia que prioriza a especificação completa antes da implementação. O processo foi orquestrado pelo framework **Reversa**, desenvolvido pelo professor Sandeco Macedo.

```
Elicitação de Requisitos → Specs SDD → Arquitetura → Implementação → Auditoria
        (PRD)              (23 SPECs)    (ARCHITECTURE)   (18+5)      (18/18 SEGURO)
```

---

## Framework Reversa

O **Reversa** é um framework de engenharia reversa e desenvolvimento dirigido por agentes, criado pelo professor **Sandeco Macedo**.

| Recurso | Link |
|---------|------|
| 🎥 Vídeo explicativo | [YouTube — Prof. Sandeco explica o Reversa](https://youtu.be/ARQBBKnfP_c?si=hU984zf2bHQwsHNw) |
| 📦 Repositório oficial | [github.com/sandeco/reversa](https://github.com/sandeco/reversa) |

O Reversa orquestrou a análise do projeto através de **agentes especializados**:

| Agente Reversa | Papel no tests-kit |
|---------------|-------------------|
| **Scout** | Mapeamento inicial + elicitação de requisitos via `prd-manager` |
| **SDD Master** | Definição do template e contrato arquitetural das 18 skills |
| **Arquiteto** | Geração do `ARCHITECTURE.md` com C4, ADRs e Spec Impact Matrix |
| **Redator** | Geração da `SDD-traceability.md` com 10 matrizes de rastreabilidade |

---

## Motor de IA

O kit foi gerado usando o modelo **Claude Sonnet 4.6 (Thinking)** como motor do **Agent Antigravity** — a IDE de IA do Google DeepMind.

| Ferramenta | Versão/Detalhe |
|-----------|----------------|
| Modelo de IA | Claude Sonnet 4.6 (Thinking) |
| IDE | Antigravity (Google DeepMind) |
| Framework de geração | Reversa (Prof. Sandeco Macedo) |

---

## Fases do projeto

### Fase 1 — Reconhecimento (PRD)

**Agente:** Scout (Reversa)

- Mapeamento da estrutura do projeto e tecnologias disponíveis
- Elicitação de requisitos via `prd-manager` com a referência técnica da IBM
- Decisões de escopo: público (qualquer nível de engenheiro), linguagem (agnóstica), nível de documentação (completo)
- **Output:** `PRD.md` — 30 requisitos funcionais definidos

### Fase 2 — Escavação (Especificações SDD)

**Agente:** SDD Master + Redator (Reversa)

- `SDD-master.md` — template e 10 critérios de aceite para todas as skills
- `SDD-tecnicas.md` — SPEC-01 (Caixa Branca) e SPEC-02 (Caixa Preta)
- `SDD-funcionais.md` — SPEC-03 a SPEC-08 (Ad-hoc, API, Exploratório, Regressão, Sanidade, Fumaça)
- `SDD-niveis.md` — SPEC-09 a SPEC-11 (Integração, Sistema, UAT)
- `SDD-especializados.md` — SPEC-12 a SPEC-18 (Recuperação, Desempenho, Carga, Estresse, Segurança, Usabilidade, Compatibilidade)
- `SDD-agents.md` — SPEC-19 a SPEC-23 (5 personas de agente)

### Fase 3 — Interpretação (Arquitetura)

**Agente:** Arquiteto (Reversa)

- `ARCHITECTURE.md` com diagrama C4 (Context, Container, Component)
- 5 ADRs (Architecture Decision Records) documentados
- Mapa de relacionamentos entre skills (grafo Mermaid)
- Spec Impact Matrix
- `SDD-traceability.md` — 10 matrizes de rastreabilidade PRD→SDD→Artefato

### Fase 4 — Implementação (Skills e Agents)

**Motor:** Claude Sonnet 4.6 (Thinking) via Antigravity

- 18 `SKILL.md` gerados (um por tipo de teste da taxonomia IBM)
- 5 arquivos de persona `agent-*.md`
- Todos agnósticos de linguagem, com frontmatter YAML completo
- Commits semânticos preservando a rastreabilidade

### Fase 5 — Infraestrutura

- `README.md` — documentação completa seguindo template padrão
- `AGENTS.md` — entry point com índice de skills e agents
- `.agent/rules/GEMINI.md` — regras globais de comportamento
- `.agent/workflows/workflow-testes.md` — ciclo completo baseado na IBM

### Fase 6 — Auditoria

**Ferramenta:** `skill-injection-auditor` (varredura heurística 7 vetores)

- 18 skills auditadas quanto a prompt injection, exfiltração de dados, execução de código, manipulação de identidade, instruções ocultas, recursividade maliciosa e escopo fora dos limites
- **Resultado:** 18/18 SEGURO ✅
- Relatório em `audit-report.json`

---

## Referência técnica base

O conteúdo das skills foi construído com base no artigo técnico da IBM:

> **"O que são testes de software?"**
> Autores: Stephanie Susnjara e Ian Smalley — IBM Think
> 🔗 [https://www.ibm.com/br-pt/think/topics/software-testing](https://www.ibm.com/br-pt/think/topics/software-testing)

A taxonomia IBM organiza os testes em:
- **Técnicas de Projeto de Teste** (caixa branca, caixa preta)
- **Testes Funcionais de Método** (ad-hoc, API, exploratório, regressão, sanidade, fumaça)
- **Testes por Nível** (unitário, integração, sistema, aceitação)
- **Testes Não-Funcionais** (desempenho, carga, estresse, segurança, usabilidade, compatibilidade)
- **Testes de Confiabilidade** (recuperação)

---

## Rastreabilidade completa

| Dimensão | Resultado |
|----------|-----------|
| Total de requisitos (PRD) | 30 RF |
| Specs SDD geradas | 30/30 (100%) |
| Artefatos implementados | 30/30 (100%) |
| Skills auditadas | 18/18 SEGURO |
| Veredicto final | ✅ APROVADO |

Para a rastreabilidade completa, veja `SDD-traceability.md`.

---

## Créditos

| Contribuição | Responsável |
|-------------|-------------|
| Framework Reversa (orquestração) | [Prof. Sandeco Macedo](https://github.com/sandeco) |
| Referência técnica de conteúdo | [IBM — Software Testing](https://www.ibm.com/br-pt/think/topics/software-testing) |
| Motor de geração (IA) | Claude Sonnet 4.6 (Thinking) via Antigravity |
| Criação e curadoria | [Mário Lúcio](https://www.linkedin.com/in/marioluciofjr) — Prazo Certo® |
