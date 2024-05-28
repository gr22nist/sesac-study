import generators
import csv

class DataGNRT:
    def __init__(self, num):
        self.num = num
        self.id_gen = generators.IdGRNT()
        self.name_gen = generators.NameGNRT()
        self.birth_gen = generators.BirthGNRT()
        self.gender_gen = generators.GenderGNRT()
        self.address_gen = generators.AddressGNRT()
        
    
    def gnrt_users(self):
        self.data = []
        for _ in range(self.num):
            id = self.id_gen.gnrt_id()
            name = self.name_gen.gnrt_name()
            birthdate = self.birth_gen.gnrt_birthdate()
            gender = self.gender_gen.gnrt_gender()
            address = self.address_gen.gnrt_address()
            
            self.data.append((id, name, birthdate, gender, address)) 
            
        return self.data
    
class DataPRT:
    def print_to_screen(self, data):
        for d in data:
            print(d)
            
    def print_to_file(self, data):
        with open('output.csv', 'w', encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            for d in data:
                writer.writerow(d)
            
            
# 메인 함수

if __name__ == "__main__":
    num_data = input("생성할 데이터의 개수를 입력하세요: ")
    
    user1 = DataGNRT(int(num_data))
    user1.gnrt_users()
    
    my_printer = DataPRT()
    
    print("출력 모드를 선택하세요")
    print("1. 화면 출력")
    print("2. 파일 저장")
    mode = input("선택 : ")
    
    if mode == '1':
        my_printer.print_to_screen(user1.data)
    
    elif mode == '2':
        my_printer.print_to_file(user1.data)
    else:
        print('선택 오류입니다')