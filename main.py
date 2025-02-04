import os
import csv

# Lis un fichier csv situé dans le répertoire data
# retourne un dictionnaire le nombre d'employées dans chaque pays
def compter_pays(nom_fichier:str) -> dict :
    donnees_pays = {}
    os.chdir(os.path.dirname(__file__) + "\\data")
    with open(nom_fichier, "r") as fichier_lu :
        lecteur_csv = csv.reader(fichier_lu, delimiter=';')
        next(lecteur_csv) # saute la première ligne
        for ligne in lecteur_csv :
            pays = ligne[3]
            if donnees_pays.get(pays) != None :
                donnees_pays[pays] = donnees_pays[pays] + 1
            else :
                donnees_pays[pays] = 1
    
    return donnees_pays








if __name__ == "__main__" :
    stats_pays = compter_pays("employes_AAB.csv")
    print(stats_pays["Canada"])
    print(stats_pays["United States of America"])