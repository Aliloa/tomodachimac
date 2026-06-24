
from flask import Flask, render_template, redirect, request, session
import models.db as db
import models.mii as mii
import models.users as users
import models.island as island
import models.note as note
import os
from dotenv import load_dotenv

load_dotenv()

server = Flask(__name__)
server.secret_key = os.getenv("SECRET_KEY")

@server.route('/', methods=['GET'])
def connexion():
    return render_template('connexion.html')

@server.route('/profile', methods=['GET'])
def display_profile():
    if 'user' not in session:
        return redirect('/')
    iles = island.getIslandsByUser(session['user']['id_compte'])
    return render_template('profile.html', iles=iles)
    
@server.route('/connexion', methods=['POST'])
def connexion_post():
    pseudo = request.form['pseudo']
    mdp = request.form['mdp']
    user = users.connexion(pseudo, mdp)
    if user:
        session['user'] = user #sauvegarder l'utilisateur dans la session
        return redirect('/profile')
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

@server.route('/create_island', methods=['GET'])
def display_island_form():
    return render_template('create_island.html')

@server.route('/create_island', methods=['POST'])
def add_island():
    if 'user' not in session:
        return redirect('/')
    name = request.form['nom']
    if not name:
        return render_template('create_island.html')
    id_compte = session['user']['id_compte']
    island.addIsland(name, id_compte)
    return redirect('/profile')

@server.route('/rate_island/<int:id_ile>', methods=['GET'])
def display_rate_isalnd(id_ile):
    return render_template('rate_island.html', id_ile=id_ile)

@server.route('/rate_island/<int:id_ile>', methods=['POST'])
def add_rate(id_ile):
    rate = request.form['note']
    note.addNote(rate, id_ile)
    return redirect('/profile')

#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)