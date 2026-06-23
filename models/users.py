from .db import mydb

def connexion(pseudo, mdp):
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE pseudo=%s AND mdp=%s", (pseudo, mdp))
    return cur.fetchone()