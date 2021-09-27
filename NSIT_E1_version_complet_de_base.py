class Magasin:
    def __init__(self, nom, produits):
        self.nom = nom
        self.stocks = produits

    def vendre(self, produit, nombre):
        dico['nombre'] -= nombre
        return nombre
        
    def donner_prix(self, produit):
        for dico in self.stocks:
            if dico['désignation'] == produit:
                return dico['prix']
        return None
            
    def afficher(self):
        print("Etat des stocks de ", self.nom)
        for dico in self.stocks:
            print(dico['nombre'], dico['désignation'], 'à', dico['prix'], '€')
        print()

class Client:
    def __init__(self, nom, argent):
        self.nom = nom
        self.solde = argent
        self.chariot = {}

    def acheter(self, magasin, produit, nombre):
        assert nombre >0, 'nombre doit être positif'
        prix_unitaire = magasin.donner_prix(produit)
        self.solde -= nombre * prix_unitaire
        self.chariot[produit] = nombre
        
    def afficher(self):
        print("Fiche client : ", self.nom)
        print("    solde : ", self.solde)
        print("    chariot : ", end="")
        prefixe = ''
        for produit, nombre in self.chariot.items():
            print(prefixe, nombre, produit, end="")
            prefixe = ','
        print()
        print()

stock1 = [
         {'désignation':'radio-réveil', 'nombre':20, 'prix':25},
         {'désignation':'cahier', 'nombre':200, 'prix':3},
         {'désignation':'yaourt', 'nombre':500, 'prix':1}]
karouf = Magasin("Karouf", stock1)
stock2 = [
         {'désignation':'TV', 'nombre':100, 'prix':2500},
         {'désignation':'PC_gamer', 'nombre':20, 'prix':8000},
         {'désignation':'écouteurs', 'nombre':400, 'prix':10}]
kefna = Magasin("La Kefna", stock2)
karouf.afficher()
kefna.afficher()
lucie = Client("Lucie", 510)
lucie.afficher()
lucie.acheter(karouf, 'cahier', 100)
lucie.afficher()
lucie.acheter(kefna, 'écouteurs', 2)
lucie.afficher()
lucie.acheter(karouf, 'radio-réveil', 20)
karouf.afficher()
kefna.afficher()
lucie.afficher()

