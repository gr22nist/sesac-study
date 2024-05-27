import sys

from gnrts.id_gnrt import IdGenerator
from gnrts.name_gnrt import NameGenerator
from gnrts.birthdate_gnrt import BirthdateGenerator
from gnrts.gender_gnrt import GenderGenerator
from gnrts.address_gnrt import AddressGenerator
from printers.printer import DataPrinter

class UserInfoGenerator:
    data = []
    num = 1
  
    def __init__(self, num):
        self.num = num
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.add_gen = AddressGenerator()
        
    def gnrt_users(self):
        self.data = []
            
        for _ in range(self.num):
            id = self.id_gen
            name = self.name_gen
            birthdate = self.birth_gen
            gender = self.gender_gen
            address = self.add_gen
            
            self.data.append((id, name, birthdate, gender, address))
      

# 메인 함수

if __name__ == "__main__":
    my_printer = DataPrinter()
    num_data = input("생성할 데이터의 개수를 입력: ") \
                if len(sys.argv) <= 1 else sys.argv[1]

    user1 = UserInfoGenerator(int(num_data))
    user1.gnrt_users()

    my_printer.print_to_screen(user1.data)

    if len(sys.argv) == 3:
        sys.argv[2] == 'screen' if my_printer.print_to_screen(user1.data) \
        else sys.argv[2] == 'file' if my_printer.print_to_file(user1.data) \
        else print("오류: 미지원 인자")
