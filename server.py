
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

@server.route('/island', methods=['GET'])
def showIsland():
    islandName = request.args.get('nom_ile') # getting island name

    idUser = session['user']['id_compte'] # getting user id
    idIsland = island.getAllIslandInformation(islandName)['id_island'] # getting island ID
    
    nbMiis = mii.CountAllIslandMiis(idIsland) # this function returns a number directly, no dictionnary
    avgNote = note.getAverageIslandNote(idIsland)
    IslandMiis = mii.getAllUserIslandMiis(idIsland) # gets images and names of miis

    return render_template('island.html', islandName=islandName, avgNote=avgNote, nbMiis=nbMiis, IslandMiis =IslandMiis)

@server.route('/create_mii', methods=['POST'])
def create_mii():
    # all mii creation informations (user input)
    name = request.form['name']
    age = request.form['age']
    sex = request.form['sex']
    personnality = request.form['personnality']
    image = request.files['image']

    # information for db :
    idUser = session['user']['id_compte']
    idIsland = request.form['id_ile']

    if image and image.filename != '':
        image.save(f"static/miis/{image.filename}") # saving the image the user imported

    mii.createMii(name, sex, age, personnality, image, idUser, idIsland)

    return render_template('create_mii.html')

#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)