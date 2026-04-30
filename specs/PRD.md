# PRD — tests-kit

> **Status:** Em revisão
> **Versão:** 1.0
> **Última atualização:** 2026-04-30
> **Responsável:** Mário Lúcio
> **Metodologia:** Spec-Driven Development (SDD) via Reversa Framework
> **Referência técnica:** IBM Software Testing Reference (testes_de_software_IBM.pdf)

---

## 1. Visão Geral

### 1.1 Resumo Executivo

O **tests-kit** é um kit portátil de skills para agentes de IA (compatível com Gemini CLI, Antigravity e demais engines agnósticas) que guia engenheiros de software — do iniciante ao sênior — na adoção de boas práticas de testes ao longo de todo o ciclo de desenvolvimento. O kit fornece personas especializadas (agents) e habilidades executáveis (skills) organizadas por tipo de teste, todas agnósticas de linguagem de programação.

### 1.2 Problema

Engenheiros de software, especialmente iniciantes e praticantes de "vibe coding", tendem a negligenciar testes por:

- Falta de conhecimento sobre **quais tipos de teste** existem e **quando aplicar cada um**
- Ausência de **processos padronizados** e acessíveis que guiem a execução de testes
- Dificuldade em escolher **técnicas** (caixa-branca vs. caixa-preta) conforme o contexto
- Carência de **personas especializadas** de IA que dominem testes e possam guiar o desenvolvedor interativamente

O resultado: código entregue sem cobertura adequada, bugs em produção, débito técnico acumulado e times que "só testam quando têm tempo".

### 1.3 Solução Proposta

Um **kit de skills e agentes de IA** que:

1. Fornece **18 skills especializadas** por tipo de teste — cada uma com instruções claras, critérios de qualidade e checklists executáveis
2. Disponibiliza **4 personas de agentes** especializadas nos 4 níveis clássicos de teste (Unidade, Integração, Sistema e Aceitação)
3. Inclui um **README.md explicativo** cobrindo toda a metodologia, estrutura e modo de uso
4. É **agnóstico de linguagem** — funciona com Python, JavaScript, Java, Go, ou qualquer outra stack
5. Usa como base teórica a **referência IBM de testes de software**, garantindo rigor técnico sem sacrificar acessibilidade

### 1.4 Objetivos do Produto

- **Objetivo 1:** Reduzir a barreira de entrada para boas práticas de testes — qualquer engenheiro, independente do nível, consegue usar uma skill em menos de 2 minutos
- **Objetivo 2:** Cobrir os principais tipos de teste documentados na literatura técnica (IBM, ISTQB) com skills acionáveis por IA
- **Objetivo 3:** Criar um kit reutilizável e extensível, que sirva como base para equipes customizarem seus próprios processos de QA
- **Objetivo 4:** Garantir que o README.md seja completo o suficiente para que um desenvolvedor iniciante entenda a metodologia antes de usar qualquer skill
- **Objetivo 5:** Versionar todo o kit via Git desde o início, garantindo rastreabilidade e contribuições futuras

---

## 2. Público-alvo & Personas

### Persona Principal — Dev Júnior / Vibe Coder

- **Perfil:** Desenvolvedor iniciante, 0–2 anos de experiência, acostumado a gerar código com IA sem seguir processos formais
- **Dores:**
  - Não sabe por onde começar quando alguém fala "escreva testes"
  - Acha que testes são "coisa de empresa grande"
  - Nunca ouviu falar de teste de fumaça, regressão ou carga
- **Ganhos esperados:**
  - Ter um agente de IA que guia passo a passo a criação de testes
  - Entender a diferença entre tipos de teste de forma clara e sem jargão
  - Sentir confiança para entregar código com cobertura de testes
- **Cenário de uso:** Chama o agente `agent-testes-de-unidade.md`, descreve o que seu código faz e recebe um roteiro de testes para implementar

### Persona Secundária — Engenheiro Pleno / Sênior

- **Perfil:** 3+ anos de experiência, conhece os tipos de teste mas não tem um processo padronizado ou rápido de referência
- **Dores:**
  - Perde tempo pesquisando a diferença entre teste de carga e stress
  - Quer um checklist rápido para auditar a cobertura de testes de um PR
  - Precisa orientar juniors sobre quando usar cada tipo de teste
- **Ganhos esperados:**
  - Skills como referência técnica rápida e acionável
  - Agentes especializados que assumem o papel de "QA sênior" na equipe
  - Kit pronto para plugar em qualquer projeto ou equipe
- **Cenário de uso:** Usa a skill `teste-de-desempenho` para guiar um agente de IA a criar um plano de testes de carga antes de um lançamento

### Persona Terciária — Tech Lead / Arquiteto de QA

