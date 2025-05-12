from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

flashcards_db = [
    {"materia": "Matematica", "domanda": "2+2", "risposta": "4"},
    {"materia": "Matematica", "domanda": "5*5", "risposta": "25"},
    {"materia": "Storia", "domanda": "Anno scoperta America", "risposta": "1492"},
    {"materia": "Scienze", "domanda": "Formula acqua", "risposta": "H2O"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/creazione', methods=['GET', 'POST'])
def crea():
    if request.method == 'POST':
        nuova_flashcard = {
            "materia": request.form.get('materia'),
            "domanda": request.form.get('domanda'),
            "risposta": request.form.get('risposta')
        }
        flashcards_db.append(nuova_flashcard)
        return redirect(url_for('home'))
    
    return render_template('creazione.html')

@app.route('/esercitati')
def esercitati():
    materie = list(set(card['materia'] for card in flashcards_db))
    return render_template('esercitazione.html', materie=materie, flashcards=flashcards_db)

if __name__ == '__main__':
    app.run(debug=True)
