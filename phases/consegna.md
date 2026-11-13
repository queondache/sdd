# Fase consegna — contesto e riga di lancio

Obiettivo: preparare tutto ciò che serve a chi sviluppa e dire all'utente cosa lanciare.
Scrive solo `context.md` e lo `stato:` dei ticket; il brief va in chat, nessun altro file.
Lo sviluppo lo lancia l'utente.

## 1. Quali ticket

1. `git fetch`. Per ogni ticket non `fatto`, controlla se è già nella base:
   `git log origin/<base> --oneline --grep "F<NN>-T<NN>"`. Trovato → `stato: fatto`.
2. Un `bloccato` con tutti gli `aspetta` fatti → `stato: pronto`.
3. Ticket da consegnare = i `pronto` non ancora nella base. Escludi quelli bloccati da un
   `[APERTO]` e i `da rivedere`. Nessuno pronto → dillo e indica cosa li blocca.
4. Esegui `bin/check_tickets.py` sulla cartella: deve dare `OK`.

## 2. context.md

Scrivi `specs/<NN>-<slug>/context.md`, al massimo 60 righe, inviato davanti a ogni brief:
- obiettivo della funzionalità in una frase;
- stack e versioni; come lanciare un solo file di test; comandi completi di build, test, lint;
- variabili d'ambiente o servizi che i test richiedono;
- regole del repo citate testualmente sia da `CLAUDE.md` sia da `AGENTS.md` (lingua dei
  commenti, nomi, log degli errori, dipendenze);
- mappa delle cartelle toccate, una riga ciascuna;
- glossario delle parole con significato locale;
- trappole note: risorse esclusive, test lenti, file generati da non toccare.

Ogni comando lo esegui una volta ora e annoti l'esito. Un comando che non gira non entra;
uno che un ticket deve ancora creare entra come `da creare in F<NN>-T<NN>`.
L'orchestratore scrive il suo `.orchestratore/CONTEXT.md`: nella riga di lancio indica
`context.md` come fonte da copiare.

## 3. Riga di lancio

**Due o più ticket pronti** — rispondi:
```
Lancia: orchestratore — ticket F03-T01, F03-T03 (specs/03-<slug>/tickets/) · CONTEXT da specs/03-<slug>/context.md · ID unità = codice ticket, titolo di ogni proposta di modifica inizia col codice
```
L'orchestratore li trasforma in brief con il suo formato.

**Un ticket pronto** — scrivi il brief completo nel formato della skill `orchestratore:brief`
(sezione "Write the brief"), con:
- `ID` = codice ticket, `class` da `tipo`, `tier` = `rischio`;
- `goal` = cosa ottiene l'utente; `spec` = le US coperte citate da `spec.md`;
- `proof` = i criteri C1..Cn del ticket;
- `read first`, `write only`, `do not touch`, `code`, `pattern` con percorsi esatti verificati
  ora sul codice della base (partendo da `aree probabili`);
- `commands` = test mirato, eseguito ora sulla base con esito annotato;
- la riga: "il titolo della proposta di modifica inizia con `F<NN>-T<NN>`".

Poi la riga: `Lancia: incolla il brief a un agente (Claude Code o Codex).`
Se la skill `orchestratore:brief` non è disponibile, usa i campi elencati sopra nello stesso ordine.

## 4. Chiusura

Riga finale: `prossimo passo: sviluppo (lo lanci tu) → poi /sdd consegna per i ticket sbloccati, /sdd revisione a ticket tutti nella base`.
