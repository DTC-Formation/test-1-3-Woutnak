#blibliotheque
import json
from datetime import datetime

#variable
liste_taches = []

tache = {

             "nom" :'',
             "deadline" : '',
             "statut" : '',

            }

# while True:
print("Bienvenue dans le gestionnaire des tâches")
print("1 - Ajout d'une tâche ")
print("2 - Affichage des tâches")
print("3 - Modification d'une tâche")
print("4 - Enregistrement des tâches")

# Ajout d'une tâche
user_action = input("Entrer une action: ")

while user_action != "1" and user_action != "2" and user_action != "3" and user_action != "4":
        user_action = input("Action non reconnu\nEntrer une action: ")

#1 - Ajout d'une tâche
if user_action == "1":
        # input nom, input
        print("Veuillez ajouter une tâche ")
        input_nom = input("Entrer le nom: ")
        input_deadline = input("Entrer le deadline (AAAA-MM-JJ HH:MM): ")

        #affection du dictionnaire tache
        tache['nom']  = input_nom
        tache['deadline'] = datetime
        #conversion en json
        data = json.dumps(tache)

#2 - Affichage des tâches
elif user_action == "2" :
#ajout de nouveau dans le liste des taches
   liste_taches.append(tache)
   print(tache)
   print(liste_taches)
   #fichier json
   f = open('tache.json',"r")
   f.read()

#type de status :commencer,en cours,terminer,rater
statut = ['commencer','en cours','terminer','rater']
deadline = datetime.fromisoformat(input_deadline)
delai = datetime.now - deadline
#3 - Modification d'une tâche
elif user_action == "3" :
 print('Modification d\'une tâche')

#4 - Enregistrement des tâches
elif user_action == "4" :
outfile.write(data)


