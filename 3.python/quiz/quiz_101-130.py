# 101~130 ==========================================================반복문

# bool

# print(3 == 5) # False, == 같다

# print(3 < 5)  # True, < ~ 보다 적은

# x = 4
# print(1 < x < 5)     # True 

# print ((3 == 3) and (4 != 3))      # True, != 같지 않다

# # print(3 => 4)      # 연산자 없음

# # if 4 < 3:
# #     print("Hello World")    # 조건 불충분

# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")     #      Hi, there.

# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")    # 1 2 4

# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")    # 3 5


# user = input('문자를 입력하세요: ')
# print(user*2)

# user = input('숫자를 입력하세요: ')
# print(10+ int(user))

# num1 = input('숫자를 입력하세요: ')
# if int(num1) %2==0:
#        print("짝수입니다")      # %2==0 정수 나눗셈 이후 나머지를 산출,
# else:print("홀수입니다")        # 오른쪽 인수가 0인 경우 ZeroDivisionError

# user = input('입력값: ')
# num1 = 20 + int(user)
# if num1 > 255:
#        print(255)
# else: print(num1)

# user = input('입력값: ')
# num1 = int(user) - 20
# if num1 > 255:
#        print(255)
# elif num1 < 0:
#        print(0)
# else: print(num1)

# time = input('현재시간: ')
# if time[-2] == '00':
#        print('정각 입니다')
# else: print('정각이 아닙니다')

# fruit = ["사과", "포도", "홍시"]
# user = input('좋아하는 과일은? ')
# if user in fruit:
#        print('정답입니다.')
# else: print('오답입니다.')

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input('관심있는 투자 종목: ')
# if user in warn_investment_list:
#        print('투자 경고 종목입니다.')
# else: print('투자 경고 종목이 아닙니다.')

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# user = input("제가 좋아하는 계절은: ")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# user = input("알파벳 하나 입력해주세요: ")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())

score = input('score: ')
score = int(score)
if 81 <= score <= 100:
    print('grade is A')
elif 61 <= score <= 80:
    print('grade is B')
elif 41 <= score <= 60:
    print('grade is C')
elif 21 <= score <= 40:
    print('grade is D')
else:
    print('grade is E')