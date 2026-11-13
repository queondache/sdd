# Fase retro — migliorare l'ambiente degli agenti

1. Trova le sessioni della funzionalità: transcript che citano `F<NN>` (Claude Code:
   `~/.claude/projects/<progetto>/*.jsonl`; Codex: `~/.codex/sessions/`). Cerca con `grep -l`.
2. Carica la skill `retro` e passale quelle sessioni come sessioni da analizzare.
3. Presenta le proposte all'utente in ordine di gravità, una riga ciascuna con l'effetto atteso.
4. Una proposta che cambia la spec o i ticket passa dalla fase relativa (`/sdd spec`,
   `/sdd ticket`). Una che cambia `CLAUDE.md`, `AGENTS.md` o i controlli automatici si mostra
   all'utente come modifica prima/dopo e si applica solo con il suo ok.
