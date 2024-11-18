# hero.py

import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
    '''
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()
    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health

  def fight(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in.
    '''
    # TODO: Fight each hero until a victor emerges.
    # Phases to implement:
    #1) randomly choose winner,
    # Hint: Look into random library, more specifically the choice method 

    if(len(self.abilities) == 0 or len(opponent.abilities) == 0):
      print("Draw")
    else:
      while(self.is_alive() and opponent.is_alive()):
        damage_to_opponent = max(0, self.attack() - opponent.defend())
        opponent.take_damage(damage_to_opponent)
        damage_to_self = max(0, opponent.attack()- self.defend())
        self.take_damage(damage_to_self)
    if(self.is_alive()):
      print(f"{self.name} won!")
    else:
      print(f"{opponent.name} won!")

    

  def add_ability(self, ability):
    ''' Add ability to abilities list '''

    # We use the append method to add ability objects to our list.
    self.abilities.append(ability)

  def attack(self):
    total_damage = 0

    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage
    
  def add_armor(self, armor):
    self.armors.append(armor)

  def defend(self):
    if (len(self.armors) == 0) or self.current_health == 0:
      return 0
    else:
      total_block = 0
      for armor in self.armors:
        total_block += armor.block()
        return total_block
      
  def add_weapon(self, weapon):
    self.abilities.append(weapon)
      
  def take_damage(self, damage):
    self.current_health -= damage

  def is_alive(self):
    if self.current_health > 0:
      return True
    else:
      return False

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    weapon = Weapon("Lasso of Truth", 90)
    hero1.add_weapon(weapon)
    print(hero1.attack())