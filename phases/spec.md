# Fase spec — sintesi

Obiettivo: completare `spec.md` da ciò che è già deciso. Nessuna domanda nuova.

## 1. Ingresso

`spec.md` con `stato: spec` e perimetro approvato. Altrimenti torna a `/sdd piano`.

**Modifica di una spec già approvata** (stato `ticket`, `consegna` o `revisione`, su richiesta
dell'utente): cambia solo le sezioni toccate, mostra all'utente le US cambiate prima/dopo e
chiedi l'ok. Poi: ticket non `fatto` che coprono US cambiate → `stato: da rivedere`; US nuove
→ ticket nuovi; `stato: ticket` in `spec.md`. I ticket `fatto` restano.

## 2. Scrivi le sezioni

Usa il vocabolario del progetto (SPEC, glossario, nomi nel codice).

- **Problema**: il problema dell'utente, dal suo punto di vista.
- **Soluzione**: cosa cambia per l'utente, dal suo punto di vista.
- **Come utente voglio…**: elenco lungo e numerato, una riga per voce, esattamente nel formato
  `- US<n>: come <attore> voglio <cosa>, per <beneficio>`. Copri ogni decisione di Andrea
  e ogni caso limite deciso nel piano: ognuno deve finire in almeno una US.
- **Decisioni prese dall'agente**: completa con moduli toccati, interfacce, contratti, schema
  dati, interazioni. Una riga + motivo. Niente percorsi di file né codice: invecchiano.
  Eccezione: uno snippet uscito da un prototipo che fissa una decisione meglio della prosa
  (macchina a stati, schema, tipo), ridotto all'essenziale e segnato "da prototipo".
- **Come si testa**: il punto di aggancio dei test, il più alto possibile, preferendo quelli
  già presenti (meno punti di aggancio = meglio); un test esistente da imitare; la regola
  "si testa il comportamento esterno, non i dettagli interni".
- **Fuori perimetro**: cosa resta fuori, ripreso dal perimetro e ampliato.

## 3. Buchi

Se scrivendo trovi una decisione di prodotto mancante: fermati, torna al formato domanda di
`phases/piano.md` con UNA sola domanda, salva la risposta, riprendi.

## 4. Revisione dell'utente

Mostra all'utente solo:
- l'elenco **Come utente voglio…**;
- **Fuori perimetro**.

Le decisioni tecniche le controllerà l'agente separato nella fase ticket. Chiedi
"Approvi la spec?" e fermati.

Con l'ok: `stato: ticket`, poi la riga `prossimo passo: /sdd ticket`.
