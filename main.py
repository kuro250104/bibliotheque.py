import Class.Bibliotheque as Bibliotheque
from Class.User import Utilisateur
from BDD import BDD_Acces
from uuid import uuid4


#test = Bibliotheque()

# BDD_Biblio.Init_DB()

# main.py


if __name__ == "__main__":
    bdd_acces = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")
    bdd_acces.Init_DB()

    id_utilisateur = str(uuid4())
    nom_utilisateur = input("Entrez le nom de l'utilisateur : ")
    prenom_utilisateur = input("Entrez le prénom de l'utilisateur : ")
    adresse_utilisateur = input("Entrez l'adresse de l'utilisateur : ")

    utilisateur = Utilisateur(id=id_utilisateur, nom=nom_utilisateur, prenom=prenom_utilisateur,
                              adresse=adresse_utilisateur)
    utilisateur.ajouter(bdd_acces)

    utilisateur.id = 1
    utilisateur.adresse = "456 Rue Secondaire"
    bdd_acces.Connect.close()