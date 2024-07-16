from Class.Bibliotheque import Bibliotheque
from BDD import BDD_Acces


BDD_Biblio = BDD_Acces("B2B2", "B2B2", "localhost", "bibliotheque")

BDD_Biblio.Init_DB()

Biblio = Bibliotheque(BDD_Biblio)
