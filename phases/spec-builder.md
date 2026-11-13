# spec-builder — costruire SPEC che un agente può usare

Modulo integrato di SDD, derivato dalla skill spec-builder di Andrea.
Lavora nella cartella del progetto con Claude Code o Codex. Leggi le istruzioni
locali e il materiale fornito dall’utente. Se manca il contesto di prodotto,
chiedilo prima di formulare decisioni. Un progetto nuovo può partire dall’idea
raccontata dall’utente: non richiede SPEC, ROADMAP, Git o GitHub preesistenti.

## A cosa serve una SPEC
A far decidere un agente da solo, senza chiedere e senza indovinare. Il valore
non sta nella prosa che descrive il prodotto: sta nei confini. Cosa e' vietato,
cosa e' gia' deciso e non si ridiscute, cosa e' ancora aperto.
**La distinzione piu' importante e' fra deciso e ipotizzato.** In prosa i due si
confondono ("ipotesi: si'", "da confermare") e l’agente costruisce sull'ipotesi come
se fosse decisione. Renderla strutturale e' il lavoro principale di questa skill.

## Materiale di partenza

Leggi i documenti accessibili del progetto e le informazioni già date dall’utente.
Se mancano obiettivi o regole, chiedili nei giri di domande. Il codice documenta
cosa esiste, non prova l’intenzione di prodotto. Non presumere accesso a chat,
memorie o archivi esterni. Usa il percorso SPEC esistente, oppure `SPEC.md` nella
root. Scrivi solo la SPEC; le altre fasi hanno documenti propri.

## Come si lavora: A GIRI, con l’utente che risponde e un giudice esterno che vota
La SPEC non la scrive l’utente e non la scrivi tu da solo: **la costruite a giri**.
Tu fai le domande, l’utente risponde, tu scrivi; un giudice a contesto fresco vota.
Si itera finche' il giudice non da' **10/10** o l’utente non dichiara stop.

**Giro 0 — analisi.** Leggi SPEC.md se esiste (se non esiste, il giro 0 e' solo
sul materiale di contesto). Proponi il TAGLIO della SPEC (vedi sotto: market /
function / goal) motivandolo dal tipo di progetto; lo conferma l’utente. Poi
valuta le sezioni 1-7 con i criteri sotto (SUFFICIENTE / DA MIGLIORARE / ASSENTE;
la 8 e' opzionale). Caccia le incertezze in prosa
("da confermare", "ipotesi", "probabilmente", "da validare", "TBD") e proponi di
promuoverle a [APERTO-NN]. Mostra all’utente il quadro PRIMA di qualsiasi domanda.

**Ogni giro successivo, sempre nello stesso ordine:**
1. **Domande, a BLOCCHI di max 5** — il tetto e' per blocco, non per giro: se
   servono piu' blocchi, si fanno, UNO alla volta (le risposte di un blocco
   decidono il successivo, mai due blocchi insieme). Domande secche, una riga
   l'una, OGNUNA con alternative concrete (a/b/c), mai aperte. Solo su cio' che
   e' ambiguo per chi deve costruire, mai su cio' che e' incompleto in astratto.
   Mai domande a cui la documentazione di progetto risponde gia'. Se l’utente non sa
   rispondere, la risposta E'
   [APERTO-NN]: va bene cosi'. Meglio dieci aperti onesti che tre decisioni
   finte. Non spingerlo a decidere per chiudere il giro: una decisione debole
   diventa un contratto immutabile.
