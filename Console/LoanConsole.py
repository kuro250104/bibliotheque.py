from BDD import BDD_Acces
from Class.Loan import LoanManager
db_acces = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")
loan_manager = LoanManager(db_acces)

def main():
    while True:
        print("Options:")
        print("1. Ajouter un emprunt")
        print("2. Modifier un emprunt")
        print("3. Afficher les emprunts")
        print("4. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            add_loan()
        elif choice == '2':
            modify_loan()
        elif choice == '3':
            print("1. Afficher tout les emprunts")
            print("2. Afficher un seul emprunt")
            choice_show = input("Choisissez une option: ")
            if choice_show == '1': show_all_loan()
            elif choice_show == '2':
                emprunt_id = input("Entrez l'ID de l'emprunt: ")
                show_one_loan(emprunt_id)
        elif choice == '4':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def add_loan():
    loan = input("Entrez l'état de l'emprunt (0 pour non-emprunté, 1 pour emprunté): ")
    start_date = input("Entrez la date de début (YYYY-MM-DD): ")
    end_date = input("Entrez la date de fin (YYYY-MM-DD): ")
    user_id = input("Entrez l'ID de l'utilisateur: ")

    try:
        loan_manager.add_loan(int(loan), start_date, end_date, int(user_id))
        print("Emprunt ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'emprunt: {e}")

def modify_loan():
    loan_id = input("Entrez l'ID de l'emprunt à modifier: ")
    loan_manager.show_one_loan(loan_id)
    loan_input = input(
        "Le livre est emprunter (oui ou non): ")
    if loan_input.lower() == 'oui':
        loan = 1
    elif loan_input.lower() == 'non':
        loan = 0
    else:
        loan = None
    start_date = input("Entrez la nouvelle date de début (YYYY-MM-DD) ou laissez vide pour ne pas modifier: ")
    end_date = input("Entrez la nouvelle date de fin (YYYY-MM-DD) ou laissez vide pour ne pas modifier: ")
    user_id = input("Entrez le nouvel ID de l'utilisateur ou laissez vide pour ne pas modifier: ")

    try:
        loan_manager.modify_loan(int(loan_id),
                                 int(loan) if loan else None,
                                 start_date if start_date else None,
                                 end_date if end_date else None,
                                 int(user_id) if user_id else None)
        print("Emprunt modifié avec succès.")
    except Exception as e:
        print(f"Erreur lors de la modification de l'emprunt: {e}")

def show_all_loan():
    try:
        loan_manager.show_loan()
    except Exception as e:
        print(f"Erreur lors de l'affichage des emprunts: {e}")

def show_one_loan(loan_id):
    try:
        loan_manager.show_one_loan(loan_id)
    except Exception as e:
        print(f"Erreur lors de l'affichage des emprunts: {e}")

if __name__ == "__main__":
    main()
