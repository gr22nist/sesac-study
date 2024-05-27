import random
import csv
from itertools import chain

class AddressGenerator:
  cities = []
  
  def __init__(self):
    with open('cities.txt', 'r', encoding='utf-8') as file:
      csvreader = csv.reader(file)
      csv_list_city = [c for c in csvreader]
      cities_list = list(chain(csv_list_city))
      self.cities = [c.split(',') for c in cities_list]
      
  def gnrt_address(self):
    city = random.choice(self.cities)
    street = random.randint(1,200)
    return f"{city} {street}"