import random

def guessingGame():
    dealer_wins = 0
    player_wins = 0
    draws = 0
    rounds = 0
    while 1: 
        dealers_choice = random.randint(0, 100)
        try:
            players_choice = int(input('Player, please pick a number: '))

        except ValueError:
            return print('input needs to be a numeric value')
        
        print(f'Dealer has {dealers_choice}')
        players_choice_eval = abs(21 - players_choice)
        dealers_choice_eval = abs(21 - dealers_choice)

        if players_choice_eval < dealers_choice_eval:
            player_wins+=1
        elif players_choice_eval > dealers_choice_eval:
            dealer_wins+=1
        else:
            draws+=1
    
        rounds+=1
        if players_choice == 21:
            return print(f'Number of hands played: {rounds} Dealer won: {dealer_wins} Player won: {player_wins}. Tied: {draws}. You’re {player_wins} for {rounds}. Come back to the Bar Fork soon.')

guessingGame()