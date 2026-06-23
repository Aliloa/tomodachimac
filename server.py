
from flask import Flask, render_template, request
import app.models.modele as modele

server = Flask(__name__)

@server.route('/')
def accueil():
    etudiants = modele.getData()
    print(etudiants)
    return render_template('liste.html', etudiants=etudiants)

@server.route('/saisie')
def saisie():
    return render_template('form.html')

@server.route('/ajout', methods=['POST'])
def ajout():
    modele.inputData(request.form['nom'])
    return accueil()

@server.route('/supprimer', methods=['POST'])
def supprimer():
    modele.deleteData(request.form['id'])
    return accueil()

#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)