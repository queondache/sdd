---
name: sdd
description: Spec-driven development planner. Use when starting a project from an idea, creating SPEC.md and ROADMAP.md, planning a feature into agent-ready tickets, or reviewing a delivered feature against its spec. Triggers "/sdd", "$sdd", "sdd", "spec-driven", "nuova funzionalità", "progetto nuovo", "codice esistente", "stato funzionalità", "prossima milestone". Plans and prepares context; development is launched by the user. Claude Code and Codex.
---

# sdd — dalla specifica ai ticket

`sdd` include spec-builder e allineamento: SPEC di progetto → ROADMAP → piano → spec → ticket → consegna, poi revisione e retro a sviluppo finito.
Lo sviluppo lo lancia l'utente (orchestratore, un agente, a mano): `sdd` si ferma alla
consegna con una riga che dice cosa lanciare. Funziona uguale in Claude Code e in Codex.

## Apertura

1. Leggi i file presenti fra `CLAUDE.md`, `AGENTS.md` e `progress.md` del progetto. Le loro regole valgono
   per ogni ticket e brief. Se due righe si contraddicono applica la più restrittiva e
   aggiungi un `[APERTO-NN]` con le due righe citate.
2. Guarda lo stato e rispondi con UNA riga: `Sei a: <dove> → prossimo passo: <comando>`.

| Trovi | Prossimo passo |
|---|---|
| `SPEC.md` assente o insufficiente (criteri di `phases/spec-builder.md`) | `/sdd progetto`: leggi `phases/spec-builder.md` |
| `ROADMAP.md` assente, o la versione SPEC nella sua intestazione ≠ versione di `SPEC.md` | `/sdd roadmap`: leggi `phases/allineamento.md` |
| Milestone di ROADMAP non FATTO senza una `spec.md` che la nomini in `fonte:` | `/sdd piano <milestone>` |
| `spec.md` con `stato: piano` | `/sdd piano <milestone>` (riprende dalle decisioni salvate) |
| `spec.md` con `stato: spec` | `/sdd spec` |
| `spec.md` con `stato: ticket` | `/sdd ticket` |
| Ticket `da rivedere`, o spec da cambiare | `/sdd ticket` sui ticket da rivedere · `/sdd spec` per cambiare la spec |
| `stato: consegna` o `revisione` e ticket sbloccati non ancora nella base | `/sdd consegna` |
| Tutti i ticket della funzionalità nella base | `/sdd revisione`, poi `/sdd retro` |

**Funzionalità e codici.** Una funzionalità è una milestone della sezione MILESTONE di
`ROADMAP.md` (scritta da `allineamento`, con il suo nome: "M6", "M-HOME"…). Alla prima
pianificazione le assegni `F<NN>` = primo numero libero fra le cartelle `specs/`, e scrivi in
`spec.md` la riga `fonte: ROADMAP.md milestone "<nome esatto>"`. Da lì in poi la ritrovi
cercando quel nome nelle righe `fonte:`. `ROADMAP.md` viene creata dalla fase `roadmap` (allineamento integrato);
la fase revisione la aggiorna alla chiusura (milestone → FATTO con evidenza).

**Base** = il ramo in cui entra il lavoro (di solito `main`). Prima di ogni controllo
"è entrato?": `git fetch`, poi `git log origin/<base> --oneline --grep "F<NN>-T<NN>"`
(senza remoto: `<base>` locale; senza git: nessun ticket è entrato, dillo).

Più milestone aperte: proponi la prima, in ordine di ROADMAP, senza dipendenze aperte
(`allineamento` ordina già per dipendenze e valore). Se l'utente ne nomina una, quella.

## Fasi

Carica solo il file della fase richiesta, poi seguilo fino al suo punto di arresto.

