
from flask import Flask, render_template, redirect, request, session
import models.db as db
import models.mii as mii
import models.users as users
import models.island as island
import models.note as note
import models.family as family
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
        return render_template('connexion.html', erreurconnexion="Identifiants invalides")

@server.route('/inscription', methods=['POST'])
def inscription():
    pseudo = request.form['pseudo']
    mdp = request.form['mdp']
    existingUser = users.getUserByPseudo(pseudo)
    if existingUser:
        return render_template('connexion.html', erreurinscription="Ce pseudo est déjà pris")
    user = users.inscription(pseudo, mdp)
    user = users.connexion(pseudo, mdp)  # on se connecte direct
    session['user'] = user
    return render_template('profile.html')

@server.route('/deconnexion', methods=['GET'])
def deconnexion():
    session.clear()
    return redirect('/')

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

@server.route('/delete_island/<int:id_ile>', methods=['POST'])
def delete_island(id_ile):
    #sécurité double vérification avant de supprimer
    ile = island.getIslandById(id_ile)
    if ile['id_compte'] != session['user']['id_compte']:
        return redirect('/profile')  # ou retourner une erreur 403
    # supprimer dabord tous les mii associés
    mii.deleteMiisByIslandId(id_ile)
    island.deleteIslandById(id_ile)
    return redirect('/profile')

@server.route('/rename_island/<int:id_ile>', methods=['POST'])
def rename_island(id_ile):
    new_name = request.form['nom']
    island.renameIsland(id_ile, new_name)
    return redirect('/profile')

@server.route('/all_islands', methods=['GET'])
def display_all_islands():
    iles = island.getAllIslands()
    for ile in iles:
        ile['moyenne'] = note.getAverageIslandNote(ile['id_ile'])
    return render_template('all_islands.html', iles=iles)

@server.route('/island/<int:id_ile>', methods=['GET'])
def showIsland(id_ile):
    ile = island.getIslandById(id_ile)
    idUser = session['user']['id_compte'] # getting user id
    
    nbMiis = mii.CountAllIslandMiis(id_ile) # this function returns a number directly, no dictionnary
    avgNote = note.getAverageIslandNote(id_ile)
    IslandMiis = mii.getAllIslandMiis(id_ile) # gets images and names of miis
    owner = users.getUserByIslandId(id_ile)['pseudo']

    return render_template('island.html',ile=ile, avgNote=avgNote, nbMiis=nbMiis, IslandMiis=IslandMiis,owner=owner )

@server.route('/create_mii/<int:id_ile>', methods=['GET'])
def display_mii_creator(id_ile):
    # information for db :
    idUser = session['user']['id_compte']

    allIslandMiis = mii.getAllIslandMiis(id_ile)
    allIslandFamilies = family.getFamiliesByIsland(id_ile)
    islandName = island.getIslandById(id_ile)['nom_ile']

    return render_template('create_mii.html', islandName=islandName, id_ile=id_ile, allIslandMiis=allIslandMiis, allIslandFamilies=allIslandFamilies)

@server.route('/create_mii/<int:id_ile>', methods=['POST'])
def create_mii(id_ile):
    # all mii creation informations (user input)
    name = request.form['name']
    age = request.form['age']
    sex = request.form['sex']
    personnality = request.form['personnality']
    image = request.files['image']

    # crush :
    crush_choice = request.form['crush_choice']
    if crush_choice != 'none':
        idCrush = int(crush_choice)
    else:
        idCrush = None
    # partner :
    partner_choice = request.form['partner_choice']
    if partner_choice != 'none':
        idPartner = int(partner_choice)
    else:
        idPartner = None
    # father :
    father_choice = request.form['father_choice']
    if father_choice != 'none':
        idFather = int(father_choice)
    else:
        idFather = None
    # mother :
    mother_choice = request.form['mother_choice']
    if mother_choice != 'none':
        idMother = int(mother_choice)
    else:
        idMother = None
    # family name :
    family_choice = request.form['family_choice']
    familyName = request.form['family_name']
    if family_choice != 'none':
        idFamily = int(family_choice)
    elif familyName:
        idFamily = family.createFamily(familyName)  # returns new id_famille via cursor.lastrowid
    else:
        idFamily = None

    # information for db :
    idUser = session['user']['id_compte']

    imageFilename = None
    if image and image.filename != '':
        imageFilename = image.filename
        image.save(f"static/miis/{image.filename}") # saving the image the user imported

    if familyName:
        family.createFamily(familyName)

    mii.createMii(name, sex, age, personnality, imageFilename, idUser, id_ile, idCrush, idPartner, idFamily, idFather, idMother)

    return redirect('/profile')

@server.route('/display_mii/<int:id_mii>', methods=['GET'])
def display_mii(id_mii):
    miiInfo = mii.getAllMiiInformations(id_mii)
    crushInfo = mii.getMiiCrushInformations(id_mii)
    if miiInfo['id_famille'] is not None:
        familyName = family.getFamilyName(miiInfo['id_famille'])
    else:
        familyName = None
    partnerInfo = mii.getMiiPartnerInformations(id_mii)

    IslandMiis=mii.getAllIslandMiis(miiInfo['id_ile'])
    ile=island.getIslandById(miiInfo['id_ile'])

    return render_template('display_mii.html', miiInfo=miiInfo, crushInfo=crushInfo, partnerInfo=partnerInfo, familyName=familyName, IslandMiis=IslandMiis, ile=ile)

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

@server.route('/delete_mii/<int:id_mii>', methods=['POST'])
def delete_mii(id_mii):
    #sécurité double vérification avant de supprimer
    selectedMii = mii.getMiiById(id_mii)
    idUser = users.getUserByIslandId(selectedMii['id_ile'])['id_compte']

    if idUser != session['user']['id_compte']:
        return redirect('/profile')  # ou retourner une erreur 403
    
    mii.deleteMiiById(id_mii)

    return redirect('/profile')

#pour voir le lien du serveur
if __name__=="__main__":
    server.run(debug=True)