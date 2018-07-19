import random


class Roll:
    def __init__(self, name):
        self.name = name

    def roll_combat(self, roll_one, roll_two):
        if roll_one == 'rock' and roll_two == 'scissors':
            return True
        elif roll_one == 'paper' and roll_two == 'rock':
            return True
        elif roll_one == 'scissors' and roll_two == 'paper':
            return True
        else:
            return False


class Player:
    def __init__(self, name):
        self.name = name

    def ask_player_name(self):
        name = input('Please type your name: ')
        return name

    def computer_roll(self, rolls):
        random_roll = random.choice(rolls)
        return random_roll

    def player_roll(self):
        my_roll = input('Type Rock, Paper or Scissors!')
        return my_roll.lower()
