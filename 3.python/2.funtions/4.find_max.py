numbers = [ -4, -17, -8, -6, -25, -3, -9. -22]

def find_max(numbers):
    max_num = numbers[0]
    
    for i in numbers[1:]:
        if i > max_num:
            max_num = i
            
    print(f'가장 큰 숫자는 {max_num} 입니다.')
            
find_max(numbers)