import mysql.connector

class Bdd_Acces():

    def __init__(self, user : str, password : str, host : str, database :str) -> None:
        self.Connect = mysql.connector.connect(
            user="B2B2",
            password="B2B2",
            host="localhost",
            database="bibliotheque"
        ) 

    
Bdd_Biblio = Bdd_Acces()
