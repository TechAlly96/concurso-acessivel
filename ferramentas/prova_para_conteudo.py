#!/usr/bin/env python3
"""Concurso Acessivel - transforma um banco de questoes (bancos/*.json)
em partes de conteudo (conteudo/*.md) no formato que o gerador narra.

Cada eixo da prova vira uma parte. Cada questao vira um capitulo com:
o texto de apoio (quando houver), o enunciado completo, as alternativas,
a explicacao e a resposta. O texto e ajustado para a voz ler direito
(graus Celsius, numeros de lei, formulas do Excel, simbolos).

Somente biblioteca padrao (roda no Termux e no GitHub).
Uso: python3 ferramentas/prova_para_conteudo.py bancos/pcmg-tpag-2026.json"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONTEUDO = RAIZ / "conteudo"

# Cada eixo vira uma parte. Prefixo 9x = provas anteriores (ver INFO no montar_dados.py).
EIXOS = {
    "geral": ("91", "Eixo geral, questões 1 a 15: Língua Portuguesa, Informática e Raciocínio Lógico"),
    "legislacao": ("92", "Eixo legislação, questões 16 a 30: Direitos Humanos e Legislação"),
    "especifico": ("93", "Eixo específico, questões 31 a 60: Auxiliar de Necropsia e Biossegurança"),
}

def celula_falada(ref):
    """B$1 -> 'B cifrão 1'; $A2 -> 'cifrão A 2' (o aluno precisa ouvir cada cifrão)."""
    m = re.fullmatch(r"(\$?)([A-Z]{1,2})(\$?)(\d+)", ref)
    partes = (["cifrão"] if m[1] else []) + [m[2]] + (["cifrão"] if m[3] else []) + [m[4]]
    return " ".join(partes)


def formula_falada(m):
    corpo = m.group(1)
    corpo = re.sub(r"\$?[A-Z]{1,2}\$?\d+", lambda r: celula_falada(r.group(0)), corpo)
    return "igual, " + corpo.replace("*", ", vezes ")


def para_voz(t):
    """Ajusta o texto para a voz Piper ler corretamente."""
    t = re.sub(r"=((?:\$?[A-Z]{1,2}\$?\d+\*?)+)", formula_falada, t)
    t = re.sub(r"\b\$?[A-Z]{1,2}\$\d+\b|\$[A-Z]{1,2}\$?\d+\b", lambda r: celula_falada(r.group(0)), t)
    t = t.replace("−", "menos ")
    t = re.sub(r"(\d)\s*°C", r"\1 graus Celsius", t)
    t = re.sub(r"\bn\.º\s*", "número ", t)
    t = re.sub(r"\bart\.\s*(\d+)\.º", r"artigo \1º", t)
    t = re.sub(r"\bart\.\s*", "artigo ", t)
    # Numero de lei: 5.406/1969 -> 5406, de 1969 (a voz nao le ponto de milhar nem barra)
    t = re.sub(r"\b(\d{1,3})\.(\d{3})/(\d{4})\b", r"\1\2, de \3", t)
    t = re.sub(r"\b(\d{1,4})/(\d{4})\b", r"\1, de \2", t)
    t = t.replace("(ex.:", "(por exemplo,").replace("ex.:", "por exemplo,")
    t = t.replace("CF", "Constituição Federal").replace("Constituição Federal de 1988 (Constituição Federal)", "Constituição Federal de 1988")
    t = t.replace("IML", "I M L").replace("EPI", "E P I").replace("OMS", "O M S")
    t = t.replace("PCMG", "P C M G").replace("RSS", "R S S").replace("UV", "U V")
    t = t.replace("TI ", "T I ").replace("DNA", "D N A")
    t = t.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("’", "'")
    return t


def sem_resposta_final(explicacao):
    """A explicacao termina com 'Resposta: X.'; a resposta vai em linha propria."""
    return re.sub(r"\s*Resposta: [A-D]\.?\s*$", "", explicacao).strip()


def questao_md(q, textos):
    linhas = [f"## Questão {q['numero']}. {para_voz(q['tema'])}", ""]
    linhas += [f"**Disciplina.** {q['disciplina']}.", ""]
    if q.get("texto_ref") and q["numero"] == min(
            x for x in textos["_primeira"].get(q["texto_ref"], [q["numero"]])):
        linhas += [f"**O texto de apoio.** Esta questão e as próximas usam o texto {q['texto_ref']}. Ouça com atenção.", ""]
        for par in textos[q["texto_ref"]]["conteudo"].split("\n\n"):
            linhas += [para_voz(par), ""]
    elif q.get("texto_ref"):
        linhas += [f"**O texto de apoio.** Esta questão usa o mesmo texto {q['texto_ref']}, lido na questão {min(textos['_primeira'][q['texto_ref']])}.", ""]
    linhas += [f"**O enunciado.** {para_voz(q['enunciado'])}", ""]
    if q.get("figura_descricao"):
        linhas += [para_voz(q["figura_descricao"]), ""]
    linhas += ["**As alternativas.**", ""]
    for letra in "ABCD":
        alt = para_voz(q["alternativas"][letra]).rstrip(".")
        linhas += [f"Letra {letra}: {alt}.", ""]
    linhas += ["Pense na sua resposta antes de ouvir a explicação.", ""]
    linhas += [f"**A explicação.** {para_voz(sem_resposta_final(q['explicacao']))}", ""]
    certa = para_voz(q["alternativas"][q["gabarito"]]).rstrip(".")
    linhas += [f"**Resposta: letra {q['gabarito']}, {certa[:1].lower() + certa[1:]}.**", "", "---", ""]
    return linhas


def main(banco):
    d = json.loads(Path(banco).read_text(encoding="utf-8"))
    c = d["concurso"]
    textos = dict(d.get("textos", {}))
    primeira = {}
    for q in d["questoes"]:
        if q.get("texto_ref"):
            primeira.setdefault(q["texto_ref"], []).append(q["numero"])
    textos["_primeira"] = primeira
    ano = c["data_prova"][:4]
    CONTEUDO.mkdir(exist_ok=True)
    for eixo, (prefixo, nome) in EIXOS.items():
        qs = [q for q in d["questoes"] if q["eixo"] == eixo]
        if not qs:
            continue
        sigla = c["id"].split("-")[0]
        arquivo = CONTEUDO / f"{prefixo}_prova_{sigla}_{ano}_{eixo}.md"
        cab = [f"# Prova {sigla.upper().replace('PCMG', 'P C M G')} {ano}. {nome}", ""]
        cab += [f"Esta é a prova real aplicada em {ano} pela banca {c['banca']} para o cargo de "
                f"{para_voz(c['cargo'])}. Os gabaritos são os oficiais definitivos.", ""]
        cab += ["Em cada questão, eu leio o enunciado e as quatro alternativas. Depois faço uma pausa "
                "para você pensar, e só então explico e dou a resposta. Se quiser treinar de verdade, "
                "pause o áudio na pausa, escolha a sua letra e depois continue.", "", "---", ""]
        corpo = []
        for q in qs:
            corpo += questao_md(q, textos)
        arquivo.write_text("\n".join(cab + corpo).rstrip("-\n ") + "\n", encoding="utf-8")
        print(f"{arquivo.name}: {len(qs)} questoes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "bancos/pcmg-tpag-2026.json"))
