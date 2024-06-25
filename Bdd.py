import mysql.connector

class Bdd_Acces():

    def __init__(self, Getuser : str, Getpassword : str, Gethost : str, Getdatabase :str) -> None:
        self.Connect = mysql.connector.connect(
            user= Getuser,
            password= Getpassword,
            host= Gethost,
            database= Getdatabase
        ) 

    
Bdd_Biblio = Bdd_Acces("B2B2", "B2B2", "localhost", "bibliotheque")
