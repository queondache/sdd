# Fase stato — tabella

Ricava i dati da `ROADMAP.md`, `specs/*/spec.md` (`stato:`, `## Aperti`), i ticket (`stato:`)
e, dopo `git fetch`, `git log origin/<base> --oneline --grep "F<NN>-T"` (un ticket nella base
conta come fatto anche se il file dice altro: segnalalo).

```
| F | Funzionalità | Stato | Ticket fatti/totali | Aperti bloccanti | Prossimo passo |
|---|---|---|---|---|---|
| F02 | Lista d'attesa | consegna | 1/3 | — | /sdd consegna |
```

Righe in ordine di ROADMAP. Sotto la tabella, la riga del router:
`Sei a: <dove> → prossimo passo: <comando>`.
