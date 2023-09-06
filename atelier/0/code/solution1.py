import random

false_answer = True
while false_answer == True:
    reponse = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
    if reponse != 'O' and reponse != 'N':
        print("Je n'ai pas compris votre réponse")
    else:
        false_answer = False

# initialisation des variable 

score_1 = 0
nombre_manche = 0
check = True
score_2 = 0
ppc = ["pierre", "papier", "ciseaux"]


# recuperer le nom du premier joueur
nom_joueur_1 = input("Quel est votre nom ? ")
print("Bienvenu ",nom_joueur_1, " nous allons jouer ensemble \n")


# recuperer le nom du 2 eme joueur 
if reponse == 'O':
    nom_joueur_2 = 'Machine'
if reponse == 'N':
    nom_joueur_2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",nom_joueur_2, " nous allons jouer ensemble \n")
 

while check == True:
    nombre_manche += 1 
    choix_joueur_1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=nom_joueur_1))
    if choix_joueur_1 not in ppc:
        validation_choix = False
        print("Je n'ai pas compris votre réponse")
        while validation_choix == False :
            print("Joueur ", nom_joueur_1)
            choix_joueur_1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
            validation_choix = True
            if choix_joueur_1 not in ppc: 
                validation_choix = False

    if nom_joueur_2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que reponse == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        choix_joueur_2 = ppc[random.randint(0, 2)]


    if nom_joueur_2 != 'Machine':
        print("Joueur", nom_joueur_2)
        choix_joueur_2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        if choix_joueur_2 not in ppc:
            validation_choix = False
            print("Je n'ai pas compris votre réponse")
            while not validation_choix :
                print("Joueur ", nom_joueur_2)
                choix_joueur_2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                validation_choix = True
                if choix_joueur_2 not in ppc: 
                    validation_choix = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nom_joueur_1, choix_joueur_1, "et", nom_joueur_2, choix_joueur_2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat

    # Le cas d'egalite si le choix 1 est le meme que le choix 2
    if choix_joueur_1 == choix_joueur_2  :
        winner = "aucun de vous, vous être ex æquo"
        print("le gagnant est ",winner)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur_1, score_1, "et", nom_joueur_2, score_2, "\n")

    if (choix_joueur_1 == 'ciseaux' and choix_joueur_2 == 'pierre') or (choix_joueur_1 == 'pierre' and choix_joueur_2 == 'papier') or (choix_joueur_1 == 'papier' and choix_joueur_2 == 'ciseaux' ) :
        winner = nom_joueur_2
        score_2 = score_2 + 1
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur_1, score_1, "et", nom_joueur_2, score_2, "\n")

    if (choix_joueur_1 == 'pierre' and choix_joueur_2 == 'ciseaux' ) or (choix_joueur_1 == 'ciseaux' and choix_joueur_2 == 'papier') or (choix_joueur_1 == 'papier' and choix_joueur_2 == 'pierre') :
        winner = nom_joueur_1
        score_1 = score_1 + 1
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur_1, score_1, "et", nom_joueur_2, score_2, "\n")


    if nombre_manche in [1,2,3,4]:
        check = True

    if nombre_manche ==5:
        # On propose de check ou de s'arrêter 
        
        false_answer = True
        while false_answer == True:
            go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom_joueur_1,nom_joueur_2))
            if go != 'O' and go != 'N':
                print("Je n'ai pas compris votre réponse")
            else:
                if go == 'O':
                    check = True
                if go == 'N':
                    check = False
                false_answer = False
    
if check == False :
    print("Merci d'avoir joué ! A bientôt")