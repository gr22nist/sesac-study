# while 문: ~에 도달할때까지 반복

count = 0

print('while')
while (count <= 10): # 이 조건이 True인 동안
    print(count)
    count = count + 2
    

# for 문: 특정 목록 안에서의 반복

print('for')
for i in range(5):  # range(5) = [0, 1, 2, 3, 4]
    print(i)
    
users = ["kim", 'lee', 'park', 'jeong']
for name in users:
    print(name)
    

for num in [-5, 7, 135, 'kim', 'sesac']:
    print(num)
    
for i in range(3, 7):   # range(3, 7) = [3, 4, 5, 6]
    print(i)
    
for i in range(1, 10, 2):   # range(1, 10, 2) = [1, 3, 5, 7, 9]
    print(i)