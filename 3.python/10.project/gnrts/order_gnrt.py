import random
from datetime import datetime


# 아이템 메뉴 제너레이터

# class ITM_NameGNRT:
#     menus = pd.read_csv('menu.csv', encoding="cp949")
#     sample = menus['Name', 'Price', 'Type']
    
#     def __init__(self):
#         self.name = self.menus.loc(self.menus['Name'])

#         # with open('menu.csv', 'r', encoding='utf-8') as file:
#         #     names = file.read().split(",")
#         #     self.name = names

#     def gnrt_storename(self):
#         self.name = random.choice(self.name)
#         return self.name
        
# n = ITM_NameGNRT()
# print(n.gnrt_storename())


class ORD_AtGNRT:
    date = []
    time = []
    
    def gnrt_at(self):
        
        self.date = f"{random.randint(2019, 2024)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        self.time = f"{random.randint(0, 23):02d}:{random.randint(0, 59)}:{random.randint(0, 59)}"
        return self.date, self.time
    
n = ORD_AtGNRT()
print(n.gnrt_at())
