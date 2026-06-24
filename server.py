
from flask import Flask, render_template, redirect, request, session
import models.db as db
import models.mii as mii
import models.users as users
import models.island as island
import os
from dotenv import load_dotenv

load_dotenv()

server = Flask(__name__)
server.secret_key = os.getenv("SECRET_KEY")

@server.route('/', methods=['GET'])
def connexion():
    return render_template('connexion.html')

@server.route('/connexion', methods=['POST'])
def connexion_post():
    pseudo = request.form['pseudo']
    mdp = request.form['mdp']
    user = users.connexion(pseudo, mdp)
    if user:
        session['user'] = user #sauvegarder l'utilisateur dans la session
        return render_template('profile.html')
    else:
        return render_template('connexion.html', erreur="Identifiants invalides")

@server.route('/inscription', methods=['POST'])
def inscription():
    pseudo = request.form['pseudo']
    mdp = request.form['mdp']
    user = users.inscription(pseudo, mdp)
    user = users.connexion(pseudo, mdp)  # on se connecte direct
    session['user'] = user
    return render_template('profile.html')

#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)

@server.route('/create_island', methods=['POST'])
def add_island():
    if 'user' not in session:
        return redirect('/')
    name=request.form.get('name','').strip()
    if not name:
        return render_template('create_island.html')
    id_compte = session['user']['id_compte']
    succes = island.addIsland(name, id_compte)
    
    if not succes:
        return render_template('create_island.html', erreur="Vous avez déjà une île avec ce nom.")
    
    return redirect('/profile')
