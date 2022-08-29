from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.active_weapon = []
    
    def run_game(self):
        self.display_welcome()
        self.battlephase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side can win!\n')

    def battle_phase(self):
        shoulder_cannon = active_weapon.Weapon("Shoulder Cannon", 50, 50)
        self.active_weapon = [shoulder_cannon]

        terminator = robot.Robot('T-1000', self.active_weapon[0])

        t_rex = dinosaur.Dinosaur('T-Rex', 70)

    def display_winner(self):
        if winner == 'Robot':
            print(f'{robot.name} Wins!')
        else:
            print(f'{dinosaur.name} Wins!')

