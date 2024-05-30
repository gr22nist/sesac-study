from printers.printer import DataPRT
from user_csv import US_DataGNRT
from store_csv import STR_DataGNRT
from item_csv import ITM_DataGNRT
from order_csv import ORD_DataGNRT
from orderitem_csv import ORDITM_DataGNRT


# 메인 함수

if __name__ == "__main__":
    print("데이터 타입을 선택하세요")
    print("1. user")
    print("2. store")
    print("3. item")
    print("4. order")
    print("5. orderitem")
    data_input = input("선택 : ")

    data_input_int = int(data_input)
    data_num = {1: "user", 2: "store", 3: "item", 4: "order", 5: "orderitem"}

    if data_input == 1:
        csv_data = US_DataGNRT()
        csv_data.gnrt_users(data_input_int)
    
    elif data_input == 2:
        csv_data = STR_DataGNRT()
        csv_data.gnrt_stores(data_input_int)
    
    elif data_input == 3:
        csv_data = ITM_DataGNRT()
        csv_data.gnrt_items(data_input_int)
    
    elif data_input == 4:
        csv_data = ORD_DataGNRT()
        csv_data.gnrt_orders(data_input_int)
        
    
    elif data_input == 5:
        csv_data = ORDITM_DataGNRT()
        csv_data.gnrt_orderitems(data_input_int)
        
    else:
        print("선택 오류입니다")
        exit(1)
        
    
    my_printer = DataPRT()
    
    print("출력 모드를 선택하세요")
    print("1. 화면 출력")
    print("2. 파일 저장")
    mode = input("선택 : ")
    
    if mode == '1':
        my_printer.print_to_screen(csv_data.data)
    
    elif mode == '2':
        my_printer.print_to_file(csv_data.data, f"{data_num[data_input_int]}.csv")
    else:
        print('선택 오류입니다')