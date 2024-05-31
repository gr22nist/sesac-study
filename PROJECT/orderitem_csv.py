from gnrts.common_gnrt import IdGRNT

import csv
import random

class ORDITM_DataGNRT:

    def __init__(self, num):
        self.num = num
        self.data = []
        self.ordid = []
        self.itmid = []
    
        self.id_gen = IdGRNT()
        
        with open('./data/order.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)
            
            for d in reader:
                self.ordid.append(d)    
        
        with open('./data/item.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)
            for d in reader:
                self.itmid.append(d)    
    
    def gnrt_orderitems(self):
        self.data.append(('Id','OrderId','ItemId'))
        
        for _ in range(self.num):
            strid = self.id_gen.gnrt_id()
            ordids = random.choice(self.ordid)
            itmids = random.choice(self.itmid)

            self.data.append((strid, ordids['Id'], itmids['Id']))
            
        return self.data

# class DataPRT:
#   def print_to_screen(self, data):
#     for d in data:
#       print(d)
      
#   def print_to_file(self, data):
#     with open('./data/orderitem.csv', 'w', encoding='utf-8') as csv_file:
#       csv_writer = csv.writer(csv_file)
#       for d in data:
#         csv_writer.writerow(d)
        
        
# # 메인 함수

# if __name__ == "__main__":
#     num_data = input("생성할 데이터의 개수를 입력하세요: ")

#     odritm1 = ORDITM_DataGNRT(int(num_data))
#     odritm1.gnrt_orderitems()

#     my_printer = DataPRT()

#     print("출력 모드를 선택하세요")
#     print("1. 화면 출력")
#     print("2. 파일 저장")
#     mode = input("선택 : ")

#     if mode == '1':
#         my_printer.print_to_screen(odritm1.data)

#     elif mode == '2':
#         my_printer.print_to_file(odritm1.data)
#     else:
#         print('선택 오류입니다')