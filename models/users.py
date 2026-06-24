from .db import mydb
import hashlib

def connexion(pseudo, mdp):
    mdp_hashe = hashlib.sha256(mdp.encode()).hexdigest()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM compte WHERE pseudo=%s AND mdp=%s", (pseudo, mdp_hashe))
    return mycursor.fetchone()

def inscription(pseudo, mdp):
    mdp_hashe = hashlib.sha256(mdp.encode()).hexdigest()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO compte (pseudo, mdp) VALUES (%s, %s)", (pseudo, mdp_hashe))
    mydb.commit()
    mycursor.close()