import random

class NameGenerator:
  lnames = []
  fnames = []
 
  def __init__(self): 
    with open('l_names.txt', 'r', encoding='utf-8') as file:
      self.lnames = file.read().split(",")
    with open('f_names.txt', 'r', encoding='utf-8' ) as file:
      self.fnames = file.read().split(",")

  def gnrt_name(self):
    return f"{random.choice(self.lnames)}{random.choice(self.fnames)}"