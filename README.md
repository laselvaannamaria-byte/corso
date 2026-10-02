# SQL: interrogare e modificare una base di dati

Percorso introduttivo per imparare a leggere una tabella, selezionare dati con query e usare i principali comandi SQL in modo consapevole.

**Classe:** [CLASSE E INDIRIZZO] · **Durata:** 6 ore · **Prerequisiti:** tabelle e record; uso di un editor di testo; concetto di dato e di condizione.

## Obiettivi di apprendimento (osservabili)

Alla fine dell'UdA lo studente sa:
1. distinguere tabella, campo, record e chiave primaria;
2. scrivere query `SELECT` con `WHERE`, `ORDER BY` e `LIMIT` per trovare e ordinare dati;
3. inserire, aggiornare ed eliminare record con `INSERT`, `UPDATE` e `DELETE`, verificando prima quali righe saranno coinvolte;
4. creare una tabella semplice con `CREATE TABLE` e spiegare il ruolo dei vincoli `PRIMARY KEY` e `NOT NULL`;
5. leggere e correggere una query, motivando il risultato atteso;
6. usare un assistente IA secondo le regole del patto d'aula e spiegare le query che consegna.

## Misconcezioni affrontate

- `SELECT` non modifica i dati: restituisce una vista dei record richiesti;
- senza `WHERE`, `UPDATE` e `DELETE` possono agire su tutte le righe della tabella;
- il testo va racchiuso tra apici, mentre i numeri normalmente no;
- `NULL` indica un valore assente e non si verifica con `= NULL`.

## Sequenza delle lezioni

| Lezione | Attività | Livello IA (0-4) | AI-proof / AI-powered | Materiali e agenti |
|---|---|---|---|---|
| 1 | Tabelle, campi, record e chiavi; lettura di una tabella di esempio | 0 | AI-proof: riconoscere struttura e chiave primaria su carta | Schema e tabella di esempio |
| 2 | `SELECT`, scelta delle colonne e alias | 1 | AI-proof: prevedere il risultato prima dell'esecuzione | Database di esercitazione |
| 3 | Filtri con `WHERE`, operatori, `AND`, `OR`, `LIKE` e `IS NULL` | 2 | AI-powered: chiedere feedback su query e casi limite, poi verificarli | Esercizi PRIMM |
| 4 | Ordinamento e limiti con `ORDER BY` e `LIMIT`; confronto tra risultati | 0 | AI-proof: scrivere query a partire da richieste in linguaggio naturale | Verifica breve senza IA |
| 5 | Comandi di modifica `INSERT`, `UPDATE`, `DELETE`; attenzione a `WHERE` | 1 | AI-proof: individuare query pericolose e prevederne l'effetto | Dataset di prova |
| 6 | `CREATE TABLE`, vincoli e prova pratica riepilogativa | 2 | AI-powered: revisione delle query con spiegazione delle correzioni | Consegna pratica e rubriche |

*Livelli: 0 = IA esclusa · 1 = IA che spiega · 2 = IA che dà feedback · 3 = IA oggetto di studio · 4 = IA collaboratrice. Almeno una lezione di livello 0 e almeno una verifica AI-proof.*

## Comandi SQL di riferimento

Gli esempi usano una tabella `studenti` con i campi `id`, `nome`, `classe` e `media`. La sintassi può variare leggermente in base al database utilizzato.

```sql
-- Leggere tutti i campi e filtrare i risultati
SELECT nome, media
FROM studenti
WHERE media >= 7
ORDER BY media DESC;

-- Inserire un record
INSERT INTO studenti (id, nome, classe, media)
VALUES (1, 'Ada', '4A', 8.5);

-- Aggiornare solo il record identificato
UPDATE studenti
SET media = 9
WHERE id = 1;

-- Eliminare solo il record identificato
DELETE FROM studenti
WHERE id = 1;

-- Creare una tabella con chiave primaria
CREATE TABLE studenti (
	id INTEGER PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	classe VARCHAR(10),
	media DECIMAL(4, 2)
);
```

Prima di eseguire `UPDATE` o `DELETE`, controllare con una `SELECT` la condizione `WHERE`: senza filtro si rischia di modificare o cancellare tutte le righe.

## Agenti per gli studenti

Istruzioni e collaudo nella cartella [`agenti/`](agenti/). Un eventuale agente può aiutare a interpretare gli errori SQL, ma lo studente deve saper spiegare e verificare ogni query.

## Artefatti

 Usa il [Laboratorio SQL interattivo](artefatti/laboratorio-sql.html): un esercitatore autonomo per esplorare tabelle e provare query `SELECT`, `INSERT`, `UPDATE`, `DELETE` e `CREATE TABLE`.

## Verifiche

- AI-proof: `verifiche/ai-proof/`
- AI-powered con evidenze: `verifiche/ai-powered/`
- Rubriche: `verifiche/rubriche/`
- Test automatici (eseguiti da GitHub Actions a ogni push): `verifiche/test/`

## Uso dell'IA nella preparazione di questo kit

Vedi [`DIARIO_DI_BORDO.md`](DIARIO_DI_BORDO.md).

## Patto d'aula

[`PATTO_IA.md`](PATTO_IA.md)

## Limiti noti

- La sintassi di alcuni comandi e tipi di dato cambia tra SQLite, MySQL, PostgreSQL e altri sistemi: indicare alla classe il DBMS usato negli esercizi.
- Usare un database di prova e dati fittizi; non eseguire comandi di modifica su archivi reali senza autorizzazione e backup.

## Licenze

Codice: MIT (file `LICENSE`). Materiali didattici: CC BY 4.0.
