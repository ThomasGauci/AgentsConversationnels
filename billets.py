
from geotext import GeoText
import datetime

def init():
    return [False,False,False,False,False,False,False]
res = init()
reservation = False
print("------------Bonjour et bienvenue sur AIR MIAGE------------")
while reservation == False:
    while res[0] == False:    
        villeDepart = GeoText(input("Quelle est votre ville de départ : ")).cities
        # Vérification qu'une ville est bien entré
        if(len(villeDepart) > 0):
            res[0] = True

    while res[1] == False:    
        villeArrive = GeoText( input("Quelle est votre ville de destination : ")).cities
        # Vérification qu'une ville est bien entré
        if(len(villeArrive) > 0):
            # Vérification que la destination n'est pas la ville de départ
            if(villeArrive[0] != villeDepart[0]):
                res[1] = True
    
    while res[2] == False:
        today = datetime.datetime.now()
        departDate = input("Quelle est la date de votre départ (dd/mm/yyyy): ")
        j,m,y = departDate.split('/')
        dateValide = True
        try:
            depart = datetime.datetime(int(y),int(m),int(j))
        except ValueError :
            dateValide = False
        # Vérification de l'écriture d'une date valide
        if(dateValide):
            # Vérification que la date n'est pas déjà passé
            if(depart>=today):
                res[2] = True

    while res[3] == False:
        allerRetour = input("Souhaitez vous un billet aller retour (oui/non): ")
        # Vérification de l'écriture
        if(allerRetour.lower() == "oui" or allerRetour.lower() == "non"):
            res[3] = True
        
    if(allerRetour == "non"):
        while res[4] == False:
            reponse = input("Voulez vous partir de " + str(villeDepart[0])  + " le " + departDate + " pour la destination de " + str(villeArrive[0]) + " : ")
            # Vérification de l'écriture
            if(reponse.lower() == "oui" or reponse.lower() == "non"):
                if(reponse.lower() == "oui"):
                    reservation = True
                res[4] = True
    else:
        while res[5] == False:
            retourDate = input("Quelle est la date de votre retour (dd/mm/yyyy): ")
            today = datetime.datetime.now()
            j,m,y = retourDate.split('/')
            dateValide = True
            
            try:
                retour = datetime.datetime(int(y),int(m),int(j))
            except ValueError :
                dateValide = False
            # Vérification de l'écriture d'une date valide
            print(retour)
            print(depart)
            if(dateValide):
                # Vérification que la date n'est pas déjà passé et que la date n'est pas avant la date de départ
                if(retour>=today and retour>=depart):
                    res[5] = True
        while res[6] == False: 
            reponse = input("Voulez vous partir de " + str(villeDepart[0]) + " le " + departDate + " pour la destination de " + str(villeArrive[0]) + " avec un vol retour le " + retourDate + " : ")
             # Vérification de l'écriture
            if(reponse.lower() == "oui" or reponse.lower() == "non"):
                if(reponse.lower() == "oui"):
                    reservation = True
                res[6] = True

    if(reponse.lower() == "non"):
        res = init()
print("------------RESERVATION EFFECTUEE------------")
