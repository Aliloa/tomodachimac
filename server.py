
from flask import Flask, render_template, request
import modele as modele

server = Flask(__name__)

@server.route('/')
def accueil():
    users = modele.getData()
    print(users)
    return render_template('liste.html', users=users)

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

@server.route('/connexion', methods=['GET'])
def connexion():
    return render_template('connexion.html')

@server.route('/connexion', methods=['POST'])
def connexion():
    pseudo = request.form['pseudo']
    mdp = request.form['mdp']
    user = modele.connexion(pseudo, mdp)
    if user:
        return render_template('profile.html')
    else:
        return render_template('login.html', erreur="Identifiants invalides")

#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)