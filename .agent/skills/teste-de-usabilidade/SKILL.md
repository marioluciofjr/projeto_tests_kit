---
name: teste-de-usabilidade
description: >
  Guia o desenvolvedor ou designer na avaliação da facilidade de uso de uma interface, verificando
  se os usuários conseguem completar suas tarefas com eficiência, eficácia e satisfação. Use esta
  skill SEMPRE que o objetivo for avaliar a experiência do usuário, aplicar as heurísticas de
  Nielsen ou conduzir testes com usuários reais. Acione quando o usuário mencionar: "teste de
  usabilidade", "usability testing", "UX testing", "o usuário consegue usar o sistema", "teste
  com usuário real", "heurísticas de Nielsen", "avaliação heurística", "minha interface é
  intuitiva", "quero testar a experiência do usuário", "facilidade de uso", "o usuário trava em
  algum ponto?". Diferente do UAT (que valida critérios de aceitação de negócio), o teste de
  usabilidade foca na experiência e facilidade de uso. Agnóstico de plataforma (web, mobile,
  desktop).
categoria_ibm: Testes Não-Funcionais
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-de-aceitacao-do-usuario
  - teste-de-compatibilidade
---

# Teste de Usabilidade

## O que é

O teste de usabilidade avalia se os usuários conseguem usar o sistema de forma eficaz (completam as tarefas?), eficiente (com o mínimo de esforço?) e satisfatória (gostaram da experiência?). Pode ser feito com usuários reais executando tarefas, ou por especialistas avaliando contra as heurísticas de Nielsen. O objetivo é encontrar problemas de design e experiência antes que os usuários reais os encontrem em produção.

## Quando usar

- Quando quer verificar se a interface é intuitiva para o público-alvo
- Quando quer identificar onde os usuários travam ou ficam confusos
- Quando quer aplicar as 10 heurísticas de Nielsen como guia de avaliação
- Quando quer medir a taxa de sucesso de tarefas críticas
- Quando está iterando no design de uma nova funcionalidade
- Antes de lançar uma interface reformulada

## Quando NÃO usar

- Para validar critérios de aceitação de negócio (se o software faz o que foi pedido) → use `teste-de-aceitacao-do-usuario`
- Para testar funcionamento técnico → use testes funcionais
- Para avaliar compatibilidade entre dispositivos → use `teste-de-compatibilidade`

## Como funciona — Processo Passo a Passo

**Passo 1: Definir objetivos**
O que quer avaliar? Quais tarefas o usuário deve ser capaz de completar? Qual é o perfil do usuário testador? Quais critérios definem sucesso?

**Passo 2: Escolher a abordagem**
- **Avaliação Heurística:** 1-5 especialistas avaliam a interface contra as 10 heurísticas de Nielsen (sem usuário real — rápido e econômico)
- **Teste com Usuário:** usuário real executa tarefas enquanto é observado (mais válido, mais custoso)
- **Teste de Primeiro Clique:** onde o usuário clicaria para realizar uma tarefa? (avalia arquitetura de informação)

**Passo 3: Preparar tarefas (para teste com usuário)**
Escreva 5 a 8 tarefas realistas baseadas no uso real. Formato: "Você quer [objetivo do usuário]. Mostre-me como faria isso." Nunca inclua palavras que aparecem na interface — não dê dicas.

**Passo 4: As 10 Heurísticas de Nielsen (para avaliação heurística)**
1. Visibilidade do status do sistema
2. Correspondência entre o sistema e o mundo real
3. Controle e liberdade do usuário (desfazer, cancelar)
4. Consistência e padrões
5. Prevenção de erros
6. Reconhecimento em vez de memorização
7. Flexibilidade e eficiência de uso
8. Design estético e minimalista
9. Ajuda ao reconhecer, diagnosticar e recuperar de erros
10. Ajuda e documentação

**Passo 5: Executar**
Para teste com usuário: peça para "pensar em voz alta" durante a execução. Observe sem ajudar — onde trava? Onde clica errado? O que diz enquanto navega?

**Passo 6: Analisar e reportar**
Taxa de sucesso por tarefa (% que completaram). Problemas de usabilidade encontrados com severidade. Sugestões de melhoria priorizadas.

## Critérios de Qualidade

- Diferencia avaliação heurística (sem usuário) de teste com usuário (com usuário real)
- Tarefas escritas sem dar dicas — baseadas em objetivos, não em nomes de botões
- Problemas de usabilidade classificados por severidade (crítico, sério, menor)
- A taxa de sucesso das tarefas é medida (não apenas achados qualitativos)
- Resultados têm sugestões de melhoria priorizadas

## Exemplo Conceitual

**Tarefa:** "Você acabou de receber uma cobrança que não reconhece. Mostre-me como você contestaria esse valor no sistema."

O que observar durante a execução:
- Onde o usuário procura primeiro? (menu? busca? área pessoal?)
- Quanto tempo leva para encontrar a opção de contestação?
- O usuário comete algum erro no caminho? (clica em "Suporte" em vez de "Faturas")
- O usuário expressa frustração ou confusão verbalmente?

Problema encontrado: 70% dos usuários procuraram em "Suporte" em vez de "Financeiro" → label da seção está ambíguo.

Severidade: Sério — afeta diretamente a capacidade do usuário de contestar cobranças.

Sugestão: renomear a seção ou adicionar atalho em "Suporte" redirecionando para "Faturas".

## Checklist de Conclusão

- [ ] Defini as tarefas em formato de objetivo (não de instrução com dicas)?
- [ ] Escolhi a abordagem: avaliação heurística ou teste com usuário?
- [ ] Se avaliação heurística: avaliei contra as 10 heurísticas de Nielsen?
- [ ] Se teste com usuário: pedi para "pensar em voz alta" e observei sem ajudar?
- [ ] Medi a taxa de sucesso de cada tarefa?
- [ ] Classifiquei os problemas por severidade?
- [ ] Produzi sugestões de melhoria priorizadas?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-aceitacao-do-usuario` | Complementar — foco em critérios de negócio | Quando o usuário valida se a funcionalidade está correta (não se é fácil de usar) |
| `teste-de-compatibilidade` | Complementar — foco em dispositivos | Quando quer verificar se a interface funciona bem em diferentes dispositivos |
