#  Agents Conversationnels

# Installation
```bash
git clone https://github.com/ThomasGauci/AgentsConversationnels.git
cd /AgentsConversationnels
python3 exoXX.py
```
# exo1.py
Agent réflexe Simple :
- Aspirateur
- Si la zone X est sale, il la nettoie
- Il boucle à l'infini

Amélioration apportée :
- mise en arrêt du robot après 3 passage dans une salle propre
# exo2.py
Agent réflexe avec état interne :
- Aspirateur
- Si la zone X est sale, il la nettoie
- Il se déplace en fonction des salles à nettoyer et de l'action qu'il vient de faire

Amélioration apportée :
- mise en arrêt du robot après 3 passage dans une salle propre
# exo3.py
Agent réflexe avec état interne et un but :
- Aspirateur
- Si la zone X est sale, il la nettoie
- Il se déplace en fonction des salles à nettoyer, de l'action qu'il vient de faire et de son but

Amélioration apportée :
- mise en arrêt du robot après 10 passages dans une salle propre ou toutes les salles sont propres
# exo4.py
Agent réflexe avec fonction d'utilité :
- Aspirateur
- Si la zone X est sale, il la nettoie
- Il se déplace en fonction des salles à nettoyer, de l'action qu'il vient de faire et de son but

Amélioration apportée :
- mise en arrêt du robot après 10 passages dans une salle propre ou toutes les salles sont propres
- l'aspirateur va essayer de prendre le chemin le plus sale entre les deux trajets
# eliza.py
Agent conversationnel :
- Règles patron-action
- Règles patron-transformation

Amélioration apportée :
- Ajout du sentiment d'amour
# parry.py
Agent conversationnel :
- Règles patron-action
- Règles patron-transformation
- Modèle mental

Amélioration apportée :
- Ajout des émotions (menacant, calme)
- S'énerve si la conversation parle de sujet sensible.
- S'énerve si la personne est trop intrusive (pose trop de question) 

# billets.py
Agent conversationnel :
- Questions prédéfinis
- Règle des slots
- Affiche un résultat à l'utisateur

Amélioration apportée :
- Structure de contrôle de la ville
- Structure de contrôle des dates
- Structure de contrôle des cohérences des réponses de l'utilisateur

# Librairies 
 - https://pypi.org/project/termcolor/
 - https://pypi.org/project/geotext/
 - https://pypi.org/project/DateTime/
