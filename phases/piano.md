# Fase piano — intervista e perimetro

Obiettivo: arrivare a un perimetro approvato con tutte le decisioni di prodotto prese, senza
mai chiedere all'utente un fatto o una scelta tecnica.

## 1. Ingresso

- Milestone di ROADMAP: usa quella; assegna `F<NN>` come in `SKILL.md` ("Funzionalità e codici").
- Funzionalità che non è in SPEC né in ROADMAP: fermati. Prima entra in `SPEC.md` (fase
  `progetto`, leggi `phases/spec-builder.md`), poi la fase `roadmap`
  (`phases/allineamento.md`) la mette in ROADMAP; poi si torna qui.
- Crea `specs/<NN>-<slug>/spec.md` da `templates/spec.md`, `stato: piano`, con la riga
  `fonte:` che nomina la milestone. Se esiste già,
  riprendi: le decisioni in `## Decisioni di Andrea` sono chiuse, riparti dalle aperte.

## 2. Prima i fatti

Leggi: le sezioni di `SPEC.md` che la riguardano, `ROADMAP.md`, il codice coinvolto (file,
test esistenti, dati), `CLAUDE.md`, `AGENTS.md`. Annota ciò che la SPEC decide già: non lo
richiedi. Ogni domanda la cui risposta sta in un file è un errore.

Annota anche i **comandi di controllo** del progetto (test, build, lint, typecheck) dichiarati
in `CLAUDE.md`/`AGENTS.md` o nei file di configurazione, e se qualcosa li esegue in automatico
(CI online, hook pre-commit). Se mancano e la funzionalità è rischio 2-3, il perimetro include
il ticket che li crea, limitato ai comandi che il progetto ha davvero; senza repo online basta
un hook o uno script locale.

## 3. Albero delle decisioni

Elenca (per te, non all'utente) le decisioni di prodotto aperte e le dipendenze fra loro:
"chi può prenotare" viene prima di "cosa succede se è pieno". La **frontiera** sono le
decisioni con i prerequisiti già chiusi.

L'albero deve toccare tutti questi temi; uno già deciso dalla SPEC è chiuso:
1. **Chi** la usa, e cosa cambia per lui quando funziona.
2. **Confini**: cosa questa funzionalità NON fa.
3. **Casi limite**: vuoto, pieno, errore, permesso negato, annullamento, doppio invio.
4. **Regole**: numeri, scadenze, ordini, chi può fare cosa.
5. **Fatto quando**: cosa vede l'utente con i suoi occhi per dire che funziona.

## 4. Giri di domande

Ogni giro: al massimo 3 domande, tutte dalla frontiera. Poi aspetti le risposte, ricalcoli
la frontiera e prepari il giro dopo. Una domanda che dipende da un'altra dello stesso giro
va al giro successivo.

Forma di ogni domanda: una **scena** con persone e numeri, 2-4 opzioni di una riga,
raccomandazione con il motivo.

```
❓ D1 — Corso pieno
Maria prova a prenotare il corso di giovedì, già pieno (8 posti su 8). Cosa vede?
A) Entra in lista d'attesa e vede "sei la 2ª in attesa"
B) Messaggio "corso pieno", nient'altro
C) Le proponiamo il prossimo giovedì con posti liberi
➡️ Consiglio A: la SPEC §4 chiede già la lista d'attesa.
```

Solo prodotto. Una scelta tecnica (tabella, libreria, endpoint, struttura dati) la decidi tu
e la scrivi in `## Decisioni prese dall'agente` come `<scelta> — <motivo>`.
Un caso limite che cambia ciò che l'utente vede o può fare è una decisione di prodotto:
chiedilo. Uno che non cambia nulla per l'utente lo decidi tu e lo mostri in "Dedotto da me".

## 5. Salva subito

Dopo ogni risposta scrivi in `## Decisioni di Andrea` la riga `D<n> <domanda> → <risposta>`.
Se la sessione si interrompe, si riparte da qui.

- L'utente non sa rispondere → `## Aperti`: `[APERTO-NN] <domanda> → blocca <cosa>`.
  L'aperto blocca solo i ticket che ne dipendono.
- Oltre ~12 domande in totale: la funzionalità è troppo grande. Proponi la divisione in due
  voci di ROADMAP, con la riga di confine, e chiedi quale tenere ora.

## 6. Uscita

Quando la frontiera è vuota:
1. Compila `## Perimetro` (OBIETTIVO, FATTO QUANDO, AREE AMMESSE, FUORI PERIMETRO, VINCOLI,
   STOP SOLO SE). Ogni riga di FATTO QUANDO è osservabile senza chiedere all'utente.
2. Mostra all'utente, in chat:
   - **Detto da te**: le decisioni di Andrea, una riga ciascuna;
   - **Dedotto da me**: ciò che hai ricavato da SPEC, codice e decisioni tecniche, da correggere;
   - il Perimetro.
3. Chiedi: "Approvi il perimetro?" e fermati.

Con l'ok: `stato: spec` in `spec.md`, poi la riga `prossimo passo: /sdd spec`.
Con correzioni: aggiorna e richiedi l'ok. Il perimetro approvato è un contratto.
