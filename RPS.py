import random

class Outcomes():

    def __init__(self):
        self.player= []
        self.computer = []

    def player_choice(self):
        Ui = input('Rock/Paper/Scissors?: ')
        self.player.append(Ui)
        print(f'You choose: {Ui}')
        
    def computer_choice(self):
            options = random.choice(['rock', 'paper', 'scissors'])
            self.computer.append(options)
            print(f'Computer choose: {options}')

    def game_rules(self):
            if self.player[-1] == self.computer[-1]:
                    print(f'Draw game; both players selected {self.player[-1]}')
            elif self.player[-1] == 'paper':
                if self.computer[-1] == 'rock':
                    print("I win!")
                else:
                    print('Scissors cuts paper, ggs, you lose.')
            elif self.player[-1] == 'scissors':
                    if self.computer[-1] == 'paper':
                         print('Scissors cuts paper, ggs i win.')
                    else:
                         print('I rock you lose.')
            else: 
                if self.player[-1] == 'rock':
                    print('Long ago an rock smashed some scissors')
                else:
                    print('Paper covers rock. GGs')

my_game = Outcomes()

def PlayRPS():
    while True:
        i = input("Let's play rock, paper, scissors. You ready?: (start/q): q to quit: ")
        if i.lower() == 'start':
            my_game.player_choice()
            my_game.computer_choice()
            my_game.game_rules()
        elif i.lower() == 'q':
            break
        else:
            print("Invalid option. Choose another")

PlayRPS()