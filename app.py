from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['DATA_FOLDER'] = 'data'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crea', methods=['GET', 'POST'])
def crea():
    if request.method == 'POST':
        materia = request.form['materia']
        domanda = request.form['domanda']
        risposta = request.form['risposta']

        filename = secure_filename(f"{materia}.txt")
        filepath = os.path.join(app.config['DATA_FOLDER'], filename)
        
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"{domanda}|||{risposta}\n")
            
        return render_template('crea.html', success=True)
    
    return render_template('crea.html', success=False)

@app.route('/esercitati')
def esercitati():
    materie = []
    for filename in os.listdir(app.config['DATA_FOLDER']):
        if filename.endswith('.txt'):
            materie.append(filename[:-4])
    
    return render_template('materie.html', materie=materie)

@app.route('/esercitati/<materia>')
def esercitati_materia(materia):
    filename = secure_filename(f"{materia}.txt")
    filepath = os.path.join(app.config['DATA_FOLDER'], filename)
    
    flashcard = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if '|||' in line:
                    domanda, risposta = line.strip().split('|||')
                    flashcard.append({'domanda': domanda, 'risposta': risposta})

    
    return render_template('esercitati.html', materia=materia, flashcard=flashcard)

if __name__ == '__main__':
    app.run(debug=True)