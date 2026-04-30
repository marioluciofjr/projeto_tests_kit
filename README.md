# tests-kit

Kit de skills e agentes de IA para boas práticas de testes de software

![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)

## Índice

- [Introdução](#introdução)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Orientações](#orientações)
- [Créditos e metodologia](#créditos-e-metodologia)
- [Links úteis](#links-úteis)
- [Contribuições](#contribuições)
- [Licença](#licença)
- [Contato](#contato)

## Introdução

O **tests-kit** é um conjunto portátil de skills e agentes de IA que guia engenheiros de software — do iniciante ao sênior — em boas práticas de testes. Baseado na referência técnica da IBM, o kit cobre 18 tipos de teste organizados pela taxonomia oficial (funcionais, não-funcionais, confiabilidade e níveis da pirâmide), mais 5 agentes especializados, tudo agnóstico de linguagem de programação e pronto para uso em qualquer motor de IA compatível com Markdown.

## Estrutura do projeto

O tests-kit organiza seu conhecimento em três blocos principais: **skills** (como executar cada tipo de teste), **agents** (com quem contar em cada nível da pirâmide) e **regras globais** (como o motor de IA deve se comportar).

```
tests-kit/
├── .agent/
│   ├── agents/                          # 5 personas especializadas
│   │   ├── agent-testes-de-unidade.md   # Base da pirâmide — funções isoladas + TDD
│   │   ├── agent-testes-de-integracao.md # Comunicação entre módulos e serviços
│   │   ├── agent-testes-de-sistema.md   # Fluxos end-to-end em staging
│   │   ├── agent-testes-de-aceitacao.md # UAT com o cliente — critérios de aceite
│   │   └── agent-relatorios.md          # Compilação de resultados e decisão Go/No-Go
│   ├── rules/
│   │   └── GEMINI.md                    # Regras globais de comportamento do kit
│   ├── workflows/
│   │   └── workflow-testes.md           # Ciclo completo de testes baseado na IBM
│   ├── skills/                          # 18 skills de teste
│   │   ├── teste-de-caixa-branca/       # Cobertura de caminhos internos do código
│   │   ├── teste-de-caixa-preta/        # Validação por comportamento externo
│   │   ├── teste-ad-hoc/                # Exploração livre sem script
│   │   ├── teste-de-API/                # Contratos, endpoints e autenticação HTTP
│   │   ├── teste-exploratorio/          # Sessões com charter e heurísticas
│   │   ├── teste-de-regressao/          # Nada quebrou com a mudança?
│   │   ├── teste-de-sanidade/           # Feature específica ainda funciona?
│   │   ├── teste-de-fumaca/             # Build verification — sistema está de pé?
│   │   ├── teste-de-integracao/         # Módulos se comunicam corretamente?
│   │   ├── teste-de-sistema/            # Sistema completo end-to-end
│   │   ├── teste-de-aceitacao-do-usuario/ # UAT em linguagem de negócio
│   │   ├── teste-de-recuperacao/        # Resiliência a falhas e recuperação
│   │   ├── teste-de-desempenho/         # Métricas de velocidade e throughput
│   │   ├── teste-de-carga/              # Comportamento sob volume crescente
│   │   ├── teste-de-estresse/           # Ponto de colapso do sistema
│   │   ├── teste-de-seguranca/          # Vulnerabilidades e OWASP Top 10
│   │   ├── teste-de-usabilidade/        # Heurísticas de Nielsen e teste com usuário
│   │   └── teste-de-compatibilidade/   # Cross-browser, cross-OS, cross-device
│   └── ARCHITECTURE.md                  # Documentação arquitetural completa (C4 + ADRs)
├── specs/                               # Especificações SDD, PRD e rastreabilidade
├── AGENTS.md                            # Índice de agents e skills (entry point)
└── README.md                            # Este arquivo
```

### Pirâmide de testes e os agents

```
         ┌─────────────────────────────────────┐
         │   agent-testes-de-aceitacao          │  ← UAT com o cliente
         └────────────────┬────────────────────┘
                          │
         ┌────────────────▼────────────────────┐
         │   agent-testes-de-sistema            │  ← Validação técnica end-to-end
         └────────────────┬────────────────────┘
                          │
         ┌────────────────▼────────────────────┐
         │   agent-testes-de-integracao         │  ← Módulos integrados
         └────────────────┬────────────────────┘
                          │
         ┌────────────────▼────────────────────┐
         │   agent-testes-de-unidade            │  ← Funções isoladas + TDD
         └─────────────────────────────────────┘

         ┌─────────────────────────────────────┐
         │   agent-relatorios                   │  ← Compila resultados de qualquer nível
         └─────────────────────────────────────┘
```

### Taxonomia IBM das skills

| Categoria IBM | Skills |
|--------------|--------|
| Técnicas de Projeto | `caixa-branca` · `caixa-preta` |
| Funcionais de Método | `ad-hoc` · `API` · `exploratório` · `regressão` · `sanidade` · `fumaça` |
| Por Nível | `integração` · `sistema` · `aceitação-do-usuário` |
| Não-Funcionais | `desempenho` · `carga` · `estresse` · `segurança` · `usabilidade` · `compatibilidade` |
| Confiabilidade | `recuperação` |

> [!NOTE]
> A inspiração para o tests-kit foi o artigo técnico da IBM: [O que são testes de software?](https://www.ibm.com/br-pt/think/topics/software-testing) — de Stephanie Susnjara e Ian Smalley. Toda a taxonomia de testes (18 tipos organizados em 4 categorias) é derivada diretamente desta referência.

## Tecnologias utilizadas

<table>
  <tr>
    <td align="center"><img height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/markdown/markdown-original.svg" /><br><b>Markdown</b></td>
    <td align="center"><img height="60" width="80" src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/dark/gemini-color.png" /><br><b>Gemini</b></td>
    <td align="center"><img height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" /><br><b>Git</b></td>
  </tr>
</table>

- **Markdown** — Formato de todas as skills, agents e documentação do kit
- **Gemini / Antigravity** — Motor de IA que interpreta e executa as skills (compatível com qualquer engine que leia Markdown)
- **Git** — Versionamento semântico de todas as mudanças no kit

## Orientações

Antes de começar, certifique-se de ter instalado:

1. **Um motor de IA compatível com Markdown** — o tests-kit funciona com qualquer engine que suporte o carregamento de arquivos SKILL.md. Recomendamos o [Antigravity](https://antigravity.google/download) (IDE do Google DeepMind).

2. **Git** — para versionar e manter seu kit atualizado.

### Como usar uma skill

Simplesmente descreva o que quer fazer para o motor de IA. Exemplos que acionam skills automaticamente:

```
"Quero testar se minha API está retornando os status codes corretos"
→ Ativa: teste-de-API

"Fiz uma refatoração e quero garantir que nada quebrou"
→ Ativa: teste-de-regressao

"O deploy funcionou? O sistema está de pé?"
→ Ativa: teste-de-fumaca
```

### Como chamar um agent

```
"Ative o agent de testes de unidade — quero fazer TDD nessa função"
→ Carrega: agent-testes-de-unidade.md

"Preciso preparar o UAT com o cliente para essa entrega"
→ Carrega: agent-testes-de-aceitacao.md

"Gere um relatório dos resultados de QA dessa sprint"
→ Carrega: agent-relatorios.md
```

### Ordem recomendada na pirâmide

```
Caixa Branca/Preta → Unitários (agent) → Fumaça → Integração (agent)
→ Regressão → Sistema (agent) → [Especializados] → Aceitação (agent) → Relatório (agent)
```

## Créditos e metodologia

Este kit só foi possível graças a duas tecnologias:

### Framework Reversa — Prof. Sandeco Macedo

O **Reversa** é um framework de elicitação de requisitos e desenvolvimento dirigido por especificações (Spec-Driven Development), criado pelo professor **Sandeco Macedo**. Ele orquestrou todo o processo de construção do tests-kit — do PRD à auditoria final.

| Recurso | Link |
|---------|------|
| 🎥 Vídeo explicativo | [YouTube — Prof. Sandeco explica o Reversa](https://youtu.be/ARQBBKnfP_c?si=hU984zf2bHQwsHNw) |
| 📦 Repositório oficial | [github.com/sandeco/reversa](https://github.com/sandeco/reversa) |

### Motor de IA — Claude Sonnet 4.6 (Thinking)

A geração completa do kit — 18 skills, 5 agents, workflow, documentação e auditoria — foi executada pelo modelo **Claude Sonnet 4.6 (Thinking)** rodando como motor do **Agent Antigravity** (IDE do Google DeepMind). O modelo operou em modo *thinking* (raciocínio extendido), garantindo consistência e qualidade em todas as especificações geradas.

Para detalhes completos da metodologia, veja [`specs/METODOLOGIA.md`](specs/METODOLOGIA.md).

## Links úteis

- [Como instalar o VSCode](https://code.visualstudio.com/download) — Link direto para download
- [Como baixar o Antigravity](https://antigravity.google/download) — Página oficial de download da IDE do Google DeepMind
- [IBM — O que são testes de software?](https://www.ibm.com/br-pt/think/topics/software-testing) — Referência técnica base do tests-kit
- [Reversa — Framework do Prof. Sandeco](https://github.com/sandeco/reversa) — Framework que orquestrou a construção do kit
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — Referência de segurança usada na skill `teste-de-seguranca`
- [10 Heurísticas de Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/) — Referência usada na skill `teste-de-usabilidade`
- [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) — Site para ícones do ecossistema de IA
- [Devicon](https://devicon.dev/) — Ícones gerais sobre tecnologia

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

Ao contribuir com novas skills ou agents, siga obrigatoriamente:
- O template definido em `.agent/ARCHITECTURE.md` (seção "Template Padrão de SKILL.md")
- Os 10 Critérios de Aceite definidos no `SDD-master.md`
- Commits com mensagens semânticas (`feat`, `fix`, `docs`, `refactor`)

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/projeto_tests_kit/blob/main/LICENSE) para detalhes.

## Contato

Mário Lúcio - Prazo Certo®

<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div>
