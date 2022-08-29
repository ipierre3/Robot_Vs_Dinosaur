class Dinosaur:  
       
 def __init__(self, name: str, attack_power: int):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

def attack_robot(self, robot):
       robot.health = robot.health - self.attack_power
       print(f'\n{self.name} attacked {robot.name} with a Tail Whip for {self.attack_power} damage!\n{robot.name} has {robot.health} health remaining!')
       if (robot.health <= 0):
              print(f'\n{robot.name} DESTROYED!')

