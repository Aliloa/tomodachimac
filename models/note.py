from .db import mydb

def getNote():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM note")
    return cur.fetchall()

def addNote(note, id_ile):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO note (note, id_ile) VALUES (%s, %s)", (note, id_ile))
    mydb.commit()
    mycursor.close()