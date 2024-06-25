import mysql.connector

class Bdd_Acces():

    def __init__(self, user : str, password : str, host : str, database :str) -> None:
        self.Connect = mysql.connector.connect(
            user="",
            password="",
            host="",
            database=""
        ) 

    

