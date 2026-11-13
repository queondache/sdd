#!/usr/bin/env python3
"""Controllo meccanico dei ticket di una funzionalità sdd.

Uso: python3 check_tickets.py <cartella-funzionalità>
Exit 0 se tutto valido, 1 con una riga ERRORE per ogni problema.
"""
import re
import sys
from pathlib import Path
from typing import Dict, List, Set

REQUIRED = ["stato", "aspetta", "copre", "tipo", "cosa ottiene l'utente"]
STATES = {"pronto", "bloccato", "da rivedere", "fatto"}
TICKET_ID = re.compile(r"F\d{2}-T\d{2}")
HEADING = re.compile(r"^# (F\d{2}-T\d{2}) — .+")
FIELD = re.compile(r"^([a-zà-ù' ]+):\s*(.*)$")
CRITERION = re.compile(r"^- C\d+: .+")
STORY = re.compile(r"^- (US\d+):")


def parse_ticket(path: Path) -> Dict[str, object]:
    # Legge intestazione, campi "chiave: valore" e criteri numerati
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    ticket: Dict[str, object] = {"file": path.name, "fields": {}, "criteria": 0, "id": None}
    if lines:
        m = HEADING.match(lines[0])
        if m:
            ticket["id"] = m.group(1)
    fields: Dict[str, str] = ticket["fields"]  # type: ignore[assignment]
    for line in lines[1:]:
        if CRITERION.match(line):
            ticket["criteria"] = int(ticket["criteria"]) + 1  # type: ignore[arg-type]
            continue
        # "tipo: … rischio: N" sta su una riga sola
        risk = re.search(r"rischio:\s*(\S+)", line)
        if risk:
            fields["rischio"] = risk.group(1)
            line = line[: risk.start()].rstrip()
        m = FIELD.match(line)
        if m:
            fields[m.group(1).strip()] = m.group(2).strip()
    return ticket


def split_ids(value: str) -> List[str]:
    if value.strip().lower() in ("", "nessuno"):
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def find_cycle(deps: Dict[str, List[str]]) -> List[str]:
    # DFS iterativa-ricorsiva con stati: 0 nuovo, 1 in visita, 2 chiuso
    state: Dict[str, int] = {k: 0 for k in deps}
    stack: List[str] = []

    def visit(node: str) -> List[str]:
        state[node] = 1
        stack.append(node)
        for nxt in deps.get(node, []):
            if nxt not in state:
                continue
            if state[nxt] == 1:
                return stack[stack.index(nxt):] + [nxt]
            if state[nxt] == 0:
                found = visit(nxt)
                if found:
                    return found
        stack.pop()
        state[node] = 2
        return []

    for node in sorted(deps):
        if state[node] == 0:
            found = visit(node)
            if found:
                return found
    return []


def check_feature(path: str) -> List[str]:
    root = Path(path)
    errors: List[str] = []
    spec = root / "spec.md"
    stories: Set[str] = set()
    if not spec.is_file():
        errors.append(f"ERRORE {root}: spec.md assente")
    else:
        for line in spec.read_text(encoding="utf-8").splitlines():
            m = STORY.match(line)
            if m:
                stories.add(m.group(1))

    if spec.is_file() and not stories:
        errors.append("ERRORE spec.md: nessuna US nel formato '- US<n>: …'")
    files = sorted((root / "tickets").glob("*.md"))
    if not files:
        errors.append(f"ERRORE {root}/tickets: nessun ticket trovato")
    tickets = [parse_ticket(f) for f in files]
    by_id: Dict[str, Dict[str, object]] = {}
    for tk in tickets:
        name = str(tk["file"])
        fields: Dict[str, str] = tk["fields"]  # type: ignore[assignment]
        tid = tk["id"]
        if not tid:
            errors.append(f"ERRORE {name}: intestazione '# F<NN>-T<NN> — titolo' assente")
            continue
        if not name.startswith(str(tid) + "-"):
            errors.append(f"ERRORE {name}: codice {tid} diverso dal nome file")
        if tid in by_id:
            errors.append(f"ERRORE {name}: codice {tid} duplicato")
        by_id[str(tid)] = tk
        for key in REQUIRED + ["rischio"]:
            if not fields.get(key):
                errors.append(f"ERRORE {name}: {tid} senza campo '{key}'")
        if fields.get("stato") and fields["stato"] not in STATES:
            errors.append(f"ERRORE {name}: stato '{fields['stato']}' non valido")
        if fields.get("rischio") and fields["rischio"] not in ("1", "2", "3"):
            errors.append(f"ERRORE {name}: rischio '{fields['rischio']}' non valido")
        if not tk["criteria"]:
            errors.append(f"ERRORE {name}: nessun criterio numerato '- C1: …' nei criteri di accettazione")

    deps = {tid: split_ids(str(tk["fields"].get("aspetta", ""))) for tid, tk in by_id.items()}  # type: ignore[union-attr]
    for tid, needs in deps.items():
        for dep in needs:
            if dep not in by_id:
                errors.append(f"ERRORE {by_id[tid]['file']}: aspetta {dep} inesistente")
    # Un ticket pronto deve avere tutte le attese già fatte
    for tid, needs in deps.items():
        if by_id[tid]["fields"].get("stato") != "pronto":  # type: ignore[union-attr]
            continue
        for dep in needs:
            if dep in by_id and by_id[dep]["fields"].get("stato") != "fatto":  # type: ignore[union-attr]
                errors.append(f"ERRORE {by_id[tid]['file']}: {tid} è pronto ma aspetta {dep} non ancora fatto")
    cycle = find_cycle(deps)
    if cycle:
        errors.append("ERRORE dipendenze: ciclo " + " → ".join(cycle))

    # Rischio 3 ereditato: chi dipende (anche indirettamente) da un rischio 3 è rischio 3
    def risk(tid: str) -> str:
        return str(by_id[tid]["fields"].get("rischio", ""))  # type: ignore[union-attr]

    if not cycle:
        for tid in by_id:
            seen: Set[str] = set()
            todo = list(deps.get(tid, []))
            while todo:
                dep = todo.pop()
                if dep in seen or dep not in by_id:
                    continue
                seen.add(dep)
                if risk(dep) == "3" and risk(tid) != "3":
                    errors.append(f"ERRORE {by_id[tid]['file']}: {tid} dipende da {dep} (rischio 3) e deve essere rischio 3")
                    break
                todo.extend(deps.get(dep, []))

    covered: Set[str] = set()
    for tid, tk in by_id.items():
        for us in split_ids(str(tk["fields"].get("copre", ""))):  # type: ignore[union-attr]
            if stories and us not in stories:
                errors.append(f"ERRORE {tk['file']}: copre {us}, che non esiste in spec.md")
            covered.add(us)
    for us in sorted(stories - covered):
        errors.append(f"ERRORE spec.md: {us} non coperta da nessun ticket")
    return errors


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("uso: check_tickets.py <cartella-funzionalità>")
        return 2
    errors = check_feature(argv[1])
    for e in errors:
        print(e)
    if errors:
        return 1
    count = len(list((Path(argv[1]) / "tickets").glob("*.md")))
    print(f"OK: {count} ticket")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
