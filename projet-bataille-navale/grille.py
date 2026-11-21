class Grille :
    def __init__(self,nombre_lignes, nombre_colonnes):
        self.matrice = ["∿" for _ in range(nombre_colonnes*nombre_lignes)]
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes

    def tirer(self, ligne, colonne, touche = "x"):
        self.matrice[ligne * self.nombre_colonnes + colonne] = touche

    def __str__(self):
        return "\n".join(" ".join(str(self.matrice[i * self.nombre_colonnes + j]) for j in range(self.nombre_colonnes)) for i in range(self.nombre_lignes))

    def ajoute(self, bateau):
        for pos in bateau.positions():
            if pos[0] >= self.nombre_lignes or pos[1] >= self.nombre_colonnes:
                return self.matrice
        for pos in bateau.positions():
            self.matrice[pos[0]*self.nombre_colonnes + pos[1]] = "⛵"
        return self.matrice



