class Magasin:
    """ Classe Magasin
        Attributs privés: self.__nom, self.__stocks
        Méthodes publiques: self.vendre(), self.donner_prix()
    """
    def __init__(self, nom, tableau_produits):
        assert len(nom) != 0, "Le nom du magasin ne doit pas être vide"
        self.__nom = nom
        self.__stocks = tableau_produits

    def vendre(self, produit, nombre):
        """ Prend en paramètre le nom du produit et le nombre d'articles souhaités
            Calcul le nombre d'articles qui peuvent être vendus dans la limite du stock
            Décrémente d'autant le nombre d'articles disponibles
            et renvoie le nombre d'article vendus.
        """
        for dico in self.__stocks: # Recherche le produit dans la liste
            if dico['désignation'] == produit:
                if nombre <= dico['nombre']: # Si il y a suffisamment de produits en stocks
                    dico['nombre'] -= nombre
                    return nombre
                else: # Sinon, nous sommes limités par le stock
                    nombre_vendu = dico['nombre']
                    dico['nombre'] = 0
                    return nombre_vendu
        return 0 # Le produit n'a pas été trouvé. Renvoie donc 0 (aucune vente)

    def donner_prix(self, produit):
        """ Renvoie le prix du produit passé en paramètre
            Si le produit n'existe pas, renvoie None
        """
        for dico in self.__stocks: # Recherche le produit dans la liste
            if dico['désignation'] == produit:
                return dico['prix']
        return None # Le produit n'a pas été trouvé. Renvoie None
            
    def __str__(self):
        description = "Etat des stocks de " + self.__nom + '\n'
        for dico in self.__stocks:
            description += '    '+ str(dico['nombre']) + ' ' + dico['désignation'] + ' à ' + str(dico['prix']) + '€\n'
        return description + '\n'

class Client:
    """ Classe Client
        Attributs privés: self.__nom, self.__solde, self.__chariot
        Méthode publique: self.acheter()
    """
    def __init__(self, nom, argent):
        self.__nom = nom
        assert argent >= 0 , "Un client ne peut pas être créé à découvert"
        self.__solde = argent
        self.__chariot = {}

    def acheter(self, magasin, produit, nombre):
        """ Prend en paramètres le nom du magasin fournisseur, le nom du produit
            et le nombre de produits souhaités
            Ajoute au chariot le nombre de produits achetés dans la limite du solde
            du compte et de la disponibilité des articles en rayon
            Soustrait la somme nécessaire à l'achat au solde du compte
        """
        prix_unitaire = magasin.donner_prix(produit)
        # Attention, ici, nous n'avons pas testé si le prix_unitaire renvoyé vaut 0 ou None!
        nombre_max = min(nombre, self.__solde // prix_unitaire)        
        nombre_vendus = magasin.vendre(produit, nombre_max)
        self.__solde -= nombre_vendus * prix_unitaire
        if produit in self.__chariot.keys():
            self.__chariot[produit] += nombre_vendus
        else:
            self.__chariot[produit] = nombre_vendus

    def __str__(self):
        description = "Fiche client : "+ self.__nom +'\n'
        description += "    solde : " + str(self.__solde) +'\n'
        description += "    chariot : "
        prefixe = ''
        for produit, nombre in self.__chariot.items():
            description += prefixe + str(nombre) + ' ' + produit + ' '
            prefixe = ','
        return description + '\n' + '\n'

if __name__ == "__main__":
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
    print(karouf)
    print(kefna)
    lucie = Client("Lucie", 510)
    print(lucie)
    lucie.acheter(karouf, 'cahier', 100)
    print(lucie)
    lucie.acheter(kefna, 'écouteurs', 2)
    print(lucie)
    lucie.acheter(karouf, 'radio-réveil', 20)
    print(karouf)
    print(kefna)
    lucie.solde = -100
    print(lucie)