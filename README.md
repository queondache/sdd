# SDD — dall’idea ai ticket

La skill di Andrea per Claude Code e Codex. Include **spec-builder** e
**allineamento**: puoi partire da un’idea, senza avere già SPEC.md o ROADMAP.md.

## Installazione

Scarica **Code → Download ZIP**, estrai e copia la cartella con il nome `sdd` in:

- Claude Code: `~/.claude/skills/sdd/`
- Codex: `~/.agents/skills/sdd/`

`SKILL.md`, `phases/`, `templates/` e `bin/` devono stare direttamente dentro
`sdd/`. Se hai già scaricato la versione precedente, sostituisci la sua cartella
con questa versione, conservando eventuali personalizzazioni.

## Parti da zero

Apri la cartella del tuo progetto in Claude Code o Codex e scrivi:

> Usa sdd. Parto da zero e voglio costruire [descrivi la tua idea]. Aiutami a creare SPEC.md e ROADMAP.md.

La skill ti fa domande, scrive la SPEC, la sottopone a verifica indipendente e
chiede la tua approvazione. Poi costruisce la ROADMAP e guida la pianificazione
della prima funzionalità. Le decisioni di prodotto restano tue.

## Comandi

| Obiettivo | Claude Code | Codex |
|---|---|---|
| Capire da dove partire | `/sdd` | `$sdd` |
| Creare o migliorare la SPEC del progetto | `/sdd progetto` | `$sdd progetto` |
| Creare o riallineare la ROADMAP | `/sdd roadmap` | `$sdd roadmap` |
| Pianificare una milestone | `/sdd piano <milestone>` | `$sdd piano <milestone>` |
| Scrivere la mini-spec della funzionalità | `/sdd spec` | `$sdd spec` |
| Preparare i ticket | `/sdd ticket` | `$sdd ticket` |
| Preparare la consegna | `/sdd consegna` | `$sdd consegna` |
| Verificare quanto sviluppato | `/sdd revisione` | `$sdd revisione` |
| Leggere lo stato | `/sdd stato` | `$sdd stato` |

Lo sviluppo lo avvii tu dopo la consegna. [Istruzioni complete](SKILL.md).

## Cosa è incluso

- [Spec-builder](phases/spec-builder.md): domande, decisioni aperte, SPEC e giudizio indipendente.
- [Allineamento](phases/allineamento.md): confronto SPEC/codice, milestone e verifica della ROADMAP.
- Pianificazione delle funzionalità, modelli di documenti e validatore dei ticket.

I due moduli sono adattati dalle skill personali di Andrea: funzionano anche
senza GitHub e senza i suoi percorsi locali. I documenti delle funzionalità
conservano alcuni titoli storici con il nome Andrea: indicano il responsabile
delle decisioni di prodotto del progetto.

## Requisiti e integrazioni

Python 3 serve per il validatore dei ticket; usa solo la libreria standard.
Le verifiche richiedono un agente separato o una sessione indipendente; in sua
assenza la skill dichiara la verifica in attesa, senza inventare un esito.
Git serve alle fasi che controllano l’integrazione del codice, non alla creazione
iniziale di SPEC e ROADMAP.

`retro` resta esterna e serve solo per `/sdd retro`, dopo lo sviluppo.
`orchestratore:brief` è facoltativa: la consegna include un formato alternativo.
