import random

#number that the player has to guess
def number_selection():
    num = random.randint(1,10)
    return num

#guessed number
def guessed_number():
    return int(input('guess the number(between 1 and 10):'))

#game
def start_game():
    chances = 5
    attempts = []
    sltd_num = number_selection()
    choose_number = guessed_number()
    if choose_number<1 or choose_number>10:
        print('Choose a valid number between 1 and 10')
        choose_number = guessed_number()
    elif choose_number == sltd_num:
        chances-=1
        print('Hurray, you have guessed the number')

