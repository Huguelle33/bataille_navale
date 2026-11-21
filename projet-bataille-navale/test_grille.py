from grille import Grille
from bateau import Bateau

def test_init():
    g = Grille(1,1)
    assert isinstance(g, Grille)

def test_matrice():
    g = Grille(5,8)
    assert g.matrice == ["∿" for _ in range(8*5)]

def test_nbcolonnes():
    g = Grille(5,8)
    assert g.nombre_colonnes == 8

def test_tirer():
    g = Grille(5,8)
    g.tirer(2,3)
    assert g.matrice[2*8+3] == "x"

def test_str():
    g = Grille(5,8)
    assert str(g) == "∿ ∿ ∿ ∿ ∿ ∿ ∿ ∿\n∿ ∿ ∿ ∿ ∿ ∿ ∿ ∿\n∿ ∿ ∿ ∿ ∿ ∿ ∿ ∿\n∿ ∿ ∿ ∿ ∿ ∿ ∿ ∿\n∿ ∿ ∿ ∿ ∿ ∿ ∿ ∿" 

def test_ajoute1():
    g = Grille(2,3)
    assert g.ajoute(Bateau(1, 0, longueur=2, vertical=False)) == ["∿", "∿", "∿", "⛵", "⛵", "∿"]

def test_ajoute2():
    g = Grille(2,3)
    assert g.ajoute(Bateau(1, 0, longueur=2, vertical=True)) == ["∿", "∿", "∿", "∿", "∿", "∿"]

def test_ajoute3():
    g = Grille(2,3)
    assert g.ajoute(Bateau(1, 0, longueur=4, vertical=True)) == ["∿", "∿", "∿", "∿", "∿", "∿"]
