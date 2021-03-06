#!/usr/bin/env python3
# GAUCI THOMAS M2 MIAGE IA
import random
# Amélioration exercice avec la mise en arrêt du robot après 3 passage dans une salle propre

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
# B C E F A D G H I
chemin = [["B","C","E","F"],["D","G","H","I"]]
tmp = chemin[random.randint(0,1)]
but = tmp[random.randint(0,3)]
print("Le but est de nettoyer la salle " + but)
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
def search(salle):
    for x in range(len(tab)):
        if(tab[x][0] == salle):
            return x
# Initialisation de l'état des salles A et B 
for i in range(9):
    tab[i][1] = initialisationeSalleEtat()
    print("La salle : " + str(tab[i][0]) + " est : " + str(tab[i][1]))
print("------------------MAIN------------------")
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
            j = search(emplacement)
            # On se déplace dans l'autre salle car la salle actuelle est propre donc on incrémente le compteur
            compteurPropre += 1
    # Si l"action est d'aller à gauche et que la salle était propre
    if (res == "gauche"):
        if(tab[j][1] == "propre"):
            # On se déplace dans l'autre salle 
            emplacement = chemin[t][j]
            j = search(emplacement) 
            # On se déplace dans l'autre salle car la salle actuelle est propre donc on incrémente le compteur
            compteurPropre += 1
    res = action(emplacement,tab[j][1],but)
    print("Emplacement salle " + emplacement)
    print("Action aspirateur : " + res)
    if(res == "stop"):
        stop = False
        res = "mise en arrêt"
    if(compteurPropre >= 8):
        # Si le compteur de propreté est plus grand que 3 alors on éteint le robot
        stop = False
        res = "mise en arrêt"
    if(res == "stop" or compteurPropre >= 8):
        print("Emplacement salle " + emplacement)
        print("Action aspirateur : " + res)
    i += 1






                


