from bateau import Bateau
from grille import Grille
from bateau import Porte_avion, Croiseur, Torpilleur, Sous_marin

def test_init():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False

def test_positions_1():
    assert Bateau(2, 3, longueur=3).positions() == [[2, 3], [2, 4], [2, 5]]
 
def test_positions_2():
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [[2, 3], [3, 3], [4, 3]]

def test_chevauchement():
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(3, 4)
    assert b1.chevauchement(b2) == "pas de chevauchement"
    b3 = Bateau(2, 4)
    assert b1.chevauchement(b3) == "chevauchement"
 
def test_coulé():
    b = Bateau(1, 0, longueur=2, vertical=False)
    g = Grille(2, 3)
    g.ajoute(b)
    g.tirer(1, 0)
    g.tirer(1, 1)
    assert b.coulé(g) == True

def test_pas_coulé():
    b = Bateau(1, 0, longueur=2, vertical=False)
    g = Grille(2, 3)
    g.ajoute(b)
    g.tirer(1, 0)
    g.tirer(0, 1)
    assert b.coulé(g) == False

def test_porte_avion():
    pa = Porte_avion(0, 0)
    assert isinstance(pa, Porte_avion)

def test_croiseur():
    c = Croiseur(0, 0)
    assert isinstance(c, Croiseur)

def test_torpilleur():
    t = Torpilleur(0, 0)
    assert isinstance(t, Torpilleur)

def test_sous_marin():
    sm = Sous_marin(0, 0)
    assert isinstance(sm, Sous_marin)