import random
chances = 5
attempts=[]
#number to be choosen
def number():
    num = random.randint(1,10)
    return num
#game
def game():
    sltd_num = number()
    choose_number = int(input('guess the number(between 1 and 10):'))
    if choose_number<1 and choose_number>10:
        print('Chose a valid number between 1 and 10')
game()