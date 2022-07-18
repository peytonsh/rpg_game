from random import randint
from tracemalloc import start


class Character:
    def __init__(self, health, power, coins):
        self.health = health
        self.power = power
        self.coins = coins

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def attack(self, enemy):
        
        if enemy.character_name != "zombie":
            enemy.health -= self.power 
     
        if(self.character_name == "hero"):
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        elif(self.character_name == "goblin" or self.character_name == "zombie"
             or self.character_name == "medic" or self.character_name == "shadow"
             or self.character_name == "dan" or self.character_name == "boss"):
            print(f"The {self.character_name} does {self.power} damage to you.")
        
            
    def print_status(self):
        if self.character_name == "hero":
            print (f"You have {self.health} health and {self.power} power.")
        elif (self.character_name == "goblin" or self.character_name == "zombie"
            or self.character_name == "medic" or self.character_name == "shadow"
             or self.character_name == "dan" or self.character_name == "boss"):
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        
    def coins(self):
        pass
                  
class Hero(Character):
    def __init__(self, health, power, coins):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power, coins)
            
    def attack(self, enemy):
        crit = randint(1,5)
        if crit == 3:
            enemy.health -= (self.power * 2)
            print(f'Critical damage!')
            print(f'Hero does {self.power * 2} damage to {enemy.character_name}!')
            hero.status
            enemy.status
        else:
            enemy.health -= self.power
            print(f'{self.character_name} does {self.power} damage to {enemy.character_name}.')
            hero.status
            enemy.status
        
               
class Goblin(Character):
    def __init__(self, health, power, coins):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power, coins)

class Zombie(Character):
    def __init__(self, health, power, coins):
        self.character_name = "zombie"
        super(Zombie, self).__init__(health, power, coins)
        
class Medic(Character):
    def __init__(self, health, power, coins):
        self.character_name = "medic"
        super(Medic, self).__init__(health, power, coins)
    def attack(self, enemy):
        crit = randint(1,5)
        if crit == 3:
            enemy.health += 2
            print(f'{self.character_name} regenerates 2 health')
        else:
            enemy.health -= self.power
            print(f'{self.character_name} does {self.power} damage to {enemy.character_name}.')

class Shadow(Character):
    def __init__(self, health, power, coins):
        self.character_name = "shadow"
        super(Shadow, self).__init__(health, power, coins)
    def attack(self, enemy):    
        crit = randint(1,10)
    if crit == 1:
        enemy.health -= self.power
    else:
        enemy.health -= self.power * 0
        print(f'{self.character_name} does {self.power} damage to {enemy.character_name}')
            
class Dan(Character):
    def __init__(self, health, power, coins):
        self.character_name = "dan"
        super(Dan, self).__init__(health, power, coins)
class Boss(Character):
    def __init__(self, health, power, coins):
        self.character_name = "boss"
        super(Boss, self).__init__(health, power, coins)
        
hero = Hero(10, 5)
goblin = Goblin(6, 2)
zombie = Zombie(1, 10)
medic = Medic(40, 10, 15)
shadow = Shadow(20, 10, 20)
dan = Dan(10, 10, 20)
boss  = Boss(50, 50, 30)
    
def main(enemy):
    
    while enemy.alive() > 0 and hero.alive():
       
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)
            
            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)
            
            if not hero.alive():
                print("""You are dead.
                      
                            
            ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
   
""")

quit()
   
main(goblin)

class store:
    def store():
        raw_input = input(f""" Welcome to the Shop
        1. Buy Supertonic
        2. Buy Armor
        3. Buy Evade
        4. Buy Sword
        5. Quit
        """)
    raw_input = input()
    if raw_input == "1":
            store()
    elif raw_input == "2":
            store()
    elif raw_input == "3":
            quit()
    else:
            main()
store()







