def hello():
    print('hello1')
    print('hello2')
    print('hello3')
    
# hello()

def numbers(num1):
    result = num1 + 4
    return result

print(numbers(3))
print(numbers(4))

def numbers(num1):
    result = num1 + 4
    return result

num1 = numbers(3)
num2 = numbers(4)

print(num1)
print(num1, num2)

# ==============================

def plus(num1, num2):
    sum = num1 + num2
    return sum

print(plus(10,20))


def add(num1, num2):
    return num1 + num2

print(add(10, 20))

def add2(num1, num2):
    return num1, num2, num1 + num2

print(add2(1, 2))


def sub(num1, num2):
    sum = num1 - num2
    return sum

print(sub(10,20))   # -10


def mul(num1, num2):
    sum = num1 * num2
    return sum

print(mul(20,10))   # 200


def div(num1, num2):
    sum = num1 / num2
    return sum

print(div(27,8))   # 3.375

print(sub(5, 0))
print(mul(2, 0))
print(div(5, 0))    # ZeroDivision Error