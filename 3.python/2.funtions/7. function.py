# 함수의 인자에 기본값을 설정하려면?

def print_gugudan(dan=2, max=9):
    print(f'{dan}단')
    for i in range(1, max+1):
        print(f'{dan} x {i} = {dan * i}')
        
print_gugudan(3, 30)

print_gugudan(dan=3, max=9)

print_gugudan(max=9)