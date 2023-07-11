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
utilisateurs = {}
#///////LOGIN////////
nom_utilisateur = input("Entrez votre nom s'il vous plait :")
if nom_utilisateur in utilisateurs:
      nom_utilisateur = input("Nom deja utilisé\nEntrez votre nom s'il vous plait:")
elif nom_utilisateur not in utilisateurs:
      utilisateurs['nom'] =  nom_utilisateur
      print("Bonjour {} et bienvenue sur TO DO List" .format(utilisateurs['nom']))
#il faut avoir un fichier json qui  enregistre tout les utilisateurs 
print(utilisateurs)  
#///////LES ACTIONS////////
while True:
   print("//////////////////////////////////////////")
   print("Bienvenue dans le gestionnaire des tâches")
   print("1 - Ajout d'une tâche ")
   print("2 - Affichage des tâches")
   print("3 - Modification d'une tâche")
   print("4 - Enregistrement des tâches")
   print("5 - Quitter TO DO List")
# Ajout d'une tâche
   user_action = input("Entrer une action: ")

   while user_action != "1" and user_action != "2" and user_action != "3" and user_action != "4" and user_action != "5":
        user_action = input("Action non reconnu\nEntrer une action: ")


#1 - Ajout d'une tâche
   if user_action == "1":
        # input nom, input deadline
        print("Veuillez ajouter une tâche ")
        input_nom = input("Entrer le nom: ")
        input_deadline = input("Entrer le deadline (AAAA-MM-JJ HH:MM): ")

        #affection du dictionnaire tache
        tache['nom']  = input_nom
        tache['deadline'] = datetime
        
        #conversion en json
        #data = json.dumps(tache)
        #fichier json   
        f = open('tache.json',"r")
        f.read()
        

#2 - Affichage des tâches
   elif user_action == "2" :
#ajout de nouveau dans le liste des tach#Ajout des taches dans liste_taches
       liste_taches.append(tache['nom'])
       print("{} Votre To do list {} :".format(user_actuel,liste_taches)) 
   
   
#3 - Modification d'une tâche
   elif user_action == "3" :
      print('Modification d\'une tâche:')
#type de status :commencer,en cours,terminer,rater
# statut = ['commencer','en cours','terminer','rater']
#deadline = datetime.fromisoformat(input_deadline)
# delai = datetime.now - deadline

#4 - Enregistrement des tâches
   elif user_action == "4" :
     #outfile.write(data)
     print('Enregistrement d\'une tâche:')
#Quitter
   elif user_action == "5":
     break



