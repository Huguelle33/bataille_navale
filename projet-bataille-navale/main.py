import random
from grille import Grille
from bateau import Porte_avion, Croiseur, Torpilleur, Sous_marin

NB_LIGNES = 8
NB_COLONNES = 10

# Affichage lorsque bateau coulé 
AFFICHAGE = {
    Porte_avion: "🚢",
    Croiseur: "⛴",
    Torpilleur: "🚣",
    Sous_marin: "🐟",
}

# Message propre à chaque type de bateau coulé
MESSAGES = {
    Porte_avion: "Le porte-avions est coulé",
    Croiseur: "Le croiseur est coulé",
    Torpilleur: "Le torpilleur est coulé",
    Sous_marin: "Le sous-marin est coulé",
}

NOMS = {
    Porte_avion: "porte-avions",
    Croiseur: "croiseur",
    Torpilleur: "torpilleur",
    Sous_marin: "sous-marin",
}

def placements_possibles(classe, bateaux_places):
    possibles = []
    for ligne in range(NB_LIGNES):
        for colonne in range(NB_COLONNES):
            for vertical in (False, True):
                candidat = classe(ligne, colonne, vertical)
                dans_la_grille = all(
                    0 <= l < NB_LIGNES and 0 <= c < NB_COLONNES
                    for l, c in candidat.positions()
                )
                if not dans_la_grille:
                    continue
                if any(candidat.chevauchement(b) == "chevauchement" for b in bateaux_places):
                    continue
                possibles.append(candidat)
    return possibles

def placer_bateaux():
    bateaux = []
    for classe in (Porte_avion, Croiseur, Torpilleur, Sous_marin):
        bateaux.append(random.choice(placements_possibles(classe, bateaux)))
    return bateaux

def demander_coup():
    while True:
        ligne = int(input(f"Choisis une ligne (0-{NB_LIGNES - 1}) : "))
        colonne = int(input(f"Choisis une colonne (0-{NB_COLONNES - 1}) : "))
        if 0 <= ligne < NB_LIGNES and 0 <= colonne < NB_COLONNES:
            return ligne, colonne
        print("Coordonnées hors de la grille.")

def jouer():
    grille = Grille(NB_LIGNES, NB_COLONNES)
    bateaux = placer_bateaux()
    cases_tirees = set()
    coups = 0
    restants = list(bateaux)

    print("=== BATAILLE NAVALE ===")
    print(grille)

    while restants:
        ligne, colonne = demander_coup()

        if (ligne, colonne) in cases_tirees:
            print("Vous avez déjà tiré sur cette case !")
            continue

        cases_tirees.add((ligne, colonne))
        coups += 1

        touche = next((b for b in restants if [ligne, colonne] in b.positions()), None)

        if touche is None:
            grille.tirer(ligne, colonne, "x")
            print("Raté !")
        else:
            grille.tirer(ligne, colonne, "💣")
            coule = all((l, c) in cases_tirees for l, c in touche.positions())
            if coule:
                for l, c in touche.positions():
                    grille.tirer(l, c, AFFICHAGE[type(touche)])
                restants.remove(touche)
                print(MESSAGES[type(touche)])
            else:
                print(f"Touché ! ({NOMS[type(touche)]})")

        print(grille)

    print(f"Bravo, tous les bateaux sont coulés en {coups} coups !")

if __name__ == "__main__":
    jouer()