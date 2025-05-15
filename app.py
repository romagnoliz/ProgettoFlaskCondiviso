from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

MATERIE = ["Informatica", "Sistemi e Reti", "TPSIT", "Matematica"]
flashcards_db = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/crea', methods=['GET', 'POST'])
def crea():
    if request.method == 'POST':
        nuova_flashcard = {
            "materia": request.form.get('materia'),
            "domanda": request.form.get('domanda'),
            "risposta": request.form.get('risposta')
        }
        flashcards_db.append(nuova_flashcard)
        return redirect(url_for('salva_flashcards'))  # Dopo la creazione, salva la flashcard

    return render_template('creazione.html', materie=MATERIE)


@app.route('/salva', methods=['GET', 'POST'])
def salva_flashcards():

    if request.method == 'POST':
        materia = request.form.get('materia')
        domanda = request.form.get('domanda')
        risposta = request.form.get('risposta')

        if not (materia and domanda and risposta):
            return "Errore: tutti i campi devono essere compilati."

        with open("flashcards_salvate.txt", "a", encoding="utf-8") as f:
            f.write(f"Materia: {materia}\n")
            f.write(f"Domanda: {domanda}\n")
            f.write(f"Risposta: {risposta}\n\n")

        return redirect(url_for('home'))  # Dopo il salvataggio, torna alla home


@app.route('/esercitati')
def esercitati():
    """Legge e mostra le flashcards salvate nel file al cliccare del bottone 'Esercitati'."""
    flashcards_salvate = []

    try:
        with open("flashcards_salvate.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            flashcard = {}

            for line in lines:
                line = line.strip()
                if line.startswith("Materia:"):
                    flashcard["materia"] = line.replace("Materia: ", "")
                elif line.startswith("Domanda:"):
                    flashcard["domanda"] = line.replace("Domanda: ", "")
                elif line.startswith("Risposta:"):
                    flashcard["risposta"] = line.replace("Risposta: ", "")
                elif line == "":
                    if flashcard:  # Se la flashcard è completa, aggiungila alla lista
                        flashcards_salvate.append(flashcard)
                        flashcard = {}

    except FileNotFoundError:
        flashcards_salvate = ["Nessuna flashcard salvata!"]

    return render_template('esercitazione.html', materie=MATERIE, flashcards=flashcards_salvate)


if __name__ == '__main__':
    app.run(debug=True)


