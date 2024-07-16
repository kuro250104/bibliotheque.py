import mysql.connector

class BDD_Acces():

    def __init__(self, Getuser : str, Getpassword : str, Gethost : str, Getdatabase :str) -> None:
        self.Connect = mysql.connector.connect(
            user= Getuser,
            password= Getpassword,
            host= Gethost,
            database= Getdatabase
        ) 

    def Init_DB(self):
        c = self.Connect.cursor()
        c.execute("SHOW TABLES")

        isSet = False
        for table_name in c:
            print(table_name)
            isSet = True
            
        if isSet == False:
            script_sql = open('E:\\Work\\projet - Data\\Untitled.sql')
            c.execute(script_sql.read())
            script_sql.close()


        c.close()   
        

    
BDD_Biblio = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")

