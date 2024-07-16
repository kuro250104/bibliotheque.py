from BDD import BDD_Acces
from datetime import date

class EmpruntsManager:
    def __init__(self, db_acces: BDD_Acces):
        self.db_acces = db_acces

    def add_emprunt(self, emprunt, date_debut, date_fin, user_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO emprunt (emprunt, date_debut, date_fin, user_id)
        VALUES (%s, %s, %s, %s)
        ''', (emprunt, date_debut, date_fin, user_id))
        conn.commit()
        cursor.close()

    def delete_emprunt(self, emprunt_id):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        cursor.execute('DELETE FROM emprunt WHERE id = %s', (emprunt_id,))
        conn.commit()
        cursor.close()

    def modify_emprunt(self, emprunt_id, emprunt=None, date_debut=None, date_fin=None, user_id=None):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        if emprunt:
            cursor.execute('UPDATE emprunt SET emprunt = %s WHERE id = %s', (emprunt, emprunt_id))
        if date_debut:
            cursor.execute('UPDATE emprunt SET date_debut = %s WHERE id = %s', (date_debut, emprunt_id))
        if date_fin:
            cursor.execute('UPDATE emprunt SET date_fin = %s WHERE id = %s', (date_fin, emprunt_id))
        if user_id:
            cursor.execute('UPDATE emprunt SET user_id = %s WHERE id = %s', (user_id, emprunt_id))
        conn.commit()
        cursor.close()

    def show_emprunts(self):
        conn = self.db_acces.Connect
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emprunt')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()