from BDD import BDD_Acces

class Bibliotheque():
    def __init__(self, db_acces: BDD_Acces):
        self.db_acces = db_acces

    def add_item(self, name, address, type_id, auteur_id, genre_id, emprunt_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        add_item_query = 'INSERT INTO item (name, address, type_id, auteur_id, genre_id, emprunt_id) VALUES (%s, %s, %s, %s, %s, %s)'
        item_data = (name, address, type_id, auteur_id, genre_id, emprunt_id)
        cursor.execute(add_item_query, item_data)
        conn.commit()
        cursor.close()

    def remove_item(self, item_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        delete_item_query = 'DELETE FROM item WHERE id = %s' % item_id
        cursor.execute(delete_item_query)
        conn.commit()
        cursor.close()

    def add_author(self, name, surname):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        add_auteur_query = 'INSERT INTO auteur (name, surname) VALUES (%s, %s)'
        author_data = (name, surname)
        cursor.execute(add_auteur_query, author_data)
        conn.commit()
        cursor.close()

    def get_table(self, table_name):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        get_table_query = 'SELECT * FROM %s' % table_name
        cursor.execute(get_table_query)
        result = cursor.fetchall()
        cursor.close()
        return result