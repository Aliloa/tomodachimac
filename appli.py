import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
    )

mycursor = mydb.cursor()

# mycursor.execute('''create table etudiants (id int primary key,
#                 nom varchar(50)
#                 )''')
# mydb.commit()

# mycursor.execute('''insert into etudiants values
#                 (1,'Bob leponge'),
#                 (2,'Dora lexporatrice'),
#                 (3,'Koro-sensei')''')
# mydb.commit()

# On rechercher, et on affiche tout
mycursor.execute('''select * from etudiants''')
etuds = mycursor.fetchall()
print(etuds)

# on recharge, car on est arrivé au bout de la liste
print('---------------------')
mycursor.execute('''select * from etudiants''')
print(mycursor.fetchone())

# On continue la liste (on a déja lu le premier)
for etud in mycursor:
    print(etud)

ajout = input("quel nom voulez-vous ajouter ?")

mycursor.execute("INSERT INTO etudiants (nom) VALUES (%s)", (ajout,))
mydb.commit()

delete_id = input("entrez l'ID de l'element que vous voulez supprimer : ")

mycursor.execute("DELETE FROM etudiants WHERE id = %s", (delete_id,))
mydb.commit()

# Pour afficher les modifications à la fin 
print('---------------------')
mycursor.execute('''select * from etudiants''')
print(mycursor.fetchone())
for etud in mycursor:
    print(etud)

mycursor.close()
