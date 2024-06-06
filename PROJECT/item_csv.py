from gnrts.common_gnrt import IdGRNT
from gnrts.item_gnrt import ITM_InfoGNRT
# from printers.printer import DataPRT

class ITM_DataGNRT:
    
    def __init__(self, num):
        self.data = []
        self.num = num
        self.id_gen = IdGRNT()
        self.info_gen = ITM_InfoGNRT()
        
    def gnrt_items(self):
        self.data.append(('Id','Name','Type','UnitPrice'))
        
        for _ in range(self.num):
            itmid = self.id_gen.gnrt_id()
            name, itmtype, price = self.info_gen.gnrt_types()
            
            self.data.append((itmid, name, itmtype, price))


# class DataPRT:
#   def print_to_screen(self, data):
#     for d in data:
#       print(d)
      
#   def print_to_file(self, data):
#     with open('./data/item.csv', 'w', encoding='utf-8') as csv_file:
#       csv_writer = csv.writer(csv_file)
#       for d in data:
#         csv_writer.writerow(d)

# # 메인 함수

# if __name__ == "__main__":
#     num_data = input("생성할 데이터의 개수를 입력하세요: ")

#     item1 = ITM_DataGNRT(int(num_data))
#     item1.gnrt_items()

#     my_printer = DataPRT()

#     print("출력 모드를 선택하세요")
#     print("1. 화면 출력")
#     print("2. 파일 저장")
#     mode = input("선택 : ")

#     if mode == '1':
#         my_printer.print_to_screen(item1.data)

#     elif mode == '2':
#         my_printer.print_to_file(item1.data)
#     else:
#         print('선택 오류입니다')