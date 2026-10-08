etudiant = {} #création du dictionnaire vide pour stocker les étudiants et leurs notes  
def ajouter_etudiant(nom, note): #fonction pour ajouter un étudiant et sa note au dictionnaire
    etudiant[nom] = float(note) #ajout de l'étudiant et de sa note au dictionnaire
    return etudiant #retourne le dictionnaire mis à jour

def moyenne_classe(): #fonction pour calculer la moyenne de la classe
    if len(etudiant) == 0: #vérifie si le dictionnaire est vide
        return 0 #retourne 0 si aucun étudiant n'a été ajouté
    somme_notes = sum(etudiant.values()) #somme des notes des étudiants
    moyenne = somme_notes / len(etudiant) #calcul de la moyenne
    return moyenne #retourne la moyenne de la classe

def meilleur_etudiant(): #fonction pour trouver l'étudiant avec la meilleure note
    if len(etudiant) == 0: #vérifie si le dictionnaire est vide
        return None #retourne None si aucun étudiant n'a été ajouté
    meilleur = max(etudiant, key=etudiant.get) #trouve l'étudiant avec la note maximale
    return meilleur, etudiant[meilleur] #retourne le nom de l'étudiant et sa note

def sauvegarder_donnees(nom_fichier): #fonction pour sauvegarder les données dans un fichier
    with open(nom_fichier, 'w', encoding='utf-8') as fichier: #ouvre le fichier en mode écriture
        for nom, note in etudiant.items(): #parcourt le dictionnaire des étudiants
            fichier.write(f"{nom},{note}\n") #écrit chaque étudiant et sa note dans le fichier
ajouter_etudiant("Alice", 12) #ajoute l'étudiant Alice avec sa note
ajouter_etudiant("Bob", 15) #ajoute l'étudiant Bob avec sa note
ajouter_etudiant("Claire", 9.5) #ajoute l'étudiant Claire avec sa note
moyenne_classe() #calcule la moyenne de la classe
meilleur_etudiant() #trouve l'étudiant avec la meilleure note
sauvegarder_donnees("donnees_etudiants.txt") #sauvegarde les données dans un fichier
