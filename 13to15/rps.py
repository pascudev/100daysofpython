def main():
    game_header()
    game_loop()

def game_header():
    print('----------------------------------')
    print('      ROCK - PAPER - SCISSORS')
    print('----------------------------------')
    print()

def game_loop():

    while True:

        if win or exit:
            break


user_name = input('Please type your name: ')
print(f'Hi {user_name}!')

user_choice = input('Choose [R]ock, [P]aper or [S]cissors!')

