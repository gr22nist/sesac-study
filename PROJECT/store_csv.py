from gnrts.common_gnrt import IdGRNT
from gnrts.common_gnrt import AddressGNRT
from gnrts.store_gnrt import STR_NameGNRT
from gnrts.store_gnrt import STR_TypeGNRT
# from printers.printer import DataPRT

import csv

class STR_DataGNRT:
    def __init__(self, num):
        self.data = []
        self.num = num
        self.id_gen = IdGRNT()
        self.name_gen = STR_NameGNRT()
        self.type_gen = STR_TypeGNRT()
        self.add_gen = AddressGNRT()
        
    
    def gnrt_stores(self):
        self.data.append(('Id','Name','Type','Address'))
        
        for _ in range(self.num):
            strid = self.id_gen.gnrt_id()
            strtype = self.name_gen.gnrt_store()
            name = f"{strtype} {self.name_gen.gnrt_store()}"
            address = self.type_gen.gnrt_type()
        
            self.data.append((strid, name, strtype, address)) 
            
        return self.data

# class DataPRT:
#     def print_to_screen(self, data):
#         for d in data:
#             print(d)
      
#     def print_to_file(self, data):
#         with open('./data/store.csv', 'w', encoding='utf-8') as csv_file:
#             csv_writer = csv.writer(csv_file)

#             for d in data:
#                 csv_writer.writerow(d)
        

# # 메인 함수

# if __name__ == "__main__":
#     num_data = input("생성할 데이터의 개수를 입력하세요: ")

#     store1 = STR_DataGNRT(int(num_data))
#     store1.gnrt_stores()

#     my_printer = DataPRT()

#     print("출력 모드를 선택하세요")
#     print("1. 화면 출력")
#     print("2. 파일 저장")
#     mode = input("선택 : ")

#     if mode == '1':
#         my_printer.print_to_screen(store1.data)

#     elif mode == '2':
#         my_printer.print_to_file(store1.data)
#     else:
#         print('선택 오류입니다')