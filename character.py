import random

from combat import Combat

class Character(Combat):
  attack_limit = 10
  experience = 0
  basehit_points = 10
  
  def attack(self): #overriding attack method from combat.py
      roll = random.randint(1, self.attack_limit)
      if self.weapon =='sword': #give extra points to sword & axe
          roll += 1
      elif self.weapon == 'axe':
          roll +=2
          return roll > 4
        
  def get_weapon(self):
    weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
    
    if weapon_choice in 'sab':
      if weapon_choice == 's':
        return 'sword'
      elif weapon_choice == 'a':
        return 'axe'
      else: 
        return 'bow'  
    else:
      return self.get_weapon()
    
  def __init__(self, **kwargs):
    self.name = input("Name: ")
    self.weapon = self.get_weapon()
    self.hitpoints = self.basehit_points()
    
    for key, value in kwargs.items():
      setattr(self, key, value)
  
  def --str--(self):
    return "{}, HP: {}, XP{}".format(self.name, self.hit_points, self.expereince)
  
  def rest(self):
    if self.hit_points < basehit_points:
      self.hit_points += 1
      
  def leveled_up(self):
    if self.experience:
      self.hit_points >= 5