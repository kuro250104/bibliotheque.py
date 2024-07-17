from Class.Bibliotheque import Bibliotheque
from Console.LoanConsole import main as LoanConsole
from Class.User import User
from BDD import BDD_Acces, BDD_Biblio
from uuid import uuid4

#BDD_Biblio.Init_DB()

bdd_acces = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")
user = User(bdd_acces)


def show_menu():
    print("\nMenu:")
    print("1. Afficher la bibliothèque")
    print("2. Ajouter un objet")
    print("3. Ajouter un auteur")
    print("4. Ajouter un utilisateur")
    print("5. Supprimer un objet")
    print("6. Supprimer un utilisateur")
    print("7. Gestion des emprunts")
    print("8. Quitter")
    response = input("Entrez votre choix: ")
    return response

def show_bibliotheque(bibliotheque: Bibliotheque):
    item_list = bibliotheque.get_table('item')
    for i in range(len(item_list)):
        print(f"{i + 1} : {item_list[i][1]}")

def new_item(bibliotheque: Bibliotheque):
    name = input("Entrez le nom de l'objet : ")
    adress = input("Entrez l'adresse de l'objet : ")

    type_list = bibliotheque.get_table('type')
    for i in range(len(type_list)):
        print(f"{i + 1} : {type_list[i][1]}")

    type_id = input("Entrez l'id du type de l'objet : ")
    auteur_list = bibliotheque.get_table('auteur')
    for i in range(len(auteur_list)):
        print(f"{i + 1} : {auteur_list[i][1]} {auteur_list[i][2]}")
    auteur_id = input("Entrez l'id de l'auteur de l'objet : ")

    genre_list = bibliotheque.get_table('genre')
    for i in range(len(genre_list)):
        print(f"{i + 1} : {genre_list[i][1]}")
    genre_id = input("Entrez l'id du genre de l'objet : ")

    bibliotheque.add_item(name, adress, type_id, auteur_id, genre_id)
    print(f"L'objet {name} a été ajouté à la bibliothèque.")

def delete_item(bibliotheque: Bibliotheque):
    item_list = bibliotheque.get_table('item')
    for i in range(len(item_list)):
        print(f"{i + 1} : {item_list[i][1]}")
    item_id = input("Entrez l'id de l'objet à supprimer : ")
    bibliotheque.remove_item(item_id)

def new_author(bibliotheque: Bibliotheque):
    author_name = input("Entrez le prenom de l'auteur : ")
    author_surname = input("Entrez le nom de l'auteur : ")
    bibliotheque.add_author(author_name, author_surname)
    print(f"L'auteur {author_name, author_surname} a été ajouté à la bibliothèque.")

def new_user():
    global user
    name = input("Entrez le nom de l'utilisateur : ")
    surname = input("Entrez le prénom de l'utilisateur : ")
    address = input("Entrez l'adresse de l'utilisateur : ")
    user.add_user(name, surname, address)

def delete_user():
    id = input("Entrez l'ID de l'utilisateur à supprimer : ")
    user.remove_user(id)

def gestion_loan():
    LoanConsole()


def main():
    BDD_acces = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")
    bibliotheque = Bibliotheque(BDD_acces)

    while True:
        choix = show_menu()
        if choix == "1":
            show_bibliotheque(bibliotheque)
        elif choix == "2":
            new_item(bibliotheque)
        elif choix == "3":
            new_author(bibliotheque)
        elif choix == "4":
            new_user()
        elif choix == "5":
            delete_item(bibliotheque)
        elif choix == "6":
            delete_user()
        elif choix == "7":
            gestion_loan()
        elif choix == "8":
            print("Au revoir!")
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()