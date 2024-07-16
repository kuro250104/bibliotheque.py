import mysql.connector

class BDD_Acces():

    def __init__(self, Getuser : str, Getpassword : str, Gethost : str, Getdatabase :str) -> None:
        self.Connect = mysql.connector.connect(
            user = Getuser,
            password = Getpassword,
            host = Gethost,
            database = Getdatabase
        ) 

    def Init_DB(self):
        c = self.Connect.cursor()
        c.execute("SHOW TABLES")

        isSet = False
        for table_name in c:
            print(table_name)
            isSet = True
            
        if isSet == False:
            script_sql = open('Untitled.sql')
            script_Whole = script_sql.read()
            script_sql.close()
            script_tab = script_Whole.split(";")
            
            for i in range(len(script_tab)):
                if script_tab[i] != "/*END*/":
                    c.execute(script_tab[i])
            
        c.close()   
        

    
BDD_Biblio = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")

