from gnrts.common_gnrt import IdGRNT
from gnrts.order_gnrt import ORD_AtGNRT
import csv
import random

class ORD_DataGNRT:
    
    def __init__(self, num):
        self.num = num
        self.data = []
        self.strid = []
        self.usid = []
        
        self.ordid_gen = IdGRNT()
        self.ordat_gen = ORD_AtGNRT()
        
        with open('store.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for d in reader:
                self.strid.append(d)    
        
        with open('user.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for d in reader:
                self.usid.append(d)
        
    def gnrt_orders(self):
        self.data.append(('Id','OrderAt','StoreId','UserId'))
        for _ in range(self.num):
            ordid = self.ordid_gen.gnrt_id()
            ordat = self.ordat_gen.gnrt_at()
            strids = random.choice(self.strid)
            usids = random.choice(self.usid)
            
            self.data.append((ordid, ordat, strids['Id'], usids['Id'])) 
            
        return self.data

# n = ORD_DataGNRT()
# print(n.gnrt_orders())


class DataPRT:
    def print_to_screen(self, data):
        for d in data:
            print(d)

    def print_to_file(self, data):
        with open('item.csv', 'w', encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            for d in data:
                writer.writerow(d)


# 메인 함수

if __name__ == "__main__":
    num_data = input("생성할 데이터의 개수를 입력하세요: ")

    item1 = ORD_DataGNRT(int(num_data))
    item1.gnrt_orders()

    my_printer = DataPRT()

    print("출력 모드를 선택하세요")
    print("1. 화면 출력")
    print("2. 파일 저장")
    mode = input("선택 : ")

    if mode == '1':
        my_printer.print_to_screen(item1.data)

    elif mode == '2':
        my_printer.print_to_file(item1.data)
    else:
        print('선택 오류입니다')