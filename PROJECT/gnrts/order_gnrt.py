import random

class ORD_AtGNRT:

    
    def __init__(self):
        self.date = []
        self.time = []
        self.year = random.randint(2019, 2024)
        self.month = random.randint(1,12)
        self.day = random.randint(1, 28 if self.month == 2 else 30 if self.month in [4, 6, 9, 11] else 31)
        self.hrs = random.randint(0, 23)
        self.min = random.randint(0, 59)
        self.sec = random.randint(0, 59)
    
    def gnrt_at(self):        
        self.date = f"{self.year}-{self.month:02d}-{self.day:02d}"
        self.time = f"{self.hrs:02d}:{self.min:02d}:{self.sec:02d}"
        return self.date, self.time
    
# n = ORD_AtGNRT()
# print(n.gnrt_at())