- **Perfil:** Responsável por definir estratégias de qualidade no time
- **Dores:**
  - Quer padronizar testes sem criar burocracia
  - Precisa de documentação de processo que a equipe realmente use
- **Ganhos esperados:**
  - Usar o tests-kit como base do playbook de QA do time
  - Customizar as skills conforme as necessidades da stack do time
- **Cenário de uso:** Fork do repositório, adaptação das skills para a stack do time, integração ao CI/CD

---

## 3. Requisitos Funcionais

### 3.1 MVP (Estrutura Essencial)

| ID | Componente | Descrição | Prioridade |
|----|-----------|-----------|-----------|
| RF-01 | `AGENTS.md` | Arquivo raiz que referencia todos os agentes disponíveis no kit | Alta |
| RF-02 | `README.md` | Documentação completa: o que é o kit, como usar, metodologia, estrutura de pastas, cada skill e agente explicados | Alta |
| RF-03 | `.agent/rules/GEMINI.md` | Regras globais do kit para motores de IA (como carregar agents/skills, comportamento padrão) | Alta |
| RF-04 | `.agent/ARCHITECTURE.md` | Visão arquitetural do kit: como os componentes se relacionam, decisões de design | Alta |
| RF-05 | Skills (18) | Uma pasta por tipo de teste, cada uma com `SKILL.md` seguindo o padrão de skills agnósticas | Alta |
| RF-06 | Agents (4) | Arquivos `.md` de personas especializadas em cada nível de teste clássico | Alta |
| RF-07 | Git | Repositório inicializado com commits semânticos a cada entrega | Alta |

### 3.2 Skills — Detalhamento (18 skills)

#### 3.2.1 Técnicas de Teste (Caixa)

| ID | Skill | Descrição | Prioridade |
|----|-------|-----------|-----------|
| RF-08 | `teste-de-caixa-branca` | Guia testes com conhecimento interno do código: cobertura de caminhos, condições e loops | Alta |
| RF-09 | `teste-de-caixa-preta` | Guia testes sem conhecimento interno: entradas, saídas esperadas, partição de equivalência | Alta |

#### 3.2.2 Testes Funcionais de Método

| ID | Skill | Descrição | Prioridade |
|----|-------|-----------|-----------|
| RF-10 | `teste-ad-hoc` | Testes não planejados, exploração livre sem script definido | Alta |
| RF-11 | `teste-de-API` | Valida contratos, endpoints, payloads, autenticação e respostas HTTP | Alta |
| RF-12 | `teste-exploratorio` | Simultâneo ao design: aprende, projeta e executa testes ao mesmo tempo | Alta |
| RF-13 | `teste-de-regressao` | Garante que novas mudanças não quebraram funcionalidades existentes | Alta |
| RF-14 | `teste-de-sanidade` | Verifica rapidamente se uma funcionalidade específica ainda funciona após mudança | Alta |
| RF-15 | `teste-de-fumaca` | Build smoke test: valida se o sistema sobe e funções críticas básicas respondem | Alta |

#### 3.2.3 Testes por Nível

| ID | Skill | Descrição | Prioridade |
|----|-------|-----------|-----------|
| RF-16 | `teste-de-integracao` | Valida a comunicação entre módulos, serviços ou sistemas | Alta |
| RF-17 | `teste-de-sistema` | Valida o comportamento do sistema completo como uma unidade | Alta |
| RF-18 | `teste-de-aceitacao-do-usuario` | UAT: valida que o produto atende os critérios de aceitação do usuário/negócio | Alta |

#### 3.2.4 Testes Especializados

| ID | Skill | Descrição | Prioridade |
|----|-------|-----------|-----------|
| RF-19 | `teste-de-recuperacao` | Valida como o sistema se recupera de falhas, crashes e condições de erro | Alta |
| RF-20 | `teste-de-desempenho` | Mede tempo de resposta, throughput e uso de recursos sob condições normais | Alta |
| RF-21 | `teste-de-carga` | Avalia comportamento do sistema sob volume crescente de usuários/requisições | Alta |
| RF-22 | `teste-de-estresse` | Empurra o sistema além dos limites para encontrar pontos de falha | Alta |
| RF-23 | `teste-de-seguranca` | Identifica vulnerabilidades, testa autenticação, autorização e proteção de dados | Alta |
| RF-24 | `teste-de-usabilidade` | Avalia experiência do usuário: clareza, eficiência e satisfação de uso | Alta |
| RF-25 | `teste-de-compatibilidade` | Valida o sistema em diferentes browsers, OS, devices e versões de dependências | Alta |

### 3.3 Agents — Detalhamento (4 agentes)

