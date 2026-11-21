#Chevauchement"

from bateau import Bateau

b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(3, 4)
print(b1.chevauchement(b2))