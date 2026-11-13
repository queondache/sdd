# Fase revisione — la funzionalità promessa c'è?

Obiettivo: verificare l'insieme. Il verificatore ha già controllato ogni ticket da solo; qui si
controlla che i ticket entrati nella base realizzino davvero la spec.

## 1. Ingresso

`git fetch`, poi `git log origin/<base> --oneline --grep "F<NN>-T"` → ticket entrati. Ticket ancora fuori:
elencali e chiedi all'utente se procedere con una revisione parziale.

## 2. Agente separato

Lancia un agente separato con SOLO `spec.md`, la cartella `tickets/` e il codice della base:
```text
Per ogni ticket in <cartella>/tickets: per ogni criterio C dai OK/KO con evidenza eseguita da te
(comando + output, oppure file:riga). Poi per ogni US di spec.md: realizzata sì/no con evidenza.
Non fidarti dei resoconti di chi ha sviluppato. Esito finale: OK o KO con elenco dei buchi.
```

## 3. Esiti

- Ticket con tutti i C OK → `stato: fatto`.
- Buco (criterio KO, US non realizzata) → ticket nuovo con il primo codice libero, scritto
  con le regole di `phases/ticket.md` e passato da `bin/check_tickets.py`; `stato: revisione`
  in `spec.md`; prossimo passo `/sdd consegna`.
- Tutto OK → `stato: chiusa` in `spec.md`; la milestone in ROADMAP → `FATTO` con evidenza
  (file, test, codici ticket), unica scrittura di `sdd` in ROADMAP; prossimo passo `/sdd retro`.

## 4. Report in chat

```
F<NN> — <nome>: <CHIUSA | DA COMPLETARE>
US realizzate: <n>/<tot>   ticket fatti: <n>/<tot>
- US<n>: OK — <comando + esito | file:riga>
Buchi → nuovi ticket: <codici | nessuno>
Prossimo passo: <comando>
```
