from os import system
from time import sleep
import random

system('cls')
backside = [[i+1]+['X']*4 for i in range(4)]
faceside = [[]*4 for i in range(4)]
card = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
steps = 0
guessed = 0
dance_frames = [
    '''
     O
    /|\\
    / \\
    ''',
    '''
     O
    \\|/
     |
    / \\
    ''',
    '''
     O
    /|\\
     |
    / \\
    ''',
    '''
     O
    \\|/
    / \\
    '''
]
def card_check(card_input):
    LETTERS = ['A', 'B', 'C', 'D']
    while True:
        while True:
            card_input = card_input.upper()
            if len(card_input) == 2 and card_input[0] in LETTERS and card_input[1] in ['1', '2', '3', '4']:
                card_input = [int(card_input[1]), LETTERS.index(card_input[0]) + 1]
                break
            else:
                card_input = input('Such coordinates don\'t exist. Try again: ')
        if backside[card_input[0]-1][card_input[1]] == 'X':
            break
        else:
            card_input = input('This card is already placed. Try again: ')
    return card_input

def print_board():
    print('   A  B  C  D')
    for i in range(4):
        for j in range(5):
            print(backside[i][j], end="  ")
        print()

for i in range(4):
    for j in range(4):
        faceside[i].append(card.pop(random.randint(0, len(card) - 1)))

while True:
    steps += 1
    print_board()
    card1 = input('Enter first card coordinates(A1, b3...): ')
    card1 = card_check(card1)

    backside[card1[0]-1][card1[1]] = faceside[card1[0]-1][card1[1]-1]
    system('cls')
    print_board()

    card2 = card_check(input('Enter second card coordinates(A1, b3...): '))

    backside[card2[0]-1][card2[1]] = faceside[card2[0]-1][card2[1]-1]
    system('cls')
    print_board()

    if backside[card1[0]-1][card1[1]] != backside[card2[0]-1][card2[1]]:
        sleep(2)
        backside[card1[0] - 1][card1[1]] = 'X'
        backside[card2[0] - 1][card2[1]] = 'X'
        system('cls')
    else:
        system('cls')
        guessed += 1
        if guessed == 8:
            print(f'You WON! \n You have made {steps} steps')
            while True:
                for frame in dance_frames:
                    system('cls')
                    print(f'You WON! \n You have made {steps} steps')
                    print(frame)
                    sleep(0.3)