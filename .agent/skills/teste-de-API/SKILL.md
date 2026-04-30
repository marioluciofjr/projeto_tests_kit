---
name: teste-de-API
description: >
  Guia o desenvolvedor na validação completa de APIs — contratos, endpoints, payloads, autenticação,
  códigos de status HTTP e comportamento sob condições de erro. Use esta skill SEMPRE que o objetivo
  for testar interfaces de programação de aplicações, independentemente da ferramenta (Postman, curl,
  código, insomnia ou qualquer HTTP client). Acione quando o usuário mencionar: "testar API",
  "teste de API", "API testing", "validar endpoints", "testar REST", "testar GraphQL", "testar
  contrato de API", "verificar se a API está retornando certo", "testar autenticação da API",
  "testar headers", "criar coleção de testes para minha API", "como testar meus endpoints".
  Não confundir com teste de integração (que testa comunicação entre módulos internos) — esta skill
  foca especificamente em interfaces HTTP. Agnóstica de linguagem e ferramenta.
categoria_ibm: Testes Funcionais de Método
nivel_maturidade: Intermediário
skills_relacionadas:
  - teste-de-caixa-preta
  - teste-de-integracao
  - teste-de-seguranca
---

# Teste de API

## O que é

O teste de API valida que uma interface de programação de aplicações (API) se comporta conforme especificado — aceitando as entradas corretas, retornando as saídas esperadas, protegendo recursos com autenticação adequada e comunicando erros de forma clara e padronizada. É uma forma de teste de caixa preta aplicada especificamente ao contrato de uma API, seja ela REST, GraphQL, RPC ou qualquer outro estilo.

## Quando usar

- Quando quer validar que seus endpoints retornam os dados e status codes corretos
- Quando quer verificar se a autenticação e autorização estão funcionando corretamente
- Quando quer criar um conjunto de testes automatizáveis para sua API
- Quando precisa validar que a API está seguindo o contrato definido (OpenAPI/Swagger)
- Quando integra com uma API de terceiros e quer verificar o comportamento antes de usar
- Quando faz uma mudança na API e quer garantir que o contrato não foi quebrado
- Quando quer testar o comportamento da API com dados inválidos ou malformados

## Quando NÃO usar

- Quando quer testar a comunicação entre módulos internos (não expostos como API) → use `teste-de-integracao`
- Quando quer testar apenas a interface visual do usuário → use `teste-de-sistema`
- Quando quer fazer um teste de segurança profundo (pentest) → use `teste-de-seguranca`

## Como funciona — Processo Passo a Passo

**Passo 1: Mapeamento de endpoints**
Liste todos os endpoints a testar. Agrupe por recurso (ex: `/usuarios`, `/produtos`, `/pedidos`). Para cada endpoint, anote: método HTTP (GET, POST, PUT, DELETE, PATCH), path, parâmetros esperados e body format.

**Passo 2: Testes de contrato básico (caminho feliz)**
Para cada endpoint: envie uma requisição válida e verifique que o status code está correto, a estrutura do response está conforme esperado e os campos obrigatórios estão presentes.

**Passo 3: Testes de autenticação**
- Sem token/credencial → deve retornar 401 Unauthorized
- Token expirado → deve retornar 401
- Token inválido → deve retornar 401
- Token de outro usuário tentando acessar recurso privado → deve retornar 403 Forbidden
- Token válido com permissão correta → deve retornar 200 (ou o código esperado)

**Passo 4: Testes de validação de input**
- Campos obrigatórios ausentes → deve retornar 400 ou 422
- Tipos de dados incorretos (string onde espera número) → deve retornar 400 ou 422
- Valores fora dos limites (strings muito longas, números negativos) → comportamento definido
- Payload completamente vazio → deve retornar 400
- Payload com JSON malformado → deve retornar 400

**Passo 5: Testes de erro e não encontrado**
- Recurso inexistente → deve retornar 404 Not Found
- Método HTTP não suportado naquele endpoint → deve retornar 405 Method Not Allowed
- Corpo da requisição em formato incorreto (ex: XML quando espera JSON) → 415 ou 400

**Passo 6: Testes de idempotência (quando aplicável)**
- PUT/PATCH: chamar duas vezes com os mesmos dados deve produzir o mesmo resultado
- DELETE: chamar duas vezes no mesmo recurso — segunda deve retornar 404 (recurso já removido)
- POST: chamar duas vezes — cria duplicata ou retorna erro de conflito (409)?

**Passo 7: Documentação dos casos**
Consolide: endpoint | método | cenário | input | status esperado | campos esperados no body de resposta.

## Critérios de Qualidade

- Pelo menos 1 caso de caminho feliz por endpoint
- Todos os cenários de autenticação testados (sem token, expirado, inválido, válido)
- Validação de input para todos os campos obrigatórios e com restrições
- Códigos de erro cobertos com o comportamento esperado documentado
- Casos de teste são independentes (não dependem de estado gerado por outro teste)
- A estrutura do response (campos e tipos) é verificada, não apenas o status code

## Exemplo Conceitual

**Cenário:** Endpoint `POST /pedidos` — cria um novo pedido.

| Caso | Método | Input | Status esperado | Verificação adicional |
|------|--------|-------|----------------|----------------------|
| Caminho feliz | POST | pedido válido com todos os campos | 201 Created | body retorna o pedido criado com `id` |
| Campo obrigatório ausente | POST | sem campo `produto_id` | 422 | body contém mensagem de erro descritiva |
| Usuário não autenticado | POST | sem token | 401 | body contém erro de autenticação |
| Usuário sem permissão | POST | token de cliente tentando criar como admin | 403 | acesso negado |
| ID de produto inexistente | POST | `produto_id: "xyz-inexistente"` | 404 | body indica que produto não existe |

## Checklist de Conclusão

- [ ] Listei todos os endpoints a testar antes de criar casos?
- [ ] Testei autenticação: sem token, token inválido, token expirado, token sem permissão?
- [ ] Testei campos obrigatórios ausentes e tipos de dados incorretos?
- [ ] Cobri os status codes: 200, 201, 400, 401, 403, 404, 422?
- [ ] Verifiquei a estrutura do body de resposta (campos e tipos), não só o status code?
- [ ] Os casos de teste são agnósticos de ferramenta (funcionam com qualquer HTTP client)?
- [ ] Casos de teste são independentes entre si?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-caixa-preta` | Base teórica — esta skill é caixa preta aplicada a APIs | Quando quer a técnica genérica sem foco em HTTP |
| `teste-de-integracao` | Complementar — quando a API é parte de uma integração maior | Quando quer testar o fluxo completo entre módulos que usam a API |
| `teste-de-seguranca` | Extensão — testes de segurança mais profundos na API | Quando quer ir além dos cenários de autenticação básica |
