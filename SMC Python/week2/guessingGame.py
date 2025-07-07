import random

def guessingGame():
    dealers_choice = random.randint(0, 100)
    try:
        players_choice = int(input('Player, please pick a number: '))

    except ValueError:
        return print('input needs to be a numeric value')
    
    print(f'Dealer has {dealers_choice}')
    players_choice_eval = abs(21 - players_choice)
    dealers_choice_eval = abs(21 - dealers_choice)

    if players_choice_eval < dealers_choice_eval:
        print('Player wins')
    elif players_choice_eval > dealers_choice_eval:
        print('Dealer wins')
    else:
       print("It's a draw") 
    

guessingGame()