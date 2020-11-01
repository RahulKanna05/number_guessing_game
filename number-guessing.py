import random
import time
from termcolor import colored

#number that the player has to guess
def number_selection():
    num = random.randint(1,10)
    return num

#guessed number
def guess_number():
    return int(input('Guess the number(between 1 and 10): '))

#prints highest score
def score(attempt_list):
    print(colored('Your highest score is {}'.format(min(attempt_list)),'red'))


#game
def start_game():
    chances = 5
    attempts_list = []
    print('Hi,Welcome to Number Guessing Game')
    playername = input("Enter your name: ")

    print('''In this game, the computer selects a number between 1 and 10.
     The player has to guess the number. He/she is awarded with 5 chances.
     Therefore the player has to guess the number within 5 attempts.''')

    game_status=input('''So {}, shall we begin the game?
    Press Y to start the game: '''.format(playername.upper()))

    print('''Computer is selecting a number
    ...
    ...''')
    sltd_num = number_selection()  # computer selects the number
    time.sleep(2)
    print('''Computer has selected the number.
    {}, now its your turn to guess the correct number(remember you only have 5 chances to guess the correct number)'''.format(playername.upper()))
    while game_status.lower() == 'y':

        try:
            if chances != 0:
                guess = guess_number()  # player guesses the number
                if guess<1 or guess>10:
                    time.sleep(1)
                    raise ValueError()

                elif guess == sltd_num :
                    time.sleep(1)
                    chances-=1
                    attempt = 5-chances
                    attempts_list.append(attempt)
                    print(colored('Hurray!!! You have guessed the correct number in {} attempts.\n'.format(attempt),'blue'))
                    score(attempts_list)
                    time.sleep(1)
                    game_status = input('''\nDo you want to play again?
    Press 
        'Y' to continue.
        'N' to exit: ''')
                    if game_status.lower() == 'y':
                        chances=5
                        print('''Computer is selecting a number
                        ...
                        ...''')
                        sltd_num = number_selection()
                        time.sleep(2)
                        print('''Computer has selected the number.
    {}, now its your turn to guess the correct number(remember you only have 5 chances to guess the correct number'''.format(playername.upper()))
                    elif game_status.lower() == 'n':
                        break

                elif guess > sltd_num :
                    time.sleep(1)
                    print('Oops! You have guessed a larger number')
                    chances-=1
                    print('You are left with {} chances'.format(chances))

                elif guess < sltd_num :
                    time.sleep(1)
                    print('Oops! You have guessed  a smaller number')
                    chances-=1
                    print('You are left with {} chances'.format(chances))

            elif chances == 0:
                print('Sorry, you ran out of chances.')
                print('You have used all your 5 chances')
                attempts_list.append(5)
                print('The correct answer is {}\n'.format(sltd_num))
                time.sleep(1)
                score(attempts_list)
                game_status=input('''Well played!
    Do you wanna try again?
    Press 
        'Y' to continue.
        'N' to exit.''')
                if game_status.lower() == 'y':
                    chances=5
                    print('''Computer is selecting a number
                    ...
                    ...''')
                    sltd_num = number_selection()
                    time.sleep(2)
                    print('''Computer has selected the number.
    {}, now its your turn to guess the correct number(remember you only have 5 chances to guess the correct number)'''.format(
                        playername))
                elif game_status.lower() == 'n':
                    break

        except ValueError as err:
            print('Invalid number/expression')
            print('Try again...')

    print(colored('HIGHEST SCORE:','red'),colored(min(attempts_list),'red'))
    print("Thank you for playing the game")

start_game()


