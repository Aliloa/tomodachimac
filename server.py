
from flask import Flask, render_template, redirect, request, session
import models.db as db
import models.mii as mii
import models.users as users
import models.island as island
import models.note as note
import models.note as family
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

@server.route('/all_islands', methods=['GET'])
def display_all_islands():
    ile = island.getAllIslands()
    return render_template('all_islands.html', ile=ile)

@server.route('/island/<int:id_ile>', methods=['GET'])
def showIsland(id_ile):
    islandName = island.getIslandById(id_ile)["nom_ile"]

    idUser = session['user']['id_compte'] # getting user id
    
    nbMiis = mii.CountAllIslandMiis(id_ile) # this function returns a number directly, no dictionnary
    # avgNote = note.getAverageIslandNote(id_ile)
    IslandMiis = mii.getAllUserIslandMiis(idUser, id_ile) # gets images and names of miis

    return render_template('island.html', islandName=islandName, avgNote="1", nbMiis=nbMiis, IslandMiis=IslandMiis)

@server.route('/create_mii/<int:id_ile>', methods=['GET'])
def display_mii_creator(id_ile):
    return render_template('create_mii.html')

@server.route('/create_mii/<int:id_ile>', methods=['POST'])
def create_mii(id_ile):
    # all mii creation informations (user input)
    name = request.form['name']
    age = request.form['age']
    sex = request.form['sex']
    personnality = request.form['personnality']
    image = request.files['image']

    # information for db :
    idUser = session['user']['id_compte']

    if image and image.filename != '':
        image.save(f"static/miis/{image.filename}") # saving the image the user imported

    allMiis = mii.getAllUserIslandMiis(idUser, id_ile)

    mii.createMii(name, sex, age, personnality, image, idUser, id_ile)

    return render_template('create_mii.html', IdIsland=id_ile, allMiis=allMiis)

@server.route('/display_mii/<int:id_mii>', methods=['GET'])
def display_mii(id_mii):
    miiInfo = mii.getAllMiiInformations(id_mii)
    name =  mii.getAllMiiInformations(id_mii)['nom_mii']
    sex =  mii.getAllMiiInformations(id_mii)['sex']
    age =  mii.getAllMiiInformations(id_mii)['age']
    personnality =  mii.getAllMiiInformations(id_mii)['personnalite']
    image =  mii.getAllMiiInformations(id_mii)['image']

    crushInfo = mii.getMiiCrushInformations(id_mii)
    familyName = family.getFamilyName(miiInfo['id_famille'])
    partnerInfo = mii.getMiiPartnerInformations(id_mii)

    return render_template('display_mii.html', miiInfo=miiInfo, crushInfo=crushInfo, partnerInfo=partnerInfo, familyName=familyName)

@server.route('/display_mii/<int:id_family>/<int:id_mii>', methods=['GET'])
def display_familly(id_mii, id_family):
    nbMembers = family.countFamilyMembers(id_family)

    # parents
    parents = mii.getMiiParents(id_mii)
    idFather = parents['id_pere']
    fatherInfo = mii.getAllMiiInformations(idFather)
    idMother = parents['id_mere']
    motherInfo = mii.getAllMiiInformations(idMother)
    # siblings
    siblingsInfo = mii.getMiiSiblings(id_mii)
    siblingsIds = [siblingInfo['id_mii'] for siblingInfo in siblingsInfo]
    # others
    allMembers = family.getAllFamilyMembers(id_family)
    otherMembers = []
    excludeIds = [id_mii, idFather, idMother] + siblingsIds

    for member in allMembers:
        if member['id_mii'] not in excludeIds:
            otherMembers.append(member)

    return render_template('family.html', nbMembers=nbMembers, otherMembers=otherMembers, fatherInfo=fatherInfo, motherInfo=motherInfo, siblingsInfo=siblingsInfo)


#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)