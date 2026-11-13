# Fase ticket — fette verticali

Obiettivo: ticket che un agente può eseguire da solo, che insieme coprono ogni US, con le
dipendenze giuste. Ogni ticket è un **tracer bullet**: una fetta verticale stretta ma completa.

## 1. Ingresso

`spec.md` con `stato: ticket`. Leggi spec, `CLAUDE.md`, `AGENTS.md` e il codice coinvolto.
Se esistono ticket `da rivedere` lavora solo su quelli e sulle US nuove: riscrivili, poi check,
agente separato e approvazione come sotto; ognuno torna `pronto` o `bloccato` secondo le attese.
Cerca un **prefactoring** che renda il resto facile: "rendi facile la modifica, poi fai la
modifica facile". Se c'è, è il primo ticket, come quello dei controlli automatici se il
perimetro lo prevede. Questi ticket di base hanno `copre: nessuno`.

## 2. Bozza

Regole delle fette:
- ogni fetta attraversa tutti gli strati che servono (dati, logica, interfaccia, test): mai
  "tutto il database" in un ticket e "tutta l'interfaccia" in un altro;
- ogni fetta, finita, si dimostra da sola;
- ogni fetta entra in un contesto fresco di un agente (indicativo: ≤ 1 giornata, ≤ 10 file);
- una fetta sotto ~30 minuti di lavoro si unisce alla vicina;
- `aspetta` elenca solo i ticket che la bloccano davvero;
- ogni ticket consegna un comportamento, salvo i ticket di base del §1: revisione,
  integrazione e verifica non sono ticket (le fa il verificatore e poi `/sdd revisione`).

Eccezione, **refactor largo** (un cambio meccanico che rompe molti punti, es. rinominare un
campo usato ovunque): espandi (nuova forma accanto alla vecchia) → migra a lotti (un ticket per
lotto, ognuno aspetta l'espansione) → contrai (togli la vecchia, aspetta tutti i lotti).

Rischio: **3** se tocca schema/migrazioni, accessi, pagamenti, multi-tenancy, dati personali
o sanitari, segreti, permessi, cancellazione definitiva di dati salvati (un "annulla" fatto
dall'utente non lo è); **2** codice di prodotto; **1** test,
documenti, strumenti interni. Chi dipende da un rischio 3 è rischio 3. Nel dubbio, il più alto.

Tipo: `correzione` (comportamento sbagliato), `nuova funzione`, `controllo` (nessun test
automatico possibile: aspetto, testi, configurazione).

## 3. Mostra la bozza

All'utente, elenco numerato:
```
F03-T01 — <titolo> · aspetta: nessuno · <cosa ottiene l'utente>
F03-T02 — <titolo> · aspetta: F03-T01 · <cosa ottiene l'utente>
```
Chiedi: "La grandezza dei pezzi va bene? Le attese sono giuste? Qualcosa da unire o dividere?"
Itera fino all'ok sulla bozza.

## 4. Scrivi i file

Un file per ticket da `templates/ticket.md`, in `specs/<NN>-<slug>/tickets/`, numerati in
ordine di dipendenza. `stato: pronto` se ogni ticket in `aspetta` è `fatto` (o `aspetta: nessuno`), altrimenti `bloccato`.
`copre` elenca le US realizzate. Ogni criterio `C<n>` nomina il test che lo dimostra e cosa
farebbe diventare rosso quel test. `aree probabili` sono cartelle indicative.

Poi esegui:
```
python3 <cartella skill>/bin/check_tickets.py specs/<NN>-<slug>
```
Correggi i ticket finché l'uscita è `OK: <n> ticket`.

## 5. Agente separato

Lancia un agente separato con SOLO `SPEC.md`, `spec.md` e la cartella `tickets/`, con questo testo:
```text
Verifica i ticket in <cartella>/tickets contro <cartella>/spec.md. Rispondi OK o KO con elenco:
1) ogni US della spec è coperta da un ticket che la realizza davvero (non solo la cita in "copre");
2) due ticket senza dipendenza reciproca non lavorano sulle stesse aree;
3) ogni ticket è una fetta verticale dimostrabile da sola;
4) ogni criterio C è osservabile da un test; un ticket con `copre: nessuno` è davvero
   preparatorio (prefactoring o controlli automatici), non un pezzo di prodotto;
5) le decisioni prese dall'agente in spec.md sono coerenti con SPEC.md e con i ticket.
KO solo per un problema che porterebbe un agente a sviluppare la cosa sbagliata o a non
poterla dimostrare. Tutto il resto elencalo come NOTE, senza KO.
Per ogni KO: ticket, problema, correzione proposta.
```
KO → correggi, rilancia il check e l'agente. Dopo due KO consecutivi fermati: porta
all'utente l'ultimo verdetto e le due strade che vedi, e riparti solo dopo la sua scelta
(il conto riparte da zero). Le NOTE le mostri all'utente all'approvazione.

## 6. Approvazione

Con l'OK dell'agente mostra all'utente: numero di ticket, quanti partono subito, eventuali
`[APERTO]` che ne bloccano alcuni. Chiedi "Approvi i ticket?" e fermati.

Con l'ok: `stato: consegna` in `spec.md`, poi la riga
`prossimo passo: /sdd consegna`.
