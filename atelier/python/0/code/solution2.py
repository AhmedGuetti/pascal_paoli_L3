import random

option = ['pierre', 'papier', 'ciseaux']


def get_player_choice (player_name):
    choice = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=player_name))
    while choice not in option :
        print("Je n'ai pas compris votre réponse")
        print("Joueur ", player_name)
        choice = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=player_name))
    return choice


def main ():
    on_game = True
    match = True
    toure = 0
    score_player1 = score_player2 = 0
    while on_game:
        choice_oponent =  input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ).upper()
        while choice_oponent != 'O' and choice_oponent != 'N':
            print("Je n'ai pas compris votre réponse")
        player1 = input("Quel est votre nom ? ")
        print("Bienvenu ",player1, " nous allons jouer ensemble \n")
        if choice_oponent == 'O':
            player2 = 'Machine'
        else:
            player2 = input("Quel est le nom du deuxième joueur ?")
            print("Bienvenu ",player2, " nous allons jouer ensemble \n")
        
        while match:
            toure += 1
            player_choice1 = get_player_choice (player1)
            if player2 == 'Machine':
                player_choice2 = option[random.randint(0, 2)]
            else:
                player_choice2 = get_player_choice (player2)
            print("Si on récapitule :",player1, player_choice1, "et", player2, player_choice2,"\n")
            if option.index(player_choice1) == option.index(player_choice2):
                print("aucun de vous, vous être ex æquo")
            elif (option.index(player_choice1) + 2 ) % 3 == option.index(player_choice2):
                print("le gagnant est",player1)
                score_player1 += 1
            else:
                print("le gagnant est",player2)
                score_player2 += 1
            print("Les scores à l'issue de cette manche sont donc",player1, score_player1, "et", player2, score_player2, "\n")
            if toure in range(1,5):
                match = True
            else:
                match = False
        check = input("Do you want to play again O/N ").upper()
        while check != '0' and check != 'N':
            check = input("Do you want to play again O/N ").upper()
        if check == 'O':
            on_game = True
        else:
            on_game = False



main()