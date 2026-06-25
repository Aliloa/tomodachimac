from .db import mydb

def getNote():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM note")
    return mycursor.fetchall()

def addNote(note, id_ile):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO note (note, id_ile) VALUES (%s, %s)", (note, id_ile))
    mydb.commit()
    mycursor.close()

def getNotesByIslandId(id_ile):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM note WHERE id_ile= %s", (id_ile,))
    return mycursor.fetchall()