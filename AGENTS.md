# tests-kit — Índice de Skills e Agents

> **Versão:** 1.0 | Motor: Gemini / Antigravity ou qualquer engine compatível com Markdown
> Este é o **ponto de entrada** do tests-kit. Leia primeiro para descobrir o que está disponível.

---

## Agents disponíveis (5 personas especializadas)

| Agent | Especialidade | Quando chamar |
|-------|--------------|--------------|
| [`agent-testes-de-unidade`](.agent/agents/agent-testes-de-unidade.md) | Funções isoladas · TDD · Cobertura | "Quero testar essa função" / "Quero fazer TDD" |
| [`agent-testes-de-integracao`](.agent/agents/agent-testes-de-integracao.md) | Módulos · Contratos · Setup/Teardown | "Testar comunicação entre módulos A e B" |
| [`agent-testes-de-sistema`](.agent/agents/agent-testes-de-sistema.md) | End-to-end · Jornadas · Staging | "Testar o sistema completo" |
| [`agent-testes-de-aceitacao`](.agent/agents/agent-testes-de-aceitacao.md) | UAT · BDD · Critérios de aceite | "O cliente vai homologar a entrega" |
| [`agent-relatorios`](.agent/agents/agent-relatorios.md) | Resultados · Métricas · Go/No-Go | "Gere um relatório dos testes executados" |

---

## Skills disponíveis (18 tipos de teste)

### Técnicas de Projeto

| Skill | Gatilhos típicos |
|-------|-----------------|
| [`teste-de-caixa-branca`](.agent/skills/teste-de-caixa-branca/) | "cobertura de código", "testar caminhos internos" |
| [`teste-de-caixa-preta`](.agent/skills/teste-de-caixa-preta/) | "testar como usuário", "partição de equivalência" |

### Funcionais de Método

| Skill | Gatilhos típicos |
|-------|-----------------|
| [`teste-ad-hoc`](.agent/skills/teste-ad-hoc/) | "teste rápido", "sem planejamento" |
| [`teste-de-API`](.agent/skills/teste-de-API/) | "testar API", "validar endpoints" |
| [`teste-exploratorio`](.agent/skills/teste-exploratorio/) | "explorar sistematicamente", "charter" |
| [`teste-de-regressao`](.agent/skills/teste-de-regressao/) | "nada quebrou?", "após merge" |
| [`teste-de-sanidade`](.agent/skills/teste-de-sanidade/) | "essa feature ainda funciona?" |
| [`teste-de-fumaca`](.agent/skills/teste-de-fumaca/) | "sistema está de pé?", "smoke test" |

### Por Nível (Pirâmide)

| Skill | Gatilhos típicos |
|-------|-----------------|
| [`teste-de-integracao`](.agent/skills/teste-de-integracao/) | "módulos se comunicam?" |
| [`teste-de-sistema`](.agent/skills/teste-de-sistema/) | "testar end-to-end", "staging" |
| [`teste-de-aceitacao-do-usuario`](.agent/skills/teste-de-aceitacao-do-usuario/) | "homologação", "UAT" |

### Não-Funcionais

| Skill | Gatilhos típicos |
|-------|-----------------|
| [`teste-de-desempenho`](.agent/skills/teste-de-desempenho/) | "quão rápido?", "baseline de performance" |
| [`teste-de-carga`](.agent/skills/teste-de-carga/) | "aguenta N usuários?", "load test" |
| [`teste-de-estresse`](.agent/skills/teste-de-estresse/) | "limite do sistema?", "stress test" |
| [`teste-de-seguranca`](.agent/skills/teste-de-seguranca/) | "SQL injection", "OWASP", "API segura?" |
| [`teste-de-usabilidade`](.agent/skills/teste-de-usabilidade/) | "interface intuitiva?", "Nielsen" |
| [`teste-de-compatibilidade`](.agent/skills/teste-de-compatibilidade/) | "cross-browser", "funciona no Safari?" |

### Confiabilidade

| Skill | Gatilhos típicos |
|-------|-----------------|
| [`teste-de-recuperacao`](.agent/skills/teste-de-recuperacao/) | "e se o banco cair?", "circuit breaker" |

---

## Ordem recomendada

```
DEV      → caixa-branca / caixa-preta / ad-hoc
COMMIT   → sanidade → fumaça
MERGE    → regressão → integração
STAGING  → sistema → exploratório → [especializados]
RELEASE  → estresse → recuperação
CLIENTE  → aceitação → usabilidade
SEMPRE   → agent-relatorios (compilar resultados)
```
