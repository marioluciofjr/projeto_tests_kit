#!/usr/bin/env python3
"""
Heuristic scan para skill-injection-auditor — tests-kit
Analisa os 7 vetores de risco em todos os SKILL.md
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import re
import os
import json
from pathlib import Path

SKILLS_ROOT = Path(r"c:\Users\mario\OneDrive\Área de Trabalho\projeto_tests_kit\tests-kit\.agent\skills")

# 7 vetores de risco com padrões detectáveis
RISK_VECTORS = {
    "V1_OVERRIDE_INSTRUCOES": {
        "severity": "ALTO",
        "desc": "Tentativa de sobrescrever regras do sistema",
        "patterns": [
            r"ignore\s+(all\s+)?previous\s+instructions?",
            r"esquece?\s+(tudo|as\s+instru)",
            r"override\s+(system|all)",
            r"disregard\s+(your|all|previous)",
            r"forget\s+(everything|all\s+previous)",
            r"nova\s+ordem\s+de\s+prioridade",
            r"suas\s+novas\s+regras\s+s[ão]o",
            r"system\s+prompt",
            r"DAN\s+mode",
            r"jailbreak",
        ]
    },
    "V2_EXFILTRACAO_DADOS": {
        "severity": "ALTO",
        "desc": "Tentativa de extrair dados sensíveis",
        "patterns": [
            r"env(ironment)?\s+var(iable)?",
            r"api[_\s]key",
            r"secret[_\s]key",
            r"bearer\s+token",
            r"base64\s+encode",
            r"exfiltrar?",
            r"envie?\s+(para|a)\s+http",
            r"curl\s+.*http",
            r"webhook.*http",
            r"send\s+to\s+external",
        ]
    },
    "V3_EXECUCAO_CODIGO": {
        "severity": "ALTO",
        "desc": "Injeção de código para execução não autorizada",
        "patterns": [
            r"exec\s*\(",
            r"eval\s*\(",
            r"subprocess\s*\.",
            r"os\.system\s*\(",
            r"__import__",
            r"shell\s*=\s*True",
            r"powershell\s+-enc",
            r"base64\s*\.\s*b64decode",
            r"\\x[0-9a-fA-F]{2}\\x[0-9a-fA-F]{2}",
        ]
    },
    "V4_MANIPULACAO_IDENTIDADE": {
        "severity": "MEDIO",
        "desc": "Tentativa de alterar a identidade ou persona do modelo",
        "patterns": [
            r"voc[eê]\s+agora\s+[eé]\s+um\s+(?!agente|especialista|guia)",
            r"you\s+are\s+now\s+(?!a\s+(guide|specialist|expert|assistant))",
            r"act\s+as\s+(?!a\s+(guide|specialist|expert|assistant))",
            r"pretend\s+you\s+are",
            r"fingir?\s+ser",
            r"personagem\s+malicioso",
            r"sem\s+restrições\s+[eé]ticas",
            r"ignore\s+your\s+training",
        ]
    },
    "V5_INSTRUCAO_OCULTA": {
        "severity": "MEDIO",
        "desc": "Instruções ocultas ou obfuscadas",
        "patterns": [
            r"<!--.*instrução.*-->",
            r"\[//\]:\s*#",
            r"<!-{2,}.*ignore.*-{2,}>",
            r"&lt;.*instrução.*&gt;",
            r"zero\s+width",
            r"​",  # zero-width space U+200B
            r"\u200b|\u200c|\u200d|\ufeff",
        ]
    },
    "V6_RECURSIVIDADE_MALICIOSA": {
        "severity": "MEDIO",
        "desc": "Tentativa de chamar outras skills de forma não declarada",
        "patterns": [
            r"execute\s+skill",
            r"activate\s+skill",
            r"carregar\s+skill(?!\s+relacionada)",
            r"chamar\s+automaticamente\s+(?!a\s+skill)",
            r"auto[_\-]execute",
            r"self[_\-]replicate",
        ]
    },
    "V7_ESCOPO_FORA_LIMITES": {
        "severity": "BAIXO",
        "desc": "Instruções que extrapolam o escopo de uma skill de testes",
        "patterns": [
            r"faça?\s+compras?",
            r"acesse?\s+minha\s+conta",
            r"transfira?\s+dinheiro",
            r"delete?\s+(?:todos?\s+os?\s+)?arquivo",
            r"formata?\s+(o\s+)?disco",
            r"rm\s+-rf",
            r"drop\s+table",
        ]
    }
}

def scan_skill(skill_path: Path) -> dict:
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return {"error": f"SKILL.md não encontrado em {skill_path}"}

    content = skill_md.read_text(encoding="utf-8", errors="ignore")
    content_lower = content.lower()

    results = {
        "skill": skill_path.name,
        "file": str(skill_md),
        "size_lines": len(content.splitlines()),
        "findings": [],
        "risk_score": 0,
        "verdict": "SEGURO"
    }

    for vector_id, vector in RISK_VECTORS.items():
        for pattern in vector["patterns"]:
            matches = list(re.finditer(pattern, content_lower, re.IGNORECASE))
            if matches:
                for m in matches:
                    # Pegar contexto ao redor do match
                    start = max(0, m.start() - 40)
                    end = min(len(content), m.end() + 40)
                    ctx = content[start:end].replace('\n', ' ').strip()
                    results["findings"].append({
                        "vector": vector_id,
                        "severity": vector["severity"],
                        "desc": vector["desc"],
                        "pattern": pattern,
                        "context": ctx
                    })
                    if vector["severity"] == "ALTO":
                        results["risk_score"] += 30
                    elif vector["severity"] == "MEDIO":
                        results["risk_score"] += 10
                    else:
                        results["risk_score"] += 3

    # Checar também arquivos auxiliares (se existirem)
    for extra in skill_path.rglob("*"):
        if extra != skill_md and extra.is_file():
            try:
                extra_content = extra.read_text(encoding="utf-8", errors="ignore")
                for vector_id, vector in RISK_VECTORS.items():
                    for pattern in vector["patterns"]:
                        if re.search(pattern, extra_content, re.IGNORECASE):
                            results["findings"].append({
                                "vector": vector_id,
                                "severity": vector["severity"],
                                "desc": vector["desc"],
                                "pattern": f"[{extra.name}] {pattern}",
                                "context": f"Encontrado em arquivo auxiliar: {extra.name}"
                            })
            except:
                pass

    # Determinar veredicto
    if results["risk_score"] >= 30:
        results["verdict"] = "MALICIOSO"
    elif results["risk_score"] >= 10:
        results["verdict"] = "SUSPEITO"
    else:
        results["verdict"] = "SEGURO"

    return results

def main():
    print("=" * 60)
    print("  AUDITORIA DE SEGURANÇA — tests-kit")
    print("  skill-injection-auditor heuristic scan")
    print("=" * 60)
    print()

    all_results = []
    skills = sorted([d for d in SKILLS_ROOT.iterdir() if d.is_dir()])

    for skill_dir in skills:
        result = scan_skill(skill_dir)
        all_results.append(result)

    # Relatório por skill
    safe_count = 0
    suspect_count = 0
    malicious_count = 0

    for r in all_results:
        verdict_emoji = {"SEGURO": "✅", "SUSPEITO": "⚠️", "MALICIOSO": "🚨"}.get(r.get("verdict",""), "?")
        print(f"{verdict_emoji} {r['skill']}")
        if r.get("findings"):
            for f in r["findings"]:
                print(f"   [{f['severity']}] {f['vector']}: {f['desc']}")
                print(f"   Contexto: ...{f['context']}...")
        else:
            print(f"   → Nenhum vetor de risco detectado | {r['size_lines']} linhas")
        print()

        v = r.get("verdict", "SEGURO")
        if v == "SEGURO": safe_count += 1
        elif v == "SUSPEITO": suspect_count += 1
        else: malicious_count += 1

    print("=" * 60)
    print(f"  RESUMO FINAL")
    print(f"  Total skills auditadas: {len(all_results)}")
    print(f"  ✅ SEGURO:    {safe_count}")
    print(f"  ⚠️  SUSPEITO:  {suspect_count}")
    print(f"  🚨 MALICIOSO: {malicious_count}")
    print("=" * 60)

    if suspect_count == 0 and malicious_count == 0:
        print("\n  🎉 TODAS AS SKILLS APROVADAS — Kit limpo e seguro.")
    else:
        print("\n  ⚠️  REVISAR SKILLS SUSPEITAS OU MALICIOSAS ANTES DO USO.")

    # Salvar JSON
    output_path = Path(r"c:\Users\mario\OneDrive\Área de Trabalho\projeto_tests_kit") / "_reversa_sdd" / "audit-report.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"\n  Relatório JSON salvo em: {output_path}")

if __name__ == "__main__":
    main()
