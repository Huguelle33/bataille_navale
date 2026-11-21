class Bateau:
    def __init__(self, ligne, colonne, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        if self.vertical:
            return [[self.ligne + i, self.colonne] for i in range(self.longueur)]
        return [[self.ligne, self.colonne + i] for i in range(self.longueur)]

    def chevauchement(self, bateau2):
        for i in self.positions():
            for j in bateau2.positions():
                if i == j:
                    return "chevauchement"
        return "pas de chevauchement" 

    def coulé(self, grille):
        for i in grille.matrice:
            if i == "⛵":
                return False
        return True

class Porte_avion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)  

class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)

class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)

class Sous_marin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)