| Comando | File | Punto di arresto |
|---|---|---|
| `/sdd progetto` | `phases/spec-builder.md` | SPEC verificata e approvata |
| `/sdd roadmap` | `phases/allineamento.md` | ROADMAP verificata e approvata |
| `/sdd piano <milestone>` | `phases/piano.md` | approvazione del perimetro |
| `/sdd spec` | `phases/spec.md` | approvazione della spec |
| `/sdd ticket` | `phases/ticket.md` | approvazione dei ticket |
| `/sdd consegna` | `phases/consegna.md` | riga "lancia: …" |
| `/sdd revisione` | `phases/revisione.md` | esito con evidenza |
| `/sdd retro` | `phases/retro.md` | proposte in ordine di gravità |
| `/sdd stato` | `phases/stato.md` | tabella |

I percorsi `phases/`, `templates/`, `bin/` sono relativi alla cartella di questa skill.
`progetto` crea la SPEC dell’intero progetto; `spec` resta la mini-spec di una funzionalità.
Usa i percorsi di SPEC e ROADMAP stabiliti dal progetto, se diversi dalla root; mantieni una sola copia.

In Codex scrivi i comandi come `$sdd <fase>` invece di `/sdd <fase>`.

## File nel progetto

```
SPEC.md                          spec di progetto (spec-builder)
ROADMAP.md                       milestone + stato (allineamento)
specs/<NN>-<slug>/spec.md        mini-spec della funzionalità, campo stato:
specs/<NN>-<slug>/context.md     contesto per gli agenti (consegna)
specs/<NN>-<slug>/tickets/F<NN>-T<NN>-<slug>.md   un ticket per file, campo stato:
```

## Regole comuni

- **Fatti all'agente, decisioni all'utente.** Ciò che si trova leggendo file, codice o git lo
  cerchi tu. All'utente porti solo decisioni di prodotto. Le scelte tecniche le prendi tu e le
  scrivi in `## Decisioni prese dall'agente` con il motivo: l'utente può bocciarle.
- **Approvazione esplicita** ai punti di arresto. Le fasi `progetto` e `roadmap` scrivono rispettivamente SPEC e ROADMAP; le fasi di funzionalità scrivono in `specs/`, salvo l’aggiornamento finale di ROADMAP in revisione.
- **Ambiente e permessi:** conserva le modifiche esistenti; commit, pubblicazione e modifiche ai permessi seguono le autorizzazioni del progetto. Un progetto nuovo può iniziare senza Git o servizi esterni.
- **Agente separato** per ogni verifica (SPEC, ROADMAP, ticket, revisione): riceve solo i documenti indicati,
  mai il tuo ragionamento. In Claude Code un subagent, in Codex un sotto-agente o `codex exec`.
- **Evidenza** per ogni "fatto": comando + output, oppure `file:riga`.
- **Lingua con l'utente:** parole semplici, nessun gergo Git (regole in `AGENTS.md` globale).
- **Codice ticket** `F<NN>-T<NN>` in brief e titolo della proposta di modifica: così
  `git log origin/<base> --grep` dice cosa è entrato.

## Moduli inclusi e integrazioni

`spec-builder` e `allineamento` sono inclusi in `phases/`: leggili direttamente,
senza cercare altre installazioni. Le versioni qui incluse sono adattate a progetti
Claude Code e Codex, anche nuovi; non richiedono i percorsi personali dell’autore.
`retro` resta un’integrazione esterna: se assente, dichiara il limite e ferma solo
la fase retro. `orchestratore:brief` ha un formato alternativo in `phases/consegna.md`.

## Errori tipici

| Invece di | Fai |
|---|---|
| Partire senza approvazione | Fermati al punto di arresto |
| Chiedere una scelta tecnica | Decidi, scrivila in Decisioni prese dall'agente |
| Dire "fatto" sulla fiducia | Porta comando e output |
| Fidarti del tuo controllo | Agente separato |
| Ritoccare codice o lanciare sviluppo | Consegna la riga "lancia: …" |
