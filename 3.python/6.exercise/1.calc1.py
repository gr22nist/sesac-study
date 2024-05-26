# 계산기 코드 작성하기
# 1. 연산자 및 두개의 숫자를 입력받아 그 결과를 입력하시오
# 2. 무한반복

def operator(num1, op, num2):
    if op == "+":
        return (num1 + num2)
    elif op == "-":
        return (num1 - num2)
    elif op == "*":
        return (num1 * num2)
    
    elif op == "/":
        try:
            return (num1 / num2)
        except ZeroDivisionError:
            print("오류: 0으로 나눌 수 없습니다")
            return

def calc():
    op_list = ["+", "-", "*", "/"]
    try:
        num1 = float(input("첫번째 숫자 입력: "))
    except ValueError:
        print("오류: 올바른 숫자가 아닙니다")
        return

    op = input("연산자 입력: (덧셈: +, 뺄셈: -, 곱셈: *, 나눗셈: /): ")
    if op not in op_list:
        print("올바른 연산자가 아닙니다")
        return

    try:      
        num2 = float(input("두번째 숫자 입력: "))
    except ValueError:
        print("오류: 올바른 숫자가 아닙니다")
        return 

    else:
        print(f"결과값: {operator(num1, op, num2)}", end="\n\n")
        print("Ctrl+C 입력시 종료됩니다")
    
while(True):
    print("")
    print("== 사칙연산 계산기== ", end="\n\n")
    calc()
    print("")


