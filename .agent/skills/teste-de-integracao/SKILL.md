---
name: teste-de-integracao
description: >
  Guia o desenvolvedor na validação da comunicação e do contrato entre dois ou mais módulos,
  serviços ou componentes que precisam trabalhar juntos. Use esta skill SEMPRE que o objetivo for
  verificar que módulos distintos se comunicam corretamente quando integrados, não de forma isolada.
  Acione quando o usuário mencionar: "teste de integração", "integration testing", "testar como
  dois módulos se comunicam", "validar a integração com o banco de dados", "testar a camada de
  serviço com o repositório", "meus módulos A e B precisam se comunicar", "testar a integração
  com uma API externa", "verificar o contrato entre componentes". Diferente de testes unitários
  (que isolam completamente) e de sistema (que testam o sistema todo), a integração foca na
  junção de partes específicas. Agnóstico de linguagem e framework.
categoria_ibm: Testes por Nível
nivel_maturidade: Intermediário
skills_relacionadas:
  - teste-de-API
  - teste-de-sistema
  - teste-de-caixa-branca
---

# Teste de Integração

## O que é

O teste de integração verifica que dois ou mais módulos, serviços ou componentes funcionam corretamente quando conectados entre si. Enquanto os testes unitários garantem que cada parte funciona isoladamente, os testes de integração garantem que as partes se comunicam com o contrato correto — enviando e recebendo os dados certos, tratando erros do parceiro e mantendo a integridade do sistema.

## Quando usar

- Quando dois ou mais módulos precisam se comunicar e quer validar essa comunicação
- Quando quer verificar que a camada de acesso a dados (repositório) se integra corretamente com o banco
- Quando integra com uma API externa e quer testar o comportamento real dessa integração
- Quando quer testar que uma fila de mensagens é processada corretamente entre produtor e consumidor
- Quando quer verificar que o contrato (interface) entre duas camadas arquiteturais está correto
- Após concluir testes unitários de todos os componentes envolvidos

## Quando NÃO usar

- Para testar lógica interna de um único módulo isolado → use testes unitários (agent-testes-de-unidade)
- Para testar o sistema completo de ponta a ponta → use `teste-de-sistema`
- Para testar apenas o contrato HTTP de uma API → use `teste-de-API`

## Como funciona — Processo Passo a Passo

**Passo 1: Mapear pontos de integração**
Liste quais módulos/serviços serão integrados. Para cada par: quem chama quem? Qual é o contrato (interface, tipos de dados)? O que um envia e o que o outro responde?

**Passo 2: Definir estratégia de integração**
- **Incremental Top-Down:** integre de cima para baixo na hierarquia, usando stubs para os módulos de baixo ainda não prontos
- **Incremental Bottom-Up:** integre de baixo para cima, usando drivers para simular os módulos de cima
- **Big Bang:** integre tudo de uma vez (arriscado — difícil de isolar a causa de falhas)
- Recomendação: incremental é sempre mais seguro

**Passo 3: Definir o que simular (mock/stub) vs. integrar de verdade**
Regra geral: integre de verdade os módulos que você controla. Simule serviços externos (APIs de terceiros, sistemas de pagamento, etc.) ou módulos ainda não implementados.

**Passo 4: Preparar o ambiente**
O que é necessário antes de rodar os testes? (banco de dados, serviços, dados de seed). Como garantir que o ambiente começa limpo? Como limpar após cada teste? (teardown)

**Passo 5: Criar casos de teste**
- Caminho feliz: os módulos se comunicam corretamente com dados válidos
- Falha no dependente: módulo A chama B, B está indisponível — A trata corretamente?
- Dados incorretos: A envia dados mal formados para B — B rejeita e A trata a rejeição?
- Timeout: B demora demais — A tem timeout configurado e trata adequadamente?

**Passo 6: Executar e analisar**
Execute em ambiente isolado (nunca em produção). Verifique logs de ambos os módulos. Confirme que o estado do sistema está correto após cada teste.

**Passo 7: Documentar**
Para cada caso: módulos envolvidos, cenário, entrada, comportamento esperado, resultado.

## Critérios de Qualidade

- Cada ponto de integração tem pelo menos um caso de caminho feliz
- Cenários de falha do módulo dependente são testados
- Setup e teardown são explícitos — sem estado compartilhado entre testes
- Decisão de mock vs. real está documentada com justificativa
- Testes nunca acessam banco ou serviços de produção

## Exemplo Conceitual

**Cenário:** Integração entre serviço de pedidos e serviço de notificações por e-mail.

| Caso | Cenário | Resultado esperado |
|------|---------|-------------------|
| Caminho feliz | Pedido criado com sucesso | Notificação é enviada com dados corretos do pedido |
| Serviço de e-mail indisponível | Pedido criado, mas notificação falha | Pedido é salvo, falha de notificação é logada — pedido não é cancelado |
| Dados de pedido incompletos | E-mail não tem campo de destinatário | Serviço de notificação rejeita e retorna erro descritivo |
| Timeout do serviço de e-mail | Serviço demora 30 segundos | Pedido não aguarda indefinidamente — timeout após 5 segundos, falha graciosamente |

## Checklist de Conclusão

- [ ] Listei quais módulos serão integrados no teste?
- [ ] Defini o que será testado de verdade vs. o que será simulado (mock/stub)?
- [ ] Tenho casos de caminho feliz para cada ponto de integração?
- [ ] Tenho casos de falha do módulo dependente?
- [ ] Defini setup e teardown (o ambiente começa limpo e é limpo após cada teste)?
- [ ] Os testes não acessam ambientes de produção?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-API` | Especialização — integração via HTTP | Quando o ponto de integração é uma API REST/GraphQL |
| `teste-de-sistema` | Nível acima — sistema completo | Quando todos os módulos já passaram nos testes de integração |
| `teste-de-caixa-branca` | Complementar — cobertura interna | Quando quer verificar os caminhos internos de cada módulo antes de integrá-los |
