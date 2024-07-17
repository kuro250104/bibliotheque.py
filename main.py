from BDD import BDD_Acces
from Class.User import User

bdd_acces = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")
user = User(bdd_acces)


def show_menu():
    print("\nMenu:")
    print("1. Ajouter un utilisateur")
    print("2. Supprimer un utilisateur")
    print("3. Ajouter un utilisateur")
    print("4. Afficher la bibliothèque")
    print("5. Quitter")
    response = input("Entrez votre choix: ")
    return response


def add_user():
    global user
    name = input("Entrez le nom de l'utilisateur : ")
    surname = input("Entrez le prénom de l'utilisateur : ")
    address = input("Entrez l'adresse de l'utilisateur : ")
    user.add_user(name, surname, address)


def remove_user():
    id = input("Entrez l'ID de l'utilisateur à supprimer : ")
    user.remove_user(id)


def main():
    bibliotheque = []
    while True:
        choix = show_menu()
        if choix == "1":
            add_user()
        elif choix == "2":
            remove_user()
        elif choix == "3":
            print("Fonctionnalité non implémentée, veuillez réessayer.")
        elif choix == "4":
            print("Fonctionnalité non implémentée, veuillez réessayer.")
        elif choix == "5":
            print("Quitter le programme.")
            break
        else:
            print("Choix non valide, veuillez réessayer.")


if __name__ == "__main__":
    main()
