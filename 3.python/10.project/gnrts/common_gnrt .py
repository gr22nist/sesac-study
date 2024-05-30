import random
import uuid

class IdGRNT:
    def gnrt_id(self):
        return str(uuid.uuid4())

# id = IdGRNT()
# print(id.gnrt_id())

class AddressGNRT:
    def __init__(self):
        self.cities = []
        
        with open('cities.txt', 'r', encoding='utf-8') as file:
            city = file.read().split(',')
            self.cities = city

    def gnrt_address(self):
        return  f"{random.choice(self.cities)} {random.randint(1, 300)}번길 {random.randint(1, 50)}"

# a = AddressGNRT()
# print(a.gnrt_address())