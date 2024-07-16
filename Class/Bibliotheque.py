from BDD import BDD_Acces

class Bibliotheque():
    def __init__(self, db_acces: BDD_Acces):
        self.db_acces = db_acces

    def add_item(self, nom, type_id, auteur_id, genre_id, emprunt_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        add_item_query = 'INSERT INTO item (nom, type_id, auteur_id, genre_id, emprunt_id) VALUES (%s, %s)'
        item_data = (nom, type_id, auteur_id, genre_id, emprunt_id)
        cursor.execute(add_item_query, item_data)
        conn.commit()
        cursor.close()

    def remove_item(self, item_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        delete_item_query = 'DELETE FROM item WHERE id = %s'
        cursor.execute(delete_item_query, item_id)
        conn.commit()
        cursor.close()

    def add_auteur(self, last_name, first_name):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        add_auteur_query = 'INSERT INTO auteur (nom, prenom) VALUES (%s, %s, %s)'
        author_data = (last_name, first_name)
        cursor.execute(add_auteur_query, author_data)
        conn.commit()
        cursor.close()

    def remove_auteur(self, author_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        delete_auteur_query = 'DELETE FROM auteur WHERE id = %s'
        cursor.execute(delete_auteur_query, author_id)
        conn.commit()
        cursor.close()