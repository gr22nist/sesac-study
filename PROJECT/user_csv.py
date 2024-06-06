from gnrts.common_gnrt import IdGRNT
from gnrts.common_gnrt import AddressGNRT
from gnrts.user_gnrt import NameGNRT
from gnrts.user_gnrt import BirthGNRT
from gnrts.user_gnrt import GenderGNRT

import csv

class US_DataGNRT:
    
    def __init__(self, num):
        self.data = []
        self.num = num
        self.id_gen = IdGRNT()
        self.name_gen = NameGNRT()
        self.birth_gen = BirthGNRT()
        self.gender_gen = GenderGNRT()
        self.address_gen = AddressGNRT()
        
    def gnrt_users(self):
        self.data.append(('Id','Name','Gender','Age','Birthdate','Address'))
        
        for _ in range(self.num):
            usid = self.id_gen.gnrt_id()
            name = self.name_gen.gnrt_name()
            age, birth = self.birth_gen.gnrt_birthdate()
            gender = self.gender_gen.gnrt_gender()
            address = self.address_gen.gnrt_address()
            
            self.data.append((usid, name, gender, age, birth, address))
            
        return self.data

# u = US_DataGNRT()
# print(u.gnrt_users())

# class DataPRT:
#   def print_to_screen(self, data):
#     for d in data:
#       print(d)
      
#   def print_to_file(self, data):
#     with open('./data/user.csv', 'w', encoding='utf-8') as csv_file:
#       csv_writer = csv.writer(csv_file)
#       for d in data:
#         csv_writer.writerow(d)
        

# # # 메인 함수

# if __name__ == "__main__":
#     num_data = input("생성할 데이터의 개수를 입력하세요: ")

#     user1 = US_DataGNRT(int(num_data))
#     user1.gnrt_users()

#     my_printer = DataPRT()

#     print("출력 모드를 선택하세요")
#     print("1. 화면 출력")
#     print("2. 파일 저장")
#     mode = input("선택 : ")

#     if mode == '1':
#         my_printer.print_to_screen(user1.data)

#     elif mode == '2':
#         my_printer.print_to_file(user1.data)
#     else:
#         print('선택 오류입니다')