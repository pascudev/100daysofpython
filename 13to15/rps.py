from classes import Roll, Player


def main():
    game_header()
    game_loop()


def game_header():
    print('----------------------------------')
    print('      ROCK - PAPER - SCISSORS')
    print('----------------------------------')
    print()


def game_loop():

    rolls = [Roll('rock'), Roll('paper'), Roll('scissors')]
    name = input('Please type your name: ')

    player1 = name

    count = 1
    while count < 6:

        p1 = Player(player1)
        p2 = Player('NPC')
        r = Roll(rolls)

        p2_roll = p2.computer_roll(rolls)
        p1_roll = p1.player_roll()

        veredict = r.roll_combat(p1_roll, p2_roll)

        if veredict == False:
            print(f'{p1.name} rolled {p1_roll}, {p2.name} rolled {p2_roll}! {p2_roll} defeats {p1_roll}! {p2.name} wins!!')
        elif veredict == True:
            print(f'{p1.name} rolled {p1_roll}, {p2.name} rolled {p2_roll}! {p1_roll} defeats {p2_roll}! {p1.name} wins!!')
        else:
            print(f'Its a tie!! Both players rolled {p1_roll}!!')

        count += 1


if __name__ == '__main__':
    main()
