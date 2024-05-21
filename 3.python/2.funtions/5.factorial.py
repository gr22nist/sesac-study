def factorial(n):
    print('팩토리알을 계산하시오')
    # for i in range(1, n+1):
    result = 1
    
    for i in range(n, 0, -1):
        result = result * i
        
    print(f'{n} 팩토리알은 {result} 입니다.')
        
factorial(5)
factorial(7)
factorial(10)