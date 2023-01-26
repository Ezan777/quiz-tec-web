class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False

questions = [Question("La divisione tra contenuto e presentazione di un sito web contribuisce ad abbassare il suo peso totale", "V"),
    Question("La divisione tra contenuto e presentazione di un sito web contribuisce a migliorarne la sua manutenibilità", "V"),
    Question("La divisione tra contenuto e presentazione contribuisce ad un buon posizionamento nei risultati dei motori di ricerca", "V"),
    Question("Una struttura organizzativa gerarchica, per essere efficiente, deve essere ampia e poco profonda", "V"),
    Question("La divisione tra contenuto e comportamento contribuisce ad abbassare la dimensione totale di un sito web.", "V"),
    Question("Le tabelle sono sempre un ostacolo alla facile comprensione del contenuto e per questo andrebbero evitate ove possibile", "V"),
    Question("Un test esaustivo dell’accessibilità della pagina non può essere fatto in modo automatico.", "V"),
    Question("Una struttura organizzativa, per essere efficiente, deve essere ampia e poco profonda", "V"),
    Question("La validazione del codice HTML e CSS di un sito web è condizione necessaria per garantire la sua accessibilità.", "V"),
    Question("Il layout a schede va facilmente incontro a problemi di manutenzione nel tempo.", "V"),
    Question("Le convenzioni interne devono sempre essere rispettate per evitare di disorientare l’utente", "V"),
    Question("È buona regola segnalare i link che portano ad elementi diversi da pagine web (es. pdf)", "V"),
    Question("Le WCAG richiedono di identificare in modo diverso i link visitati dai link non visitati.", "V"),
    Question("La divisione tra contenuto e presentazione di una pagina web e condizione necessaria e sufficiente per garantirne l’accessibilità", "F"),
    Question("La presenza di una parola nel metatag keywords è condizione sufficiente per modificare il posizionamento di una pagina web nelle pagine di risposta dei motori di ricerca", "F"),
    Question("La presenza di una barra con il path di contesto in una pagina web evita il sovraccarico cognitivo dell’utente", "F"),
    Question("Il contenuto del metatag author influenza il posizionamento di una pagina web nelle pagine di risposta dei motori di ricerca", "F"),
    Question("Il layout a schede è fortemente consigliato in caso di tassonomie con molte voci nello stesso livello e poco profonde", "F"),
    Question("La divisione tra contenuto e comportamento aiuta a migliorare il posizionamento nelle risposte dei motori di ricerca", "F"),
    Question("La divisione tra struttura e presentazione non contribuisce al posizionamento della pagina nelle SERP del motore di ricerca.", "F"),
    Question("Il contenuto del tag <title> deve sempre esprimere prima il contesto generale e poi quello particolare", "F"),
    Question("È buona norma utilizzare icone con bandiere per indicare link a pagine in altre lingue", "F"),
    Question("L’uso dei menù a scomparsa non influisce sull'accessibilità di un sito.", "F"),
    Question("L’uso dei colori non influenza l’accessibilità del sito.", "F"),
    Question("Il tag <input> in XHTML può essere figlio diretto di una <form>", "F"),
    Question("Permettere la fruibilità di una pagina mediante screen reader è condizione necessaria e sufficiente a garantirne l’accessibilità?", "F"),
    Question("Il numero massimo di voci in un menu è 6", "F"),
    Question("La separazione tra struttura, contenuto e presentazione aiuta il posizionamento nelle pagine SERP?", "F"),
]