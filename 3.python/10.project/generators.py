import random
import uuid
import datetime
import pandas as pd

class NameGNRT:
    
    def __init__(self):
        self.lname = []
        self.fname = []
    
        with open('lnames.txt', 'r', encoding='utf-8') as file:
            self.lname = file.read().split(',')

        with open('fnames.txt', 'r', encoding='utf-8') as file:
            self.fname = file.read().split(',')
        
        # return self.lname, self.fname

    def gnrt_name(self):
        return f"{random.choice(self.lname)}{random.choice(self.fname)}"


# n = NameGNRT()
# print(n.gnrt_name())
    

class IdGRNT:
    def gnrt_id(self):
        return str(uuid.uuid4())

# id = IdGRNT()
# print(id.gnrt_id())


class GenderGNRT:
    gender = ["Male", "Female"]
    
    def gnrt_gender(self):
        return random.choice(self.gender)
    
# gd = GenderGNRT()
# print(gd.gnrt_gender())



class BirthGNRT:
    
    def __init__(self):
        self.months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
    
    def gnrt_birthdate(self):
        year = random.randint(1958, 2005)
        month = random.choice(self.months)
        day = random.randint(1, 28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31)
        
        current_year = datetime.datetime.now().year
        age = current_year - year
        
        return f"{year}-{month:02d}-{day:02d}, {age}세"

# b = BirthGNRT()
# print(b.gnrt_birthdate())

class AddressGNRT:
    def __init__(self):
        self.cities = []
        
        with open('cities.txt', 'r', encoding='utf-8') as file:
            city = file.read().split(',')
            self.cities = city
            # self.street1 = random.randint(1, 300)
            # self.street2 = random.randint(1, 50)
            
    def gnrt_address(self):
        return  f"{random.choice(self.cities)} {random.randint(1, 300)}번길 {random.randint(1, 50)}"

# a = AddressGNRT()
# print(a.gnrt_address())


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




class ITM_NameGNRT:
    menus = pd.read_csv('menu.csv', encoding="cp949")
    sample = menus['Name', 'Price', 'Type']
    
    def __init__(self):
        self.name = self.menus.loc(self.menus['Name'])

        # with open('menu.csv', 'r', encoding='utf-8') as file:
        #     names = file.read().split(",")
        #     self.name = names

    def gnrt_storename(self):
        
        return random.choice(self.name)
        
n = ITM_NameGNRT()
print(n.gnrt_storename())
