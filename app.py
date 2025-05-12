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
        return redirect(url_for('home'))
    
    return render_template('creazione.html', materie=MATERIE)

@app.route('/esercitati')
def esercitati():
    return render_template('esercitazione.html', materie=MATERIE, flashcards=flashcards_db)

if __name__ == '__main__':
    app.run(debug=True)