import random
 

valid_options = ["pierre", "papier", "ciseaux"]

def get_valid_answer(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_options:
            return user_input
        print("Je n'ai pas compris votre réponse")

def determine_winner(player1, player2):
    if player1 == player2:
        return "aucun de vous, vous êtes ex æquo"
    wins = [('ciseaux', 'pierre'), ('pierre', 'papier'), ('papier', 'ciseaux')]
    if (player1, player2) in wins:
        return nom_joueur_2
    return nom_joueur_1

score_1 = 0
score_2 = 0
ppc = ["pierre", "papier", "ciseaux"]
nombre_manche = 0

response = get_valid_answer("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ", ['O', 'N'])
nom_joueur_1 = input("Quel est votre nom ? ")

if response == 'N':
    nom_joueur_2 = input("Quel est le nom du deuxième joueur ? ")
else:
    nom_joueur_2 = 'Machine'

while True:
    nombre_manche += 1
    choix_joueur_1 = get_valid_answer(f"{nom_joueur_1}, faîtes votre choix parmi (pierre, papier, ciseaux): ", ppc)

    if nom_joueur_2 == 'Machine':
        choix_joueur_2 = random.choice(ppc)
    else:
        choix_joueur_2 = get_valid_answer(f"{nom_joueur_2}, faîtes votre choix parmi (pierre, papier, ciseaux): ", ppc)

    print(f"Récapitulation : {nom_joueur_1} a choisi {choix_joueur_1} et {nom_joueur_2} a choisi {choix_joueur_2}\n")

    winner = determine_winner(choix_joueur_1, choix_joueur_2)
    score_1 += (winner == nom_joueur_1)
    score_2 += (winner == nom_joueur_2)

    print(f"Le gagnant est {winner}")
    print(f"Les scores à l'issue de cette manche sont donc {nom_joueur_1}: {score_1} et {nom_joueur_2}: {score_2}\n")

    if nombre_manche == 5:
        play_again = get_valid_answer(f"Souhaitez-vous refaire une partie {nom_joueur_1} contre {nom_joueur_2} ? (O/N): ", ['O', 'N'])
        if play_again == 'N':
            break

print("Merci d'avoir joué ! A bientôt")
