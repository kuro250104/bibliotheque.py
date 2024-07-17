from mysql.connector import Error
from BDD import BDD_Acces

class User:
    def __init__(self, db_acces: BDD_Acces):
        self.db_acces = db_acces

    def add_user(self, name, surname, address):
        try:
            conn = self.db_acces.Connect
            cursor = conn.cursor()
            add_user_query = 'INSERT INTO utilisateur (nom, prenom, adresse) VALUES (%s, %s, %s)'
            user_data = (name, surname, address)
            cursor.execute(add_user_query, user_data)
            conn.commit()
            cursor.close()
            conn.close()
            print(f"Utilisateur {name} {surname} ajouté avec succès")
        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

    def remove_user(self, id):
        try:
            conn = self.db_acces.Connect
            cursor = conn.cursor()
            remove_user_query = 'DELETE FROM utilisateur WHERE id = %s'
            user_data = ( int(id),)
            cursor.execute(remove_user_query, user_data)
            conn.commit()
            cursor.close()
            conn.close()
            print(f"Utilisateur supprimé avec succès")
        except Error as e:
            print(f"Erreur lors de la suppression de l'utilisateur : {e}")
