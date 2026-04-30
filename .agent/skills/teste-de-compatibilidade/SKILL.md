---
name: teste-de-compatibilidade
description: >
  Guia o desenvolvedor na validação do comportamento do sistema em diferentes navegadores, sistemas
  operacionais, dispositivos e versões de dependências. Use esta skill SEMPRE que o objetivo for
  garantir que o sistema funciona corretamente para usuários em diferentes ambientes. Acione quando
  o usuário mencionar: "teste de compatibilidade", "compatibility testing", "cross-browser",
  "testar em diferentes browsers", "testar em diferentes sistemas operacionais", "funciona no
  Safari, Firefox, IE?", "compatível com mobile", "responsivo?", "testar em diferentes versões
  da dependência", "backward compatibility", "funciona no Android? No iOS?", "testar em telas
  diferentes". Diferente dos testes funcionais (que verificam o comportamento) e de usabilidade
  (que verificam a experiência), a compatibilidade verifica se o mesmo comportamento correto
  ocorre em todos os ambientes suportados.
categoria_ibm: Testes Não-Funcionais
nivel_maturidade: Intermediário
skills_relacionadas:
  - teste-de-sistema
  - teste-de-usabilidade
---

# Teste de Compatibilidade

## O que é

O teste de compatibilidade verifica que o sistema funciona corretamente em diferentes combinações de navegadores, sistemas operacionais, dispositivos e versões de dependências. O objetivo é garantir que todos os usuários — independentemente do ambiente que usam — tenham a mesma experiência funcional e visual correta.

## Quando usar

- Quando o sistema tem usuários em múltiplos navegadores (Chrome, Firefox, Safari, Edge)
- Quando o sistema precisa funcionar em dispositivos móveis além de desktop
- Quando a base de usuários usa diferentes sistemas operacionais
- Quando quer definir formalmente quais combinações são suportadas (matriz de suporte)
- Antes de lançamentos de grandes atualizações de interface

## Quando NÃO usar

- Para testar funcionalidade (se funciona) — garanta isso primeiro com testes funcionais
- Para avaliar a experiência do usuário — use `teste-de-usabilidade`
- Para verificar desempenho em diferentes ambientes — use `teste-de-desempenho`

## Como funciona — Processo Passo a Passo

**Passo 1: Definir a matriz de compatibilidade**
Liste os ambientes que precisam ser suportados:
- **Navegadores:** Chrome (versão mínima), Firefox, Safari, Edge — com versões mínimas
- **Sistemas Operacionais:** Windows, macOS, Linux, Android, iOS
- **Dispositivos:** Desktop (1920x1080, 1366x768), Tablet (768px), Mobile (375px, 414px)
- **Versões de dependências:** versões mínimas e máximas suportadas das principais bibliotecas

**Passo 2: Priorizar combinações**
Identifique quais combinações são mais usadas pelo seu público-alvo (use analytics se disponível). Foque em: combinações de alto uso, combinações com histórico de problemas.

**Passo 3: Definir os fluxos a testar**
Para cada combinação prioritária, teste os fluxos críticos do sistema — não todas as funcionalidades, mas as principais.

**Passo 4: Criar casos de compatibilidade**
Para cada combinação prioritária: executar os fluxos críticos. Verificar: renderização visual correta, funcionalidade completa, desempenho aceitável, responsividade em diferentes tamanhos de tela.

**Passo 5: Registrar problemas**
Para cada problema: combinação afetada | componente | comportamento esperado | comportamento real | screenshot.

**Passo 6: Classificar por prioridade**
- Combinações de alto uso com problema → alta prioridade (corrigir antes do release)
- Combinações de uso médio com problema → média prioridade
- Combinações raras com problema → baixa prioridade (documentar como limitação conhecida)

**Passo 7: Publicar a matriz de suporte**
Defina oficialmente: quais combinações são garantidas (suportadas), quais são "best effort" e quais não são suportadas.

## Critérios de Qualidade

- Matriz de compatibilidade definida antes de executar os testes
- Priorização por frequência de uso (não todas as combinações têm o mesmo peso)
- Dispositivos móveis incluídos além de desktop
- Problemas documentados com screenshot e combinação específica
- Matriz de suporte oficial publicada ao final

## Exemplo Conceitual

**Matriz de compatibilidade de uma aplicação web (priorizada):**

| Prioridade | Navegador | SO | Dispositivo | Status |
|-----------|-----------|-----|-------------|--------|
| Alta | Chrome 120+ | Windows 10 | Desktop 1920x1080 | ✅ Suportado |
| Alta | Chrome 120+ | macOS 13+ | Desktop | ✅ Suportado |
| Alta | Safari 17+ | iOS 16+ | Mobile (iPhone 14) | ⚠️ Testar |
| Alta | Chrome Mobile | Android 13 | Mobile | ⚠️ Testar |
| Média | Firefox 120+ | Windows 10 | Desktop | ✅ Suportado |
| Média | Edge 120+ | Windows 10 | Desktop | ✅ Suportado |
| Baixa | Safari | macOS | Desktop | Best effort |
| — | Internet Explorer | qualquer | qualquer | ❌ Não suportado |

**Problema encontrado:** Botão de "Enviar" não aparece corretamente no Safari/iOS com tela de 375px.

Classificação: Alta prioridade (combinação de alto uso).

## Checklist de Conclusão

- [ ] Defini a matriz de compatibilidade (navegadores, SOs, dispositivos) antes de testar?
- [ ] Priorizei as combinações por frequência de uso do meu público-alvo?
- [ ] Incluí dispositivos móveis além de desktop?
- [ ] Testei os fluxos críticos em cada combinação prioritária?
- [ ] Documentei problemas com screenshot e combinação específica?
- [ ] Publiquei (ou defini) a matriz de suporte oficial?

## Skills Relacionadas

| Skill | Relação | Quando preferir aquela |
|-------|---------|------------------------|
| `teste-de-sistema` | Pré-requisito — funcionalidade garantida antes da compatibilidade | Garanta que o sistema funciona antes de testar em múltiplos ambientes |
| `teste-de-usabilidade` | Complementar — foco em experiência | Quando quer avaliar se a interface é fácil de usar nos dispositivos |
