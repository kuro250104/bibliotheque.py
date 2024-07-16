import mysql.connector
from datetime import date
from mysql.connector import Error
import BDD

class Utilisateur:
    def __init__(self, id, nom, prenom, adresse,):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse


    def ajouter(self, bdd_acces):
        try:
            cursor = bdd_acces.Connect.cursor()
            sql = """
            INSERT INTO utilisateur (nom, prenom, adresse)
            VALUES (%s, %s, %s)
            """
            val = (self.nom, self.prenom, self.adresse, )
            cursor.execute(sql, val)
            bdd_acces.Connect.commit()
            print(f"Utilisateur {self.nom} {self.prenom} ajouté avec succès")
        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

