#!/usr/bin/env python3
# GAUCI THOMAS M2 MIAGE IA
import random
# Amélioration exercice avec la mise en arrêt du robot après 3 passage dans une salle propre

# retourne l'action de l'aspirateur en fonction de l'emplacement et de l'état de la salle
def action(emplacement, etat):
    if(etat == "sale"):
        return "aspirer"
    if(emplacement == "A"):
        return "droite"
    if(emplacement == "B"):
        return "gauche"
# Initialisation de l'état des salles
def initialisationeSalleEtat():
    i = random.randint(0,1)
    if(i == 0):
        return "propre"
    else:
        return "sale"

print("-------------INITIALISATION-------------")
# Initialisation des salles A et B 
tab = [[0 for x in range(2)] for y in range(2)]
tab[0][0] = "A"
tab[1][0] = "B" 
# Initialisation de l'état des salles A et B 
for i in range(2):
    tab[i][1] = initialisationeSalleEtat()
    print("La salle : " + str(tab[i][0]) + " est : " + str(tab[i][1]))
print("------------------MAIN------------------")
# Compteur qui permet au robot de s'éteindre si toutes les salles sont propres
compteurPropre = 0
stop = True
j = random.randint(0,1)
print("Départ salle : " + str(tab[j][0]))
res = action(tab[j][0],tab[j][1])
print("Action aspirateur : " + res)
i = 0
# Le robot fait maximum 10 actions ou alors s'éteins si les salles sont propres
while((i < 10) & stop):
    # Si l"action est d'aspirer et que la salle était sale
    if(res == "aspirer" and tab[j][1] == "sale"):
        # On aspire donc la salle devient propre
        tab[j][1] = "propre"
    # Si l"action est d'aller à droite et que la salle était propre
    if(res == "droite" and tab[j][1] == "propre"):    
        # On se déplace dans l'autre salle  
        j = 1
        # On se déplace dans l'autre salle car la salle actuelle est propre donc on incrémente le compteur
        compteurPropre += 1
    # Si l"action est d'aller à gauche et que la salle était propre
    if (res == "gauche" and tab[j][1] == "propre"):
        # On se déplace dans l'autre salle 
        j = 0 
        # On se déplace dans l'autre salle car la salle actuelle est propre donc on incrémente le compteur
        compteurPropre += 1
    res = action(tab[j][0],tab[j][1])
    if(compteurPropre >= 3):
        # Si le compteur de propreté est plus grand que 3 alors on éteint le robot
        stop = False
        res = "mise en arrêt"
    print("Action aspirateur : " + res)
    i += 1






                


