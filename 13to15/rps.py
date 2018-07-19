from gamez import Roll, Player


def main():
    game_header()

    rock = Roll('rock')
    paper = Roll('paper')
    scissors = Roll('scissors')

    rolls = [rock, paper, scissors]
    name = input('Please type your name: ')

    player1 = name
    player2 = Player('NPC')

    game_loop(rolls, player1, player2)

def game_header():
    print('----------------------------------')
    print('      ROCK - PAPER - SCISSORS')
    print('----------------------------------')
    print()

def game_loop(rolls, player1, player2):

    count = 1
    while count < 3:
        p2_roll = Player.computer_roll(rolls)
        p1_roll = Player.player_roll()

        veredict = Roll.roll_combat(p1_roll, p2_roll)

        print(f'The veredict is {veredict}')

        count += 1


if __name__ == '__main__':
    main()

