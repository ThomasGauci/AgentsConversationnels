#!/usr/bin/env python3
# GAUCI THOMAS M2 MIAGE IA
import random
# Amélioration exercice avec la fonction d'utilité

# retourne l'action de l'aspirateur en fonction de l'emplacement et de l'état de la salle
def action(emplacement, etat, but):
    if(etat == "sale"):
        return "aspirer" 
    if(trajet == chemin[0]):
        if(emplacement != but):
            return "gauche"
    if(trajet == chemin[1]):
        if(emplacement != but):
            return "droite"
    return "stop"
# Initialisation de l'état des salles
def initialisationeSalleEtat():
    i = random.randint(0,1)
    if(i == 0):
        return "propre"
    else:
        return "sale"

print("-------------INITIALISATION-------------")
# Disposition des salles 
# F E C B A D G H I
chemin = [["B","C","E","F"],["D","G","H","I"]]
tmp = chemin[random.randint(0,1)]
# Initialisation des salles
tab = [[0 for x in range(2)] for y in range(9)]
tab[0][0] = "A"
tab[1][0] = "B" 
tab[2][0] = "C" 
tab[3][0] = "D" 
tab[4][0] = "E" 
tab[5][0] = "F" 
tab[6][0] = "G" 
tab[7][0] = "H" 
tab[8][0] = "I" 
# Initialisation de l'état des salles A et B 
for i in range(9):
    tab[i][1] = initialisationeSalleEtat()
    print("La salle : " + str(tab[i][0]) + " est : " + str(tab[i][1]))
print("------------------MAIN------------------")
# fonction d'utilité, si elle est vrai, l'aspirateur va essayer de prendre le chemin le plus sale entre les deux trajets
utility = random.randint(0,1)
print("Utility " + str(utility))
if(utility):
    print("Fonction d'utilité activé")
    g = 0
    d = 0
    for i in range(len(tab)):
        for j in chemin[0]:
            if(tab[i][0] == j):
                if(tab[i][1] == "sale"):
                    g += 1
        for j in chemin[1]:
            if(tab[i][0] == j):
                if(tab[i][1] == "sale"):
                    d += 1
    if(d > g):
        but = "I"
    else :
        but = "F"
else:
    but = tmp[random.randint(0,3)]
print("Le but est de nettoyer la salle " + but)
# Compteur qui permet au robot de s'éteindre si toutes les salles sont propres
compteurPropre = 0
stop = True
j = 0
emplacement = tab[j][0]
t = 0
for i in range(2):
        tmp = chemin[i]
        for d in tmp:
            if(d == but):
                t = i
                trajet = tmp
                print("Voici le trajet" + str(trajet))
print("Départ salle : " + emplacement)
res = action(emplacement,tab[j][1],but)
print("Action aspirateur : " + str(res))
i = 0

# Le robot fait maximum 10 actions ou alors s'éteins si les salles sont propres
while((i < 10) & stop):
    # Si l"action est d'aspirer et que la salle était sale
    if(res == "aspirer"):
        if(tab[j][1] == "sale"):
            # On aspire donc la salle devient propre
            tab[j][1] = "propre"
    # Si l"action est d'aller à droite et que la salle était propre
    if(res == "droite" ):    
        if(tab[j][1] == "propre"):
            # On se déplace dans l'autre salle  
            emplacement = chemin[t][j]
            j += 1
            # On se déplace dans l'autre salle car la salle actuelle est propre donc on incrémente le compteur
            compteurPropre += 1
    # Si l"action est d'aller à gauche et que la salle était propre
    if (res == "gauche"):
        if(tab[j][1] == "propre"):
            # On se déplace dans l'autre salle 
            emplacement = chemin[t][j]
            j += 1 
            # On se déplace dans l'autre salle car la salle actuelle est propre donc on incrémente le compteur
            compteurPropre += 1
    res = action(emplacement,tab[j][1],but)
    if(res == "stop"):
        stop = False
        res = "mise en arrêt"
    if(compteurPropre >= 8):
        # Si le compteur de propreté est plus grand que 3 alors on éteint le robot
        stop = False
        res = "mise en arrêt"
    print("Emplacement salle " + emplacement)
    print("Action aspirateur : " + res)
    i += 1






                


