from flask import Blueprint, render_template, request
import app.models.modele as modele

etudiants_bp = Blueprint("etudiants", __name__)

@etudiants_bp.route('/')
def accueil():
    etudiants = modele.getData()
    print(etudiants)
    return render_template('liste.html', etudiants=etudiants)

@etudiants_bp.route('/saisie')
def saisie():
    return render_template('form.html')

@etudiants_bp.route('/ajout', methods=['POST'])
def ajout():
    modele.inputData(request.form['nom'])
    return accueil()

@etudiants_bp.route('/supprimer', methods=['POST'])
def supprimer():
    modele.deleteData(request.form['id'])
    return accueil()