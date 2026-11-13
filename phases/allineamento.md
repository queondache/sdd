# Allineamento SPEC → ROADMAP

Modulo integrato di SDD, derivato dalla skill allineamento di Andrea.
Produce il delta fra il prodotto descritto dalla SPEC e ciò che esiste davvero.

## 1. Contesto e prerequisiti

Leggi le istruzioni locali, la SPEC approvata, la ROADMAP e lo stato esistenti.
Usa i percorsi del progetto; se non sono stabiliti, usa la root. SPEC assente o
insufficiente: torna a `/sdd progetto` leggendo `phases/spec-builder.md`.

Controlla le modifiche e le copie di lavoro se Git è presente. Preserva il lavoro
esistente; chiedi come procedere solo se una modifica concorrente interessa i
file da scrivere. Registra la revisione analizzata, o «cartella locale senza Git».
Git, remoto, GitHub, autenticazione e protezioni del ramo non sono prerequisiti
per scrivere la roadmap. Non creare commit, inviare modifiche o cambiare configurazioni.

Progetto nuovo senza codice: tutte le capacità sono MANCANTI; non inventare
comandi di build o test. Con codice esistente, individua i controlli disponibili,
eseguili se l’ambiente e le regole locali lo consentono e registra errori o limiti.
Un controllo non eseguito non è un controllo passato.

## 2. Analisi e ROADMAP

Leggi tutta la SPEC. Esamina codice, test e interfacce pertinenti. Per progetti
ampi puoi usare agenti separati per area, con incarico di sola lettura e richiesta
di evidenze con file e riga. Rispetta il limite di agenti dell’ambiente.

Scrivi solo ROADMAP, conservando le parti ancora valide:
- Intestazione: versione SPEC, data, revisione o stato locale analizzato.
- Ogni capacità: FATTO, PARZIALE o MANCANTE, con evidenza concreta. FATTO richiede
  prova del comportamento richiesto; senza evidenza non assegnarlo.
- Ogni capacità PARZIALE o MANCANTE entra in una milestone. Gli aperti della SPEC
  restano espliciti: indica le milestone che bloccano, senza inventare decisioni.
- Sezione MILESTONE: nome stabile, risultato utente verificabile, dipendenze,
  aree coinvolte, taglia piccola/media/grande. Ogni milestone è completabile in
  una sessione; dividi quelle più grandi. Ordina per dipendenza e poi valore.
- Le milestone eseguibili in parallelo hanno file disgiunti e nessuna dipendenza
  implicita: altrimenti ordinale o fondile. Punta a 60 righe; conserva la copertura
  completa della SPEC anche quando richiede più spazio.

Le milestone nascono dal delta osservato. Un piano storico nella SPEC non prova
lo stato del prodotto: segnala la duplicazione, senza modificare la SPEC in questa fase.
Se ROADMAP esiste, ricontrolla le evidenze, conserva nomi e riferimenti validi,
aggiungi il nuovo e segnala ciò che la SPEC non richiede più. Non creare STATE.md
né altri documenti di stato.

## 3. Verifica indipendente

Affida a un agente a contesto fresco solo SPEC, ROADMAP, accesso in lettura al
codice e questa richiesta:

> Verifica la copertura di ogni capacità della SPEC nella ROADMAP. Controlla fino
> a tre voci FATTO e tre MANCANTE scelte da te (tutte se sono meno), con evidenze.
> In un progetto senza codice verifica che nessuna capacità sia marcata FATTO.
> Controlla dipendenze e sovrapposizioni delle milestone parallele. Restituisci
> OK o KO con problemi puntuali, file e righe. Gli aperti dichiarati sono limiti,
> non decisioni prese.

Se KO, correggi e richiedi verifica sul testo aggiornato. Dopo tre correzioni
fallite fermati e presenta il punto irrisolto. Ogni modifica successiva a un OK
richiede nuova verifica. Se non puoi usare un agente separato, prepara il materiale
per una sessione indipendente e dichiara la verifica in attesa, senza autovalutarti.

## 4. Approvazione e consegna

Mostra capacità FATTO/PARZIALE/MANCANTE, milestone, limiti e verdetto indipendente.
Chiedi approvazione della ROADMAP. Con OK del verificatore e approvazione dell’utente,
indica `/sdd piano <prima milestone senza dipendenze e senza aperti bloccanti>`.
Se tutte sono bloccate, poni una domanda su un aperto che sblocca il percorso.
La fase termina con il documento approvato; lo sviluppo resta un passo successivo.
