---
name: teste-ad-hoc
description: >
  Guia o desenvolvedor em testes completamente livres, sem script ou planejamento prévio, conduzidos
  pela intuição e experiência. Use esta skill SEMPRE que o objetivo for testar de forma rápida e
  informal, sem roteiro predefinido. Acione quando o usuário mencionar: "teste ad-hoc", "teste
  livre", "testar sem planejamento", "quero só clicar por aí e ver o que quebra", "não tenho tempo
  para escrever testes formais agora", "quero fazer um teste rápido antes de entregar", "teste
  informal". Diferente do teste exploratório (que usa sessões estruturadas com charter e heurísticas),
  o ad-hoc é pura exploração livre sem compromisso de documentação formal. Ideal para verificações
  rápidas, descobertas iniciais de um sistema desconhecido ou validações de urgência. Funciona para
  qualquer tipo de software.
categoria_ibm: Testes Funcionais de Método
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-exploratorio
  - teste-de-fumaca
  - teste-de-sanidade
---

# Teste Ad-hoc

## O que é

O teste ad-hoc é a forma mais livre de teste de software: sem plano, sem script, sem documentação obrigatória. O testador explora o sistema usando intuição, experiência e curiosidade, tentando encontrar problemas que testes formais não capturam. É rápido, flexível e eficaz para descobertas iniciais — mas seus resultados dependem muito do conhecimento e criatividade de quem testa.

## Quando usar

- Quando precisa testar algo rapidamente antes de uma entrega ou demonstração
- Quando está explorando um sistema desconhecido pela primeira vez e quer uma impressão geral
- Quando não há tempo para planejar casos de teste formais no momento
- Quando quer complementar testes formais com exploração livre
- Quando um bug foi reportado e quer investigar a área ao redor sem roteiro fixo
- Quando quer "brincar" com o sistema como um usuário real faria

## Quando NÃO usar

- Quando quer exploração sistemática com heurísticas e registro estruturado → use `teste-exploratorio`
- Quando é a primeira validação de um novo build → use `teste-de-fumaca`
- Quando quer verificar se uma funcionalidade específica ainda funciona → use `teste-de-sanidade`
- Quando precisa de evidências documentadas para auditoria ou conformidade

## Como funciona — Processo Passo a Passo

**Passo 1: Contexto rápido**
Identifique o que foi construído ou alterado recentemente. Pergunte-se: onde estão as áreas de maior risco? Onde a implementação foi mais complexa? Que tipo de usuário vai usar isso?

**Passo 2: Identificar ponto de entrada**
Escolha por onde começar: a funcionalidade principal, a área mais nova ou a que "parece mais frágil". Não precisa de justificativa formal.

**Passo 3: Exploração livre**
Interaja com o sistema sem seguir um roteiro. Experimente: ações em ordem diferente da esperada, entradas inesperadas ou absurdas, duplos cliques, ações rápidas em sequência, dados em formatos inesperados, operações sem completar o fluxo.

**Passo 4: Seguir intuições**
Se algo "parece estranho" ou "poderia quebrar", explore mais fundo. Não ignore sensações de que algo está errado.

**Passo 5: Registrar achados**
Quando encontrar algo inesperado, anote rapidamente: o que fiz → o que aconteceu → o que esperava que acontecesse. Não precisa de formato formal — uma anotação rápida serve.

**Passo 6: Triagem dos achados**
Classifique o que encontrou: bug crítico (para tudo), comportamento estranho (investigar mais), melhoria de experiência (registrar para o backlog).

## Critérios de Qualidade

- A exploração foca nas áreas de maior risco ou maior novidade
- Bugs encontrados são registrados com informação suficiente para reprodução
- A exploração não é aleatória — há intenção em cada ação, mesmo sem script
- O testador usa perspectivas diferentes (usuário comum, usuário malicioso, usuário apressado)
- O tempo de exploração é produtivo: há achados ou confirmação de que a área está saudável

## Exemplo Conceitual

**Cenário:** Um formulário de cadastro de usuário foi modificado.

Exploração ad-hoc:
- Submeter o formulário com todos os campos vazios → o que acontece?
- Preencher apenas alguns campos e submeter → mensagens de erro são claras?
- Copiar e colar texto com caracteres especiais (emojis, acentos, `<script>`) no nome → sistema aceita?
- Clicar em "Cadastrar" múltiplas vezes rapidamente → cria duplicatas?
- Navegar para outra página no meio do preenchimento e voltar → os dados são preservados?
- Tentar cadastrar o mesmo e-mail duas vezes → sistema detecta duplicata?

Nenhum desses cenários precisa estar em um script formal — são intuições de exploração.

## Checklist de Conclusão

- [ ] Explorei as áreas de maior risco ou maior novidade do sistema?
- [ ] Tentei entradas inesperadas, absurdas ou em formatos incorretos?
- [ ] Anotei todos os comportamentos inesperados encontrados?
- [ ] Cada achado tem informação suficiente para ser reproduzido?
- [ ] Classifiquei os achados por severidade (crítico, estranho, melhoria)?
- [ ] Explorei perspectivas diferentes (usuário comum, apressado, curioso)?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-exploratorio` | Versão estruturada do ad-hoc | Quando quer sessão timeboxed com charter e heurísticas formais |
| `teste-de-fumaca` | Mais formal — valida o sistema inteiro | Quando quer verificar se o build está funcional com critério de pass/fail |
| `teste-de-sanidade` | Mais focado — uma funcionalidade específica | Quando sabe exatamente o que quer verificar |
