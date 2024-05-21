# 1. 반복문을 이용하여 화면에 삼각형 출력하기

# row = input('출력을 원하는 높이를 입력하세요')
# num_rows = int(row)
# for i in range(num_rows):
#     print('*' * i)
    
# row = input('출력을 원하는 높이를 입력하세요')
# for i in range(int(row)):
#     print('*' * i)

row = 5
for i in range(1, row+1):
    print('*' * i)

for i in range(1, row+1):
    print(' ' *(row-i), '*' * i)
    

for i in range(1, row+1):
    print(' ' * (row-i), '*' * i)
    
for i in range(1, row+1):
    print(' ' * (row-i),'*' * (2 * i - 1))
    
for i in range(1, row+1):
    print(' ' * (row-i),'*' * (2 * i - 1))