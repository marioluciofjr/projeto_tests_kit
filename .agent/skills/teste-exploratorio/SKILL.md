---
name: teste-exploratorio
description: >
  Guia o desenvolvedor em sessões estruturadas de teste exploratório usando charters, heurísticas
  e timeboxing. Use esta skill SEMPRE que o objetivo for explorar sistematicamente uma funcionalidade
  em busca de problemas não cobertos por testes formais, usando técnicas como SFDPOT, HICCUPPS ou
  mnemonics de James Bach. Acione quando o usuário mencionar: "teste exploratório", "session-based
  testing", "teste com charter", "quero descobrir bugs que não sabia que existiam", "testar com
  heurísticas", "investigar essa funcionalidade profundamente", "exploração estruturada". Diferente
  do ad-hoc (completamente livre), o exploratório tem missão, tempo definido e registro. Adequado
  para qualquer nível, mas mais produtivo com alguma experiência prévia.
categoria_ibm: Testes Funcionais de Método
nivel_maturidade: Intermediário / Avançado
skills_relacionadas:
  - teste-ad-hoc
  - teste-de-usabilidade
  - teste-de-seguranca
---

# Teste Exploratório

## O que é

O teste exploratório é uma abordagem em que o design dos testes, a execução e o aprendizado acontecem simultaneamente, dentro de uma sessão com missão definida (charter), duração limitada (timebox) e registro estruturado. É sistemático — diferente do ad-hoc — mas flexível o suficiente para seguir intuições. O objetivo é descobrir problemas que especificações e testes planejados não capturam.

## Quando usar

- Quando quer explorar uma funcionalidade nova de forma aprofundada e sistemática
- Quando suspeita que há bugs escondidos que os testes formais não alcançam
- Quando quer complementar a suíte de testes automatizados com descobertas humanas
- Quando está investigando uma área após um bug crítico ser reportado
- Quando quer avaliar a qualidade geral antes de um release
- Quando há tempo definido para teste e quer maximizar o aprendizado no período

## Quando NÃO usar

- Quando quer exploração completamente livre, sem registro → use `teste-ad-hoc`
- Quando já sabe exatamente o que quer testar com script predefinido → use a skill específica
- Quando quer validar critérios de aceitação com o cliente → use `teste-de-aceitacao-do-usuario`

## Como funciona — Processo Passo a Passo

**Passo 1: Definir o charter**
Formato: "Explorar [área] para encontrar [tipo de problema] usando [heurística/recurso]."
Exemplo: "Explorar o fluxo de cadastro para encontrar falhas de validação usando heurísticas de EXTREMOS."

**Passo 2: Timeboxing**
Defina a duração: geralmente 60 a 90 minutos. Sessões mais longas perdem foco.

**Passo 3: Escolher heurísticas**
- **SFDPOT:** Structure, Function, Data, Platform, Operations, Time
- **CRUD:** Criar, Ler, Atualizar, Deletar cada entidade
- **Extremos:** zero, um, muitos, máximo, mínimo, nulo, caracteres especiais
- **Interrupções:** cancele no meio de uma operação, perca a conexão, feche e reabra

**Passo 4: Executar**
Explore seguindo as heurísticas. Divida o tempo: ~40% execução, ~40% investigação de achados, ~20% anotações.

**Passo 5: Registrar em tempo real**
Anote enquanto explora: ação → comportamento observado → esperado → é bug?

**Passo 6: Debriefing**
Ao fim: o charter foi cumprido? Que bugs foram encontrados? O que ficou sem testar?

**Passo 7: Session report**
Documente: charter, duração, áreas cobertas, bugs com steps de reprodução, próxima sessão.

## Critérios de Qualidade

- A sessão tem charter claro antes de começar
- Duração timeboxed (máximo 90 minutos)
- Pelo menos uma heurística seguida durante a exploração
- Bugs registrados com steps de reprodução durante a sessão
- Debriefing identifica o que ficou sem testar
- Session report produzido ao final

## Exemplo Conceitual

**Charter:** "Explorar autenticação para encontrar comportamentos inesperados com credenciais incomuns. 60 minutos."

Heurística EXTREMOS aplicada:
- Senha de 1 caractere, senha de 1000 caracteres, senha com apenas espaços
- E-mail sem @, e-mail com múltiplos @, campo vazio, caracteres especiais

Heurística INTERRUPÇÕES:
- Clicar em "Login" antes de preencher todos os campos
- Abrir o link de "recuperar senha" em outra sessão/dispositivo

## Checklist de Conclusão

- [ ] Defini um charter claro antes de começar?
- [ ] Defini uma duração máxima (timebox)?
- [ ] Escolhi pelo menos uma heurística para guiar a exploração?
- [ ] Registrei os achados durante (não só no final)?
- [ ] Fiz debriefing: charter cumprido? O que ficou sem testar?
- [ ] Produzi session report com bugs e próximos passos?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-ad-hoc` | Versão livre, sem estrutura | Quando quer exploração sem compromisso de charter |
| `teste-de-usabilidade` | Complementar — foco em experiência do usuário | Quando quer avaliar facilidade de uso |
| `teste-de-seguranca` | Complementar — heurísticas de segurança | Quando o charter foca em vulnerabilidades |
