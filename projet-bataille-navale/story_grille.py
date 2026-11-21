# Plouf dans l'eau

from grille import Grille       

grille = Grille(5, 8)   #la classe Grille n'est pas encore créée
print(grille)          
x = int(input("rentre la coordonnée x (0-4) : "))
y = int(input("rentre la coordonnée y (0-7) : "))
grille.tirer(x, y)      #la fonction tirer n'est pas encore définie
print(grille)           
