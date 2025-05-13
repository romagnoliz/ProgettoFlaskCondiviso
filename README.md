# Progetto di introduzione a Flask

## Struttura del progetto
- app.py -> File core dell'applicazione per avviare la webapp
- templates -> Cartella contenente tutti i template HTML
    - base.html -> Template base con layout comune per tutte le pagine HTML (solitamente header, footer, etc..)
    - home.html -> Homepage della webapp
    - product_detail.html -> Pagina dettaglio del prodotto selezionato
    - contact.html -> Form di contatto
    - login.html -> Pagina di login
    - dashboard.html -> Dashboard (visibile solo da admin)
    - 404.html -> Pagina errore 404
    - 500.html -> Pagina errore 500

## Concetti proposti
- Routing: Definizione di percorsi URL con @app.route()
- Template con Jinja2: Ereditarietà dei template, cicli, condizioni
- Gestione dei form: Lettura dei dati inviati con i metodi GET e POST
- Session: Gestione dello stato utente tra le richieste
- Flash messages: Notifiche temporanee per l'utente
- Gestione errori: Personalizzazione delle pagine di errore 404 e 500
- Autenticazione: Semplice sistema di login/logout
- Parametri URL dinamici: Come in /product/<int:product_id>
- Reindirizzamenti: Con redirect() e url_for()

## Come eseguire l'applicazione
Aprire un terminale dalla cartella principale del progetto:
- Creazione ambiente virtuale: python -m venv venv
- Attivazione ambiente virtuale:
    - Windows: venv\Scripts\activate
    - macOS/Linux: source venv/bin/activate
- Installazione delle dipendenze e librerie: pip install -r requirements.txt
- Start della webapp: python app.py
- Visita http://localhost:5000 in un browser (meglio Google Chrome)