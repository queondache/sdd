# SDD — dalla specifica ai ticket

Skill personale di Andrea per Claude Code e Codex. Pianifica: perimetro → specifica → ticket → consegna → revisione → retro. Lo sviluppo lo avvia l’utente.

## Installazione

Scarica **Code → Download ZIP**, estrai e copia la cartella con il nome `sdd` in `~/.claude/skills/` (Claude Code) oppure `~/.agents/skills/` (Codex). Il file `SKILL.md` deve stare direttamente dentro `sdd/`.

## Uso

Claude Code: `/sdd`. Codex: `$sdd` oppure «usa sdd».

Fasi: `piano`, `spec`, `ticket`, `consegna`, `revisione`, `retro`, `stato`.

[Leggi le istruzioni complete](SKILL.md).

## Dipendenze

Questa copia conserva i riferimenti e le convenzioni personali di Andrea. Richiama `spec-builder`, `allineamento` e `retro`, non incluse: le fasi che le richiedono si fermano se non sono disponibili. La consegna può usare `orchestratore:brief` o il formato alternativo descritto nella skill.

Per partire da una milestone servono `SPEC.md` e `ROADMAP.md` nel progetto. Il validatore incluso richiede Python 3 e usa solo la libreria standard.
