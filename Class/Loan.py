from BDD import BDD_Acces


class LoanManager:
    def __init__(self, db_acces: BDD_Acces):
        self.db_acces = db_acces

    def add_loan(self, emprunt, date_debut, date_fin, user_id):
        try:
            conn = self.db_acces.Connect
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO emprunt (emprunt, date_debut, date_fin, user_id)
            VALUES (%s, %s, %s, %s)
            ''', (emprunt, date_debut, date_fin, user_id))
            conn.commit()
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'emprunt: {e}")
        finally:
            cursor.close()

    def modify_loan(self, emprunt_id, emprunt=None, date_debut=None, date_fin=None, user_id=None):
        try:
            conn = self.db_acces.Connect
            cursor = conn.cursor()
            if emprunt is not None:
                cursor.execute('UPDATE emprunt SET emprunt = %s WHERE id = %s', (emprunt, emprunt_id))
            if date_debut is not None:
                cursor.execute('UPDATE emprunt SET date_debut = %s WHERE id = %s', (date_debut, emprunt_id))
            if date_fin is not None:
                cursor.execute('UPDATE emprunt SET date_fin = %s WHERE id = %s', (date_fin, emprunt_id))
            if user_id is not None:
                cursor.execute('UPDATE emprunt SET user_id = %s WHERE id = %s', (user_id, emprunt_id))
            conn.commit()
        except Exception as e:
            print(f"Erreur lors de la modification de l'emprunt: {e}")
        finally:
            cursor.close()

    def show_loan(self):
        try:
            conn = self.db_acces.Connect
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM emprunt')
            rows = cursor.fetchall()
            for row in rows:
                loan_statut = "emprunté" if row[1] == 1 else "pas emprunté"
                print(
                    f"Détails de l'emprunt: ID: {row[0]}, Statut: {loan_statut}, Date début: {row[2]}, Date fin: {row[3]}, Utilisateur ID: {row[4]}")
        except Exception as e:
            print(f"Erreur lors de l'affichage des emprunts: {e}")
        finally:
            cursor.close()

    def show_one_loan(self, emprunt_id):
        try:
            conn = self.db_acces.Connect
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM emprunt WHERE id = %s', (emprunt_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Erreur lors de l'affichage de l'emprunt: {e}")
        finally:
            cursor.close()

        if row:
            emprunt_statut = "emprunté" if row[1] == 1 else "pas emprunté"
            print(
                f"Détails de l'emprunt: ID: {row[0]}, Statut: {emprunt_statut}, Date début: {row[2]}, Date fin: {row[3]}, Utilisateur ID: {row[4]}")
        else:
            print(f"Aucun emprunt trouvé avec l'ID: {emprunt_id}")
