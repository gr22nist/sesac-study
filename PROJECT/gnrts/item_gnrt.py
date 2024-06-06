import random

class ITM_InfoGNRT:
    data = {}
    child_dict = {}
    
    def __init__(self):
        
        with open('./data/type.csv', 'r', encoding='utf-8') as file:
            self.types = file.read().split(',')
        
        for t in self.types:
        
            with open(f"./data/{str(t)}.csv", 'r', encoding='utf-8') as file:
                self.iteminfo = file.read().splitlines()
                
                for i in self.iteminfo:
                    idata = i.split(',')
                    name = idata[0]
                    price = idata[1]
                    self.child_dict[name] = price
                self.data[t] = self.child_dict
            self.child_dict = {}

    def gnrt_types(self):
        
        itmtype = random.choice(list(self.data.keys()))
        name = random.choice(list(self.data[itmtype].keys()))
        price = self.data[itmtype][name]
        
        return name, itmtype, price

# i = ITM_InfoGNRT()
# print(.gnrt_types())