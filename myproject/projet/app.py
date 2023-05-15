from flask import Flask,render_template
from modele.test import Modele
import whisper
app = Flask(__name__)
app.secret_key ='SECRET_KEY'
@app.route("/")
def hello_world():
    posts=['post1','post1','post1','post1']
    return render_template('index.html',posts=posts)

@app.route('/upload',methods=['POST'])
def upload():
    model = whisper.load_model("tiny")
    # Traiter le fichier audio avec le modèle
    
    transcription = model.transcribe('36855.mp3')

    # Afficher la transcription
    return transcription


if __name__ == "__main__":
    app.run(debug=True)