2. **Scrittura** — integra le risposte in SPEC.md e mostra all’utente SOLO il
   delta (cosa e' cambiato e dove). Non riscrivere quello che gia' funziona: le
   SPEC buone si stratificano. Alza la versione e datala.
3. **Giudizio esterno** — vedi sotto. Voto e difetti puntuali.
4. **Esito del giro** — voto 10/10: consegna. Voto inferiore: i difetti elencati
   dal giudice diventano l'agenda del giro successivo (le nuove domande partono
   da li'). L’utente puo' fermarsi prima: il voto raggiunto resta scritto in testa
   alla SPEC, non si finge un 10.

In testa a SPEC.md, sempre: versione, data, taglio dichiarato, ultimo voto del
giudice e data del giudizio; prima della verifica scrivi «giudizio non ancora eseguito».

## Il giudice esterno — mai autovalutarsi
Chi scrive la SPEC non la vota. Il voto di chi ha in contesto la conversazione
non è indipendente.
- **In Claude Code o Codex**: agente separato a contesto fresco. Riceve SOLO SPEC.md e
  la rubric qui sotto — MAI la storia della sessione, mai le risposte dell’utente.
- **Se gli agenti separati non sono disponibili**: prepara SPEC e rubric per una
  sessione indipendente. Segna il giudizio come non eseguito; non inventare il voto.
  La consegna verificata resta in attesa di quel giudizio.

**Rubric (da passare al giudice integralmente):**
Vota 0-10 rispondendo a: "un agente che legge SOLO questa SPEC sa decidere da
solo cosa e' vietato, cosa e' deciso, cosa e' aperto e come si verifica ogni
blocco — senza chiedere e senza indovinare?"
- Prima verifica: il taglio dichiarato in testa (market / function / goal)
  e' coerente col progetto descritto? Se no, e' un difetto da elencare.
- Verdetto per ciascuna delle sezioni 1-7, giudicando 1-2 col criterio del
  taglio dichiarato: SUFFICIENTE / DA MIGLIORARE / ASSENTE. La 8 e' opzionale:
  se assente non e' un difetto, se presente si giudica come le altre.
- 10/10 = sezioni 1-7 tutte SUFFICIENTE + zero incertezze in prosa + ogni
  [APERTO-NN] nel formato obbligatorio. Un [APERTO] ben formato NON abbassa il
  voto: gli aperti onesti sono qualita', non buchi. Un'ipotesi in prosa si'.
- Un elenco di milestone, fasi o date nella SPEC e' un DIFETTO da elencare, non
  un merito: il piano e' `ROADMAP.md`.
- Ogni punto sotto il 10 va motivato con un difetto PUNTUALE e actionable
  (sezione, riga, cosa manca) — mai "si potrebbe arricchire".
- Vietato premiare la lunghezza: prosa in piu' che non aggiunge confini e' un
  difetto, non un merito.

## Il taglio della SPEC — dipende dal progetto, si dichiara al giro 0
Non tutte le SPEC sono da prodotto. Il taglio orienta le sezioni 1-2; le sezioni
3-8 (bloccate, aperte, verifica, confini, obiettivi/mercato, priorita') sono identiche
per tutti i tagli.
- **Market-based** (prodotto per un mercato: SaaS, app per terzi): la sezione 1
  e' utente specifico + dolore specifico (wedge); la 2 e' l'anti-wedge.
- **Function-based** (strumento/software di servizio: monitoraggio, importer,
  CLI, integrazione): la sezione 1 e' l'elenco delle funzioni che DEVE svolgere,
  con input e output osservabili; la 2 e' le funzioni contigue che NON deve
  svolgere, anche se verrebbe comodo.
- **Goal-based** (progetto che esiste per raggiungere un risultato misurabile:
  una metrica, una migrazione, una bonifica): la sezione 1 e' l'obiettivo con
  numero e scadenza + come si misura; la 2 e' le strade escluse per arrivarci.
Un taglio sbagliato produce domande sbagliate: se il progetto non entra in
nessuno dei tre, si dichiara un taglio misto esplicitando quale sezione segue
quale criterio.

## Struttura: 7 sezioni obbligatorie + 1 opzionale, con criteri di sufficienza
Il titolo lo riempi sempre. Il criterio dice se quello che c'e' basta.

1. **Obiettivo e wedge** — criterio secondo il taglio dichiarato (sopra).
   In ogni caso: categoria generica, funzione vaga o obiettivo non misurabile =
   insufficiente.
2. **Fuori scope (anti-wedge)** — sufficiente se elenca cose che a qualcuno
   verrebbe voglia di costruire, secondo il taglio. Vuota o ovvia = non
   protegge da niente.
3. **Decisioni bloccate** — sufficiente se ogni voce dice cosa e' deciso E cosa
   vieta. Sono contratti immutabili: l’agente non le ridiscute mai. Se stanno nel
   CLAUDE.md di progetto, il posto giusto e' qui: sono SPEC, non convenzioni.
4. **Decisioni aperte** — sufficiente se ogni voce ha ID, cosa blocca, ipotesi
   corrente e alternative concrete. Formato obbligatorio:

   ### [APERTO-NN] Domanda in una riga
   Blocca: cosa non si puo' costruire finche' e' aperta
   Ipotesi corrente: quella su cui si sta lavorando, se esiste
   Alternative: (a) ... · (b) ... · (c) ...
   Serve per decidere: cosa concretamente (interviste, dato, test)

   Senza ID e alternative l'aperto non e' risolvibile dentro un perimetro.
5. **Come si verifica** — sufficiente se per ogni blocco funzionale c'e'
   un'azione che l’utente fa da solo, senza leggere codice.
6. **Confini non negoziabili** — vincoli legali, fiscali, di isolamento,
   compliance. Sufficiente se sono verificabili, non aspirazionali.
7. **Obiettivi e mercato (<=30 righe)** — distillato dalla chat di progetto: e' cio'
   che l’agente legge al posto del materiale originale. Sufficiente se sta nel tetto
   e non rimanda a materiale che l’agente non puo' aprire. Oltre 30 righe = insufficiente.
8. **Priorita' di prodotto** (opzionale) — le capacita' della SPEC ordinate per
   valore per l'utente, in prosa o in un elenco corto. Niente milestone, niente
   firme, niente date: e' un input per l'ordinamento di `ROADMAP.md`, non un piano.
   Sufficiente se dice quale capacita' vale piu' di quale e perche'. Se assente,
   `/sdd roadmap` ordina solo per dipendenza: la sezione non blocca nulla.

**Mai in SPEC**: elenchi di milestone o fasi (il piano e' `ROADMAP.md`, lo produce
`/sdd roadmap` dal delta fra SPEC e codice), stato di avanzamento (progress.md),
lavoro tecnico che non cambia cosa l'utente puo' fare (issue GitHub), decisioni
implementative reversibili (le prende l’agente).

## Consegna (a 10/10 o a stop dell’utente)
Elenco secco: voto finale e giri fatti, sezioni sufficienti, sezioni migliorate,
[APERTO-NN] aperti con cosa bloccano. Chiedi approvazione della SPEC prima di passare alla roadmap. Nessun commit o
pubblicazione impliciti. Con SPEC verificata e approvata: prossimo passo `/sdd roadmap`.
Se l’utente ferma prima del 10/10, conserva il voto effettivo e attendi la sua
decisione esplicita se procedere con quei limiti. Se ci
sono aperti bloccanti, un [APERTO] bloccante si risolve nel perimetro della
milestone che lo tocca, oppure quella milestone non parte.

## Anti-pattern
- Scrivere la SPEC in un colpo solo senza domande: il loop E' il metodo
- Votarsi da soli, o "stimare" il voto del giudice per saltare il giro
- Ripresentare al giudice una SPEC invariata sperando in un voto diverso
- Chiudere un [APERTO] con l'ipotesi corrente senza che l’utente decida
- Riscrivere una SPEC valida per uniformarla al template
- Dedurre obiettivi di prodotto dal codice
- Fare domande di cui la documentazione di progetto ha gia' la risposta
