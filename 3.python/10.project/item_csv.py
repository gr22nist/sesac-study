from generators import IdGRNT
from generators import ITM_NameGNRT
from generators import ITM_TypeGNRT
from generators import ITM_PRCGNRT

import csv

class DataGNRT:
    def __init__(self, num):
        self.num = num
        self.id_gen = IdGRNT()
        self.name_gen = ITM_NameGNRT()
        self.type_gen = ITM_TypeGNRT()
        self.price_gen = ITM_PRCGNRT()
        
    
    def gnrt_items(self):
        self.data = []
        for _ in range(self.num):
            itmid = self.id_gen.gnrt_id()
            itmtype = self.type_gen.gnrt_type()
            itmname = f"{itmtype} {self.name_gen.gnrt_store()}"
            itmprice = self.address_gen.gnrt_address()
            
            self.data.append((itmid, itmname, itmtype, itmprice)) 
            
        return self.data
    
class DataPRT:
    def print_to_screen(self, data):
        for d in data:
            print(d)
            
    def print_to_file(self, data):
        with open('store.csv', 'w', encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            for d in data:
                writer.writerow(d)
            
            
# 메인 함수

if __name__ == "__main__":
    num_data = input("생성할 데이터의 개수를 입력하세요: ")
    
    store1 = DataGNRT(int(num_data))
    store1.gnrt_stores()
    
    my_printer = DataPRT()
    
    print("출력 모드를 선택하세요")
    print("1. 화면 출력")
    print("2. 파일 저장")
    mode = input("선택 : ")
    
    if mode == '1':
        my_printer.print_to_screen(store1.data)
    
    elif mode == '2':
        my_printer.print_to_file(store1.data)
    else:
        print('선택 오류입니다')