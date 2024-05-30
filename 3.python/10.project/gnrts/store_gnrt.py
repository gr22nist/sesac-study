import random

class STR_TypeGNRT:
    
    def __init__(self):
        self.type = []
        
        with open('brands.txt', 'r', encoding='utf-8') as file:
            types = file.read().split(',')
            self.type = types

    def gnrt_type(self):
        
        return random.choice(self.type)

# t = STR_TypeGNRT()
# print(t.gnrt_type())

class STR_NameGNRT:
    
    def __init__(self):
        self.store = []

        with open('stores.txt', 'r', encoding='utf-8') as file:
            stores = file.read().split(',')
            self.store = stores

    def gnrt_store(self):
        
        return f"{random.choice(self.store)}{random.randint(1,15)}호점"
    
# s = STR_NameGNRT()
# print(s.gnrt_store())