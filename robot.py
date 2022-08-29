from weapon import Weapon

class Robot:
       def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon

       def attack_dinosaur(self, dinosaur):
              dinosaur.health = dinosaur.health - self.attack_power.weapon
              print(f'\n{self.name} attacked {dinosaur.name} with Shoulder Cannon for {self.attack_power.weapon} damage!\n{dinosaur.name} has {dinosaur.health} health remaining!')
              if (dinosaur.health <= 0):
                     print(f'\n{dinosaur.name} now EXTINCT!')