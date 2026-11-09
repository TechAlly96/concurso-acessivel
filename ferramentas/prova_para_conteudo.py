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


# Siglas soletradas para a voz (as pronunciaveis, como ONU e OAB, ficam como estao).
SIGLAS = {
    "IPv4": "I P versão 4", "IPv6": "I P versão 6", "GPLv2": "G P L versão 2", "GPLv3": "G P L versão 3",
    "BSD": "B S D", "DRM": "D R M", "NAT": "N A T", "DoS": "D o S", "CSV": "C S V", "PDF": "P D F",
    "TI": "T I", "IP": "I P", "STF": "S T F", "STJ": "S T J", "LC": "L C", "EC": "E C",
    "DH": "D H", "DNA": "D N A", "PCMG": "P C M G", "CPP": "C P P", "IML": "I M L", "EPI": "E P I",
    "OMS": "O M S", "RSS": "R S S", "UV": "U V", "CF": "Constituição Federal", "GHz": "gigahertz",
    "TPAG": "T P A G", "FGV": "F G V", "NR": "N R", "HIV": "H I V", "CLT": "C L T", "VBA": "V B A",
    "RDC": "R D C", "GPL": "G P L", "v3": "versão 3", "PNDH": "P N D H", "CEDAW": "Cedáu",
}

# Algarismos romanos de itens e incisos, lidos por extenso.
ROMANOS = {"I": "um", "II": "dois", "III": "três", "IV": "quatro", "V": "cinco", "VI": "seis",
           "VII": "sete", "VIII": "oito", "IX": "nove", "X": "dez", "XX": "vinte",
           "LVI": "cinquenta e seis", "LXIII": "sessenta e três"}
VF = {"V": "verdadeira", "F": "falsa"}


def verdadeiro_falso(t):
    """'V – F – V.' -> 'verdadeira, falsa, verdadeira.'"""
    m = re.fullmatch(r"\s*([VF](?:\s*[–,-]\s*[VF])+)\s*(\.?)\s*", t)
    if not m:
        return None
    return ", ".join(VF[x] for x in re.findall(r"[VF]", m[1])) + m[2]


def para_voz(t):
    """Ajusta o texto para a voz Piper ler corretamente."""
    vf = verdadeiro_falso(t)
    if vf:
        return vf
    t = re.sub(r"\(?\bV\b\)? para a verdadeira e \(?\bF\b\)? para a falsa",
               "verdadeiro para a verdadeira e falso para a falsa", t)
    t = re.sub(r"\b(LXIII|LVI|XX|VIII|VII|VI|IV|IX|III|II|I|V|X)\b(?![\-–])",
               lambda m: ROMANOS[m[1]], t)
    t = re.sub(r"=((?:\$?[A-Z]{1,2}\$?\d+\*?)+)", formula_falada, t)
    t = re.sub(r"\b\$?[A-Z]{1,2}\$\d+\b|\$[A-Z]{1,2}\$?\d+\b", lambda r: celula_falada(r.group(0)), t)
    t = t.replace("−", "menos ")
    t = re.sub(r"(\d)\s*°C", r"\1 graus Celsius", t)
    t = re.sub(r"\bn\.?º\s*", "número ", t)
    t = t.replace("§", "parágrafo ").replace("–", ",")
    for sigla, falada in SIGLAS.items():
        t = re.sub(r"\b" + re.escape(sigla) + r"\b", falada, t)
    t = re.sub(r"\bart\.\s*(\d+)\.º", r"artigo \1º", t)
    t = re.sub(r"\bart\.\s*", "artigo ", t)
    # Numero de lei: 5.406/1969 -> 5406, de 1969 (a voz nao le ponto de milhar nem barra)
    t = re.sub(r"\b(\d{1,3})\.(\d{3})/(\d{4})\b", r"\1\2, de \3", t)
    t = re.sub(r"\b(\d{1,4})/(\d{4})\b", r"\1, de \2", t)
    t = t.replace("(ex.:", "(por exemplo,").replace("ex.:", "por exemplo,")
    t = t.replace("Constituição Federal de 1988 (Constituição Federal)", "Constituição Federal de 1988")
    t = t.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("’", "'")
    return t


def sem_resposta_final(explicacao):
    """A explicacao termina com 'Resposta: X.'; a resposta vai em linha propria."""
    return re.sub(r"\s*Resposta: [A-E]\.?\s*$", "", explicacao).strip()


def questao_md(q, textos):
    linhas = [f"## Questão {q['numero']}. {para_voz(q['tema'])}", ""]
    linhas += [f"**Disciplina.** {para_voz(q['disciplina'])}.", ""]
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
    for letra in sorted(q["alternativas"]):
        alt = para_voz(q["alternativas"][letra]).rstrip(".")
        linhas += [f"Letra {letra}: {alt}.", ""]
    linhas += ["Pense na sua resposta antes de ouvir a explicação.", ""]
    linhas += [f"**A explicação.** {para_voz(sem_resposta_final(q['explicacao']))}", ""]
    if q["gabarito"] == "anulada":
        linhas += ["**Questão anulada pela banca.** Na prova, ela valeu ponto para todos os candidatos.", "", "---", ""]
        return linhas
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
    eixos = {e["id"]: (e["prefixo"], e["nome"]) for e in d["eixos"]} if d.get("eixos") else EIXOS
    for eixo, (prefixo, nome) in eixos.items():
        qs = [q for q in d["questoes"] if q["eixo"] == eixo]
        if not qs:
            continue
        sigla = c["id"].split("-")[0]
        arquivo = CONTEUDO / f"{prefixo}_prova_{sigla}_{ano}_{eixo}.md"
        cab = [f"# Prova {para_voz(c['orgao'].split(' (')[0])}, {para_voz(c['cargo'])}, {ano}. {nome}", ""]
        cab += [f"Esta é a prova real aplicada em {ano} pela banca {c['banca']} para o cargo de "
                f"{para_voz(c['cargo'])}. Os gabaritos são os oficiais definitivos.", ""]
        cab += ["Em cada questão, eu leio o enunciado e as quatro alternativas. Depois faço uma pausa "
                "para você pensar, e só então explico e dou a resposta. Se quiser treinar de verdade, "
                "pause o áudio na pausa, escolha a sua letra e depois continue.", "", "---", ""]
        if d.get("introducao"):
            cab[-2:-2] = ["", d["introducao"]]
        corpo = []
        for q in qs:
            corpo += questao_md(q, textos)
        arquivo.write_text("\n".join(cab + corpo).rstrip("-\n ") + "\n", encoding="utf-8")
        print(f"{arquivo.name}: {len(qs)} questoes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "bancos/pcmg-tpag-2026.json"))
