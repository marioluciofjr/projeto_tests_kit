---
name: teste-de-fumaca
description: >
  Guia o desenvolvedor em uma verificação rápida e superficial do sistema como um todo para
  determinar se um novo build ou deploy foi bem-sucedido e se as funcionalidades críticas básicas
  respondem. Use esta skill SEMPRE que o objetivo for determinar se vale a pena avançar para testes
  mais profundos ou se o build está quebrado. Acione quando o usuário mencionar: "teste de fumaça",
  "smoke test", "smoke testing", "o sistema subiu?", "o deploy funcionou?", "validar o build",
  "checar se está de pé", "build verification test", "preciso saber se o sistema básico está ok
  antes de testar mais". Diferente da sanidade (uma feature específica) e da regressão (abrangente),
  a fumaça cobre o sistema inteiro de forma superficial — só caminho feliz — e deve terminar em
  menos de 15 minutos. Resultado é binário: PASSA (avança) ou FALHA (para).
categoria_ibm: Testes Funcionais de Método
nivel_maturidade: Todos os níveis
skills_relacionadas:
  - teste-de-sanidade
  - teste-de-regressao
---

# Teste de Fumaça

## O que é

O teste de fumaça (smoke test) é uma verificação rápida e superficial das funcionalidades críticas do sistema após um novo build ou deploy. O nome vem da eletrônica: ao ligar um novo circuito, o primeiro sinal de que algo está errado é a fumaça. Analogamente, o smoke test identifica problemas óbvios antes de investir tempo em testes mais profundos. Se o smoke test falhar, para tudo — o build está quebrado.

## Quando usar

- Logo após um novo build ou deploy para qualquer ambiente
- Antes de iniciar qualquer suíte de testes mais profunda
- Quando quer confirmar rapidamente que o sistema básico está operacional
- Como validação automática em pipelines de CI/CD (gate de qualidade)
- Após restauração de backup ou migração de ambiente

## Quando NÃO usar

- Para validar uma funcionalidade específica → use `teste-de-sanidade`
- Para garantir que nada quebrou após uma mudança → use `teste-de-regressao`
- Para testar casos de borda, cenários negativos ou edge cases (smoke é apenas caminho feliz)

## Como funciona — Processo Passo a Passo

**Passo 1: Identificar funcionalidades críticas**
O que é ESSENCIAL para o sistema funcionar? Liste no máximo 10 itens. Exemplos: a aplicação carrega, o login funciona, a operação principal responde, o banco de dados conecta, a home page renderiza.

**Passo 2: Um caso de teste por funcionalidade**
Para cada item crítico: defina APENAS o caminho feliz. Um caso, uma verificação, sem variações.

**Passo 3: Montar a suíte**
A suíte completa deve ser executável em menos de 15 minutos. Se demorar mais, está grande demais para smoke.

**Passo 4: Executar**
Execute em ordem. Automação é preferível, mas execução manual é aceitável.

**Passo 5: Decisão imediata**
- Todos passaram → sistema está "vivo" → avance para testes mais profundos
- **Qualquer falha → PARE.** O build está quebrado. Reporte antes de qualquer outra ação.

**Passo 6: Registrar**
Registre: data, versão do build, resultado (PASS/FAIL), lista de falhas se houver.

## Critérios de Qualidade

- Suíte completa executável em menos de 15 minutos
- No máximo 10 a 15 casos de teste por suíte
- Cada caso testa APENAS o caminho feliz (zero casos de borda)
- Resultado é binário e claro: PASS ou FAIL
- Qualquer falha suspende imediatamente a progressão para testes mais profundos

## Exemplo Conceitual

**Suíte de fumaça de uma aplicação web de e-commerce:**

| # | Funcionalidade crítica | Verificação |
|---|----------------------|-------------|
| 1 | Aplicação carrega | Home page responde em menos de 3 segundos |
| 2 | Login funciona | Usuário de teste consegue autenticar |
| 3 | Catálogo carrega | Página de produtos lista pelo menos 1 produto |
| 4 | Busca funciona | Buscar "produto" retorna resultados |
| 5 | Carrinho funciona | Adicionar 1 produto ao carrinho funciona |
| 6 | Checkout inicia | Clicar em "Finalizar compra" abre o fluxo |
| 7 | API de pagamento responde | Endpoint de saúde da integração retorna 200 |

Tempo estimado: 8 minutos.
Resultado esperado: todos os 7 casos passam → sistema pronto para testes aprofundados.

## Checklist de Conclusão

- [ ] Listei apenas as funcionalidades CRÍTICAS do sistema (máximo 10-15)?
- [ ] Cada caso testa apenas o caminho feliz (zero variações ou casos de borda)?
- [ ] A suíte inteira é executável em menos de 15 minutos?
- [ ] O resultado é binário — PASS (avança) ou FAIL (para)?
- [ ] Se qualquer caso falhou, parei e reportei antes de avançar para outros testes?
- [ ] Registrei: data, versão do build, resultado e falhas encontradas?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-sanidade` | Mais focado — uma funcionalidade específica | Quando quer verificar uma feature específica, não o sistema todo |
| `teste-de-regressao` | Mais abrangente — funcionalidades afetadas por mudança | Quando quer garantir que nada quebrou, não apenas que o sistema está de pé |
