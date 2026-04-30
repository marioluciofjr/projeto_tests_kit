---
name: workflow-testes-software
description: "Workflow completo do ciclo de vida de testes de software baseado nas boas práticas da IBM. Use quando quiser seguir um processo estruturado de ponta a ponta para planejar, executar e reportar testes. Ativa automaticamente as skills e agents corretos em cada etapa. Gatilhos: 'iniciar ciclo de testes', 'workflow de testes', 'processo completo de QA', 'como testar do início ao fim', 'pipeline de testes', 'plano de testes IBM'."
versao: "1.0"
referencia: "IBM — O que são testes de software? (https://www.ibm.com/br-pt/think/topics/software-testing)"
---

# Workflow: Ciclo Completo de Testes de Software

> Baseado nas boas práticas da IBM. Agnóstico de linguagem e ferramenta.
> **Referência:** [IBM — O que são testes de software?](https://www.ibm.com/br-pt/think/topics/software-testing)

---

## Como usar este workflow

Este workflow guia você por **6 etapas** do ciclo de testes — do planejamento ao relatório final. Em cada etapa, as skills e agents corretos são indicados. Você pode entrar no fluxo em qualquer ponto, dependendo de onde está no seu ciclo de desenvolvimento.

```
PLANEJAMENTO → DESIGN → AMBIENTE → EXECUÇÃO → ANÁLISE → RELATÓRIO
     1              2         3           4          5          6
```

---

## Etapa 1 — Planejamento de Testes

**Objetivo:** Definir o escopo, abordagem, recursos e critérios de sucesso antes de escrever um único caso de teste.

**Quando fazer:** No início de cada sprint, release ou entrega significativa.

### Perguntas a responder nesta etapa

1. Quais funcionalidades serão testadas?
2. Quais tipos de teste são necessários para esta entrega?
3. Quais são os critérios de aceite (DoD — Definition of Done)?
4. Qual o nível de risco desta entrega?
5. Há prazo definido para testes?

### Mapa de decisão: qual(is) tipo(s) de teste devo aplicar?

```
Nova feature implementada?
├── Sim → Sempre: fumaça → caixa-preta → integração
│         Se crítica: + sistema + regressão completa
│         Se exposta externamente: + teste-de-API
│         Se toca segurança: + teste-de-seguranca
│         Se é UI: + usabilidade + compatibilidade
└── Não (apenas refatoração) → fumaça → regressão → caixa-branca

Mudança de infraestrutura ou deploy?
├── Sim → fumaça → teste-de-recuperacao → carga → estresse
└── Não → prosseguir com plano normal

Cliente vai validar?
├── Sim → aceitacao-do-usuario → agent-testes-de-aceitacao
└── Não → manter ciclo técnico
```

### Skills e agents desta etapa

| Recurso | Uso |
|---------|-----|
| `agent-testes-de-unidade` | Definir escopo de testes unitários e TDD |
| `agent-testes-de-integracao` | Mapear pontos de integração a testar |
| `agent-testes-de-sistema` | Definir jornadas end-to-end críticas |
| `agent-testes-de-aceitacao` | Elicitar critérios de aceite com o cliente |

---

## Etapa 2 — Design dos Casos de Teste

**Objetivo:** Criar casos de teste concretos para cada funcionalidade ou comportamento a validar.

**Quando fazer:** Após o planejamento, antes da execução.

### Técnicas de design (escolha conforme contexto)

| Técnica | Skill | Quando usar |
|---------|-------|-------------|
| **Caixa Branca** | `teste-de-caixa-branca` | Tem acesso ao código; quer cobertura de caminhos |
| **Caixa Preta** | `teste-de-caixa-preta` | Valida comportamento externo; TDD; UAT |
| **Partição de Equivalência** | `teste-de-caixa-preta` | Agrupar entradas com comportamento idêntico |
| **Valores Limite** | `teste-de-caixa-preta` | Testar bordas de intervalos válidos/inválidos |
| **Given-When-Then** | `teste-de-aceitacao-do-usuario` | Escrever critérios em linguagem de negócio |

### Estrutura básica de um caso de teste

```
ID:               TC-[número]
Título:           [Descrição breve do que está sendo testado]
Pré-condições:    [Estado do sistema antes do teste]
Passos:           1. [Ação]
                  2. [Ação]
                  ...
Resultado esp.:   [O que deve acontecer]
Resultado real:   [Preencher durante execução]
Status:           [ ] Não executado | [P] Passou | [F] Falhou | [B] Bloqueado
Severidade (se F): 🔴 Crítica | 🟠 Alta | 🟡 Média | 🟢 Baixa
```

### Skills de design desta etapa

- `teste-de-caixa-branca` — Para testes com acesso ao código
- `teste-de-caixa-preta` — Para testes baseados em comportamento
- `teste-exploratorio` — Para design livre com charter
- `teste-de-API` — Para contratos de interface

---

## Etapa 3 — Preparação do Ambiente

**Objetivo:** Garantir que o ambiente de teste está disponível, estável e representativo.

**Quando fazer:** Antes de iniciar a execução dos testes.

### Checklist de ambiente

- [ ] Ambiente de teste isolado de produção
- [ ] Dados de teste representativos carregados
- [ ] Dependências externas disponíveis (APIs, bancos, filas)
- [ ] Versão correta do software deployada
- [ ] Logs habilitados para captura de evidências
- [ ] Ferramentas de teste configuradas
- [ ] Acesso concedido aos testadores

### Validação de ambiente — execute primeiro

Antes de qualquer outro teste, execute o **teste de fumaça** para confirmar que o build está de pé:

```
Skill recomendada: teste-de-fumaca
Critério de sucesso: todas as funções críticas respondem em < 5 min de verificação
Se FALHAR → parar tudo. Reportar ao time de dev. Reagendar testes.
```

---

## Etapa 4 — Execução dos Testes

**Objetivo:** Executar os casos de teste planejados e registrar os resultados.

**Quando fazer:** Com ambiente validado (fumaça passou).

### Ordem recomendada de execução (pirâmide IBM)

```
① UNITÁRIOS          → agent-testes-de-unidade
   caixa-branca / caixa-preta / TDD
   ↓ (todos os unitários passaram)

② FUMAÇA             → skill: teste-de-fumaca
   Build verification — o sistema está de pé?
   ↓ (fumaça passou)

③ INTEGRAÇÃO         → agent-testes-de-integracao
   teste-de-integracao / teste-de-API
   ↓ (integração passou)

④ REGRESSÃO          → skill: teste-de-regressao
   Nada que funcionava antes quebrou?
   ↓ (regressão passou)

⑤ SISTEMA            → agent-testes-de-sistema
   teste-de-sistema / teste-exploratorio / teste-de-sanidade
   ↓ (sistema passou)

⑥ NÃO-FUNCIONAIS     → skills especializadas (conforme plano)
   desempenho / carga / estresse / segurança / usabilidade / compatibilidade / recuperação
   ↓ (não-funcionais aprovados)

⑦ ACEITAÇÃO          → agent-testes-de-aceitacao
   teste-de-aceitacao-do-usuario (com o cliente/PO)
```

### Regras durante a execução

| Situação | Ação |
|---------|------|
| Falha Crítica encontrada | Parar execução → reportar imediatamente → aguardar correção |
| Falha Alta encontrada | Registrar → continuar outros testes → reportar ao fim da sessão |
| Ambiente instável | Parar → re-verificar fumaça → continuar apenas se passar |
| Resultado ambíguo | Documentar como "resultado inconclusivo" → escalar para revisão |
| Tempo esgotado | Documentar o que foi e não foi executado → emitir relatório parcial |

### Registro de evidências

Para cada falha encontrada, registrar obrigatoriamente:
1. **Passos para reproduzir** (exatos e completos)
2. **Resultado esperado** vs. **resultado real**
3. **Ambiente** (versão, SO, browser, etc.)
4. **Severidade** (Crítica / Alta / Média / Baixa)
5. **Evidência** (screenshot, log, vídeo)

---

## Etapa 5 — Análise dos Resultados

**Objetivo:** Interpretar os dados de execução, classificar falhas e tomar a decisão de Go/No-Go.

**Quando fazer:** Ao final de cada ciclo de execução.

### Métricas a calcular

| Métrica | Fórmula |
|---------|---------|
| Taxa de aprovação | (Testes que passaram / Total executados) × 100 |
| Taxa de falha | (Testes que falharam / Total executados) × 100 |
| Cobertura funcional | (Funcionalidades testadas / Total de funcionalidades) × 100 |
| Densidade de defeitos | Falhas encontradas / Pontos de função ou tamanho da entrega |

### Classificação de impacto das falhas (IBM)

| Severidade | Definição | Exemplo |
|-----------|-----------|---------|
| 🔴 **Crítica** | Sistema inoperante ou perda de dados | Login não funciona; dados corrompidos |
| 🟠 **Alta** | Funcionalidade importante indisponível | Relatório não gera; pagamento falha |
| 🟡 **Média** | Funcionalidade parcialmente comprometida | Filtro retorna resultados incorretos |
| 🟢 **Baixa** | Problema cosmético ou de menor impacto | Texto mal alinhado; label errado |

### Critérios de decisão Go/No-Go

| Condição | Decisão |
|---------|---------|
| Zero falhas Críticas e Alta; cobertura ≥ meta definida | ✅ **GO** |
| Falhas Alta com plano de correção acordado e prazo | ⚠️ **GO CONDICIONAL** |
| Qualquer falha Crítica sem correção | 🛑 **NO-GO** |
| Cobertura abaixo do mínimo definido (ex: < 80%) | 🛑 **NO-GO** |
| Testes não-funcionais críticos não executados | 🛑 **NO-GO** (para releases de produção) |

### Skill e agent desta etapa

```
agent-relatorios → Compila, classifica e emite a decisão fundamentada de Go/No-Go
```

---

## Etapa 6 — Relatório e Encerramento

**Objetivo:** Comunicar os resultados, documentar o ciclo e preparar o próximo.

**Quando fazer:** Ao final de cada ciclo — antes do release ou da próxima sprint.

### Tipos de relatório

| Relatório | Público | Conteúdo |
|-----------|---------|---------|
| **Técnico** | Time de dev | Todos os casos, falhas com stack trace, cobertura por módulo |
| **Executivo** | Gestores / PM | Sumário, métricas gerais, decisão Go/No-Go, próximos passos |
| **Release** | Todos | Técnico + Executivo + evidências + assinatura de aprovação |
| **Parcial** | Time de dev | Resultados até o momento + bloqueios + projeção de conclusão |

### Template de relatório mínimo

```
# Relatório de Testes — [Sistema] v[X.Y.Z]
Data: [____] | Ambiente: [____] | Responsável: [____]

## Sumário Executivo
[2-3 frases sobre o resultado geral]
Decisão: ✅ GO | ⚠️ GO CONDICIONAL | 🛑 NO-GO

## Métricas
| Total executados | Aprovados | Reprovados | Bloqueados | Cobertura |
|-----------------|-----------|------------|------------|-----------|
| N               | N (X%)    | N (X%)     | N          | X%        |

## Falhas Críticas e Altas
[Tabela: ID | Descrição | Severidade | Status]

## Próximos Passos
[Lista acionável com responsável e prazo]
```

### Skill e agent desta etapa

```
agent-relatorios → Gera o relatório no formato adequado ao público
```

### Atividades de encerramento do ciclo

- [ ] Relatório final enviado aos stakeholders
- [ ] Bugs abertos no rastreador da equipe com prioridade definida
- [ ] Ambientes de teste limpos / dados removidos
- [ ] Casos de teste atualizados (se comportamento mudou)
- [ ] Lições aprendidas registradas
- [ ] Próximo ciclo de testes planejado

---

## Resumo do workflow

| Etapa | Duração típica | Output | Responsável |
|-------|--------------|--------|-------------|
| 1 — Planejamento | 10-20% do tempo total | Plano de testes | QA Lead / Dev Sênior |
| 2 — Design | 20-30% | Casos de teste documentados | Testadores / Devs |
| 3 — Ambiente | 5-10% | Ambiente pronto + fumaça passou | Infra / DevOps |
| 4 — Execução | 40-50% | Resultados registrados | Todos os testadores |
| 5 — Análise | 5-10% | Decisão Go/No-Go | QA Lead |
| 6 — Relatório | 5% | Relatório entregue | QA Lead |

---

## Skills e agents por etapa (mapa rápido)

```
PLANEJAMENTO   → agents (todos os 4 de pirâmide)
DESIGN         → caixa-branca · caixa-preta · exploratorio · API
AMBIENTE       → fumaca (validação de build)
EXECUÇÃO       → todos os tipos conforme pirâmide
ANÁLISE        → agent-relatorios
RELATÓRIO      → agent-relatorios
```

---

*Workflow baseado em: [IBM — O que são testes de software?](https://www.ibm.com/br-pt/think/topics/software-testing)*
