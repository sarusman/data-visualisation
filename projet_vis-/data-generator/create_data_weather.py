import csv

def lire_csv(nom_fichier):
    lignes_non_nan = []
    try:
        with open(nom_fichier, 'r') as fichier_csv:
            lecteur = csv.reader(fichier_csv)
            for ligne in lecteur:
                if not any(cellule == 'NaN' for cellule in ligne):
                    lignes_non_nan.append(ligne)
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
        return None
    return lignes_non_nan



def decouper_liste(liste):
    sous_listes = []
    for l in liste:
        ligne = l[0].split(";")
        sous_liste =  []
        sous_liste.append(ligne[0])  # id station
        sous_liste.append(ligne[1]) # date
        sous_liste.append(ligne[7])  # temperature
        sous_liste.append(ligne[9]) # humidité
        sous_liste.append(ligne[11]) # temps présent --> nuage/soleil..
        sous_listes.append(sous_liste) #
    return sous_listes

def afficher_sous_listes(sous_listes):
    with open('colonnes_extraites.csv', 'w', newline='') as fichier_sortie:
        ecrivain = csv.writer(fichier_sortie)
        for sous_liste in sous_listes:
            ecrivain.writerow(sous_liste)