| ID | Agent | Nível de Teste | Especialidade |
|----|-------|---------------|--------------|
| RF-26 | `agent-testes-de-unidade.md` | Unitário | Foca em funções/métodos isolados, mocking, TDD |
| RF-27 | `agent-testes-de-integracao.md` | Integração | Foca na comunicação entre módulos, contratos de API |
| RF-28 | `agent-testes-de-sistema.md` | Sistema | Foca no sistema completo, fluxos de ponta a ponta |
| RF-29 | `agent-testes-de-aceitacao.md` | Aceitação | Foca em critérios de negócio, UAT, BDD |

### 3.4 Padrão de Qualidade de Cada Skill

Cada SKILL.md deve conter:

| Elemento | Descrição |
|---------|-----------|
| Frontmatter YAML | `name`, `description` otimizados para triggering por LLMs |
| O que é | Definição clara e acessível do tipo de teste |
| Quando usar | Contextos e gatilhos de ativação (incluindo os da IBM) |
| Quando NÃO usar | Anti-padrões e confusões comuns |
| Processo passo-a-passo | Roteiro executável, agnóstico de linguagem |
| Critérios de qualidade | O que diferencia um bom teste de um ruim |
| Exemplos conceituais | Pseudocódigo ou descrição de cenários |
| Checklist | Lista de verificação antes de considerar o teste completo |
| Relacionamentos | Links para outras skills relacionadas |

### 3.5 Pós-MVP (Roadmap Futuro)

| ID | Componente | Fase |
|----|-----------|------|
| RF-30 | Workflows de teste (ex: `pre-release-checklist.md`) | v2.0 |
| RF-31 | Skills de ferramentas específicas (Jest, Pytest, JUnit) | v2.0 |
| RF-32 | Agent de QA Lead — orquestra os 4 agentes principais | v2.0 |
| RF-33 | Templates de plano de teste por tipo de projeto | v2.1 |
| RF-34 | Integração com CI/CD (GitHub Actions workflows) | v3.0 |

---

## 4. Requisitos Não-Funcionais

| Categoria | Requisito | Critério de Aceitação |
|-----------|-----------|----------------------|
| **Portabilidade** | Compatível com qualquer engine de IA que suporte skills/SKILL.md | Testado em Gemini CLI e Antigravity |
| **Agnóstico** | Nenhuma skill pode referenciar linguagem ou framework específico no corpo principal | 0 referências a linguagens sem qualificação contextual |
| **Acessibilidade** | Linguagem clara para iniciantes sem sacrificar rigor técnico | Leitura compreensível por dev com menos de 1 ano de experiência |
| **Extensibilidade** | Estrutura de pastas permite adicionar novas skills sem modificar o kit base | Nova skill = nova pasta, sem alteração de arquivos existentes |
| **Segurança** | Nenhuma skill contém prompt injection, instruções maliciosas ou código executável inseguro | Auditoria pelo skill-injection-auditor com resultado SEGURO |
| **Rastreabilidade** | Toda skill referencia a categoria de teste correspondente na taxonomia IBM | 100% das skills com referência à fonte |
| **Versionamento** | Kit versionado via Git com commits semânticos por feature | Git log auditável desde o início |
| **Documentação** | README.md completo antes da primeira release | Score de completude >= 90% |

---

## 5. Fora do Escopo (v1.0)

Explicitamente **fora** do escopo desta versão:

- Scripts de automação de testes (ex: geração de código de testes)
- Integração direta com frameworks de teste (Jest, Pytest, etc.)
- Dashboard de cobertura de testes
- Plugin para IDEs (VS Code, IntelliJ)
- Suporte a testes de hardware ou sistemas embarcados
- Skills em idioma diferente do Português (internacionalização é v2.0+)

---

## 6. Critérios de Sucesso & KPIs

| Métrica | Meta | Prazo |
|---------|------|-------|
| Todas as 18 skills criadas e auditadas | 18/18 com resultado SEGURO | Entrega v1.0 |
| Todos os 4 agents criados | 4/4 completos | Entrega v1.0 |
| README.md completo | Score SDD >= 80 | Entrega v1.0 |
| Git: commits semânticos | 100% das entregas comitadas | Contínuo |
| ARCHITECTURE.md completo | Diagrama C4 + decisões ADR | Entrega v1.0 |
| Auditoria de segurança | 0 skills com resultado MALICIOSO | Entrega v1.0 |

---

## 7. Estrutura Final do Projeto

```
tests-kit/
├── .agent/
│   ├── agents/
│   │   ├── agent-testes-de-unidade.md
│   │   ├── agent-testes-de-integracao.md
│   │   ├── agent-testes-de-sistema.md
│   │   └── agent-testes-de-aceitacao.md
│   ├── rules/
│   │   └── GEMINI.md
│   ├── skills/
│   │   ├── teste-de-caixa-branca/     (SKILL.md)
│   │   ├── teste-de-caixa-preta/      (SKILL.md)
│   │   ├── teste-ad-hoc/              (SKILL.md)
│   │   ├── teste-de-API/              (SKILL.md)
│   │   ├── teste-exploratorio/        (SKILL.md)
│   │   ├── teste-de-regressao/        (SKILL.md)
│   │   ├── teste-de-sanidade/         (SKILL.md)
│   │   ├── teste-de-fumaca/           (SKILL.md)
│   │   ├── teste-de-integracao/       (SKILL.md)
│   │   ├── teste-de-sistema/          (SKILL.md)
│   │   ├── teste-de-aceitacao-do-usuario/ (SKILL.md)
│   │   ├── teste-de-recuperacao/      (SKILL.md)
│   │   ├── teste-de-desempenho/       (SKILL.md)
│   │   ├── teste-de-carga/            (SKILL.md)
│   │   ├── teste-de-estresse/         (SKILL.md)
│   │   ├── teste-de-seguranca/        (SKILL.md)
│   │   ├── teste-de-usabilidade/      (SKILL.md)
│   │   └── teste-de-compatibilidade/  (SKILL.md)
│   ├── workflows/
│   └── ARCHITECTURE.md
├── AGENTS.md
└── README.md
```

---

## 8. Roadmap de Alto Nível

| Fase | Entregável | Status |
|------|-----------|--------|
| **Fase 1 — PRD** | Este documento | Em andamento |
| **Fase 2 — Specs SDD** | Spec de cada skill e agent | Próxima |
| **Fase 3 — Arquitetura** | ARCHITECTURE.md + ADRs | Pendente |
| **Fase 4 — Skills** | 18 SKILL.md criados | Pendente |
| **Fase 5 — Agents** | 4 agent .md criados | Pendente |
| **Fase 6 — Estrutura Global** | AGENTS.md + GEMINI.md | Pendente |
| **Fase 7 — README** | README.md completo | Pendente |
| **Fase 8 — Auditoria** | skill-injection-auditor em todas | Pendente |
| **Fase 9 — Git** | Commits semânticos + histórico | Contínuo |

---

## 9. Riscos e Dependências

| Risco/Dependência | Probabilidade | Impacto | Mitigação |
|-------------------|--------------|---------|-----------|
| Skills com linguagem muito técnica (inacessível para juniors) | Média | Alto | Revisão pelo revisor-gramatical em cada SKILL.md |
| Skills com conteúdo sobreposto (ex: fumaca vs. sanidade vs. regressão) | Alta | Médio | Definir claramente a fronteira entre skills similares nas specs SDD |
| Triggering inadequado de skills por LLMs | Média | Alto | Otimizar descriptions via skill-creator + testes de acionamento |
| Escopo creep (adicionar v2.0 no v1.0) | Alta | Médio | Backlog explícito na seção "Fora do Escopo" |
| Prompt injection nas skills | Baixa | Muito Alto | Auditoria obrigatória via skill-injection-auditor antes de release |

---

## 10. Taxonomia de Referência IBM

Com base na referência `testes_de_software_IBM.pdf`, as 18 skills cobrem as seguintes categorias:

| Categoria IBM | Skills Cobertas |
|--------------|-----------------|
| **Técnicas de Projeto de Teste** | Caixa Branca, Caixa Preta |
| **Testes Funcionais** | Ad-hoc, Exploratório, API, Sanidade, Fumaça, Regressão |
| **Testes por Nível** | Integração, Sistema, Aceitação do Usuário |
| **Testes Não-Funcionais** | Desempenho, Carga, Estresse, Segurança, Usabilidade, Compatibilidade |
| **Testes de Confiabilidade** | Recuperação |

---

## 11. Glossário

| Termo | Definição |
|-------|-----------|
| **Skill** | Pasta com SKILL.md que ensina um agente de IA a executar um tipo específico de teste |
| **Agent** | Arquivo .md que define uma persona especializada em um nível de teste |
| **Kit** | Conjunto completo de skills + agents + regras + documentação |
| **Vibe coding** | Prática de gerar código com IA sem seguir processos formais de engenharia |
| **Triggering** | Capacidade de uma skill ser acionada corretamente pelo LLM diante do contexto certo |
| **Agnóstico** | Independente de linguagem de programação, framework ou plataforma específica |
| **TDD** | Test-Driven Development — escrever testes antes do código de produção |
| **UAT** | User Acceptance Testing — testes conduzidos pelo usuário final ou stakeholder |
| **ISTQB** | International Software Testing Qualifications Board — certificação internacional de QA |

---

## 12. Histórico de Revisões

| Versão | Data | Autor | Alterações |
|--------|------|-------|-----------|
| 1.0 | 2026-04-30 | Reversa + Mário Lúcio | Versão inicial gerada via orquestração Reversa |
