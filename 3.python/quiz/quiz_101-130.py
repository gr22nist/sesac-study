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

#122

# score = input('score: ')
# score = int(score)
# if 81 <= score <= 100:
#     print('grade is A')
# elif 61 <= score <= 80:
#     print('grade is B')
# elif 41 <= score <= 60:
#     print('grade is C')
# elif 21 <= score <= 40:
#     print('grade is D')
# else:
#     print('grade is E')

# 123

# exchange = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
# user = input("입력 :")
# num, currency = user.split()
# print(float(num) * exchange[currency], "원")

# num1 = input("number1: ")
# num2 = input("number2: ")
# num3 = input("number3: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)
    
# 125

# number = input('휴대폰 번호를 입력하세요: ')
# num = number.split("-")[0]
# if num == "011":
#     com = ("SKT")
# elif num == "016":
#     com = ("KT")
# elif num == "019":
#     com = ("LGU")
# else: 
#     com =("알 수 없음")
    
# print(f'당신은 {com} 사용자입니다.')

# 126

# num = input('우편번호: ')
# num = num[:3]
# if num in ['010', '011','012']:
#     print("강북구")
# elif num in ['013', '014','015']:
#     print("도봉구")
# else:
#     print("노원구")

# 127

# num = input('주민등록번호를 입력하세요: ')
# nums = num.split("-")[1]
# if nums[0] == "1" or nums[0] == "3":
#     print("남자")
# else: 
#     print("여자")

# 128

# 주민번호 = input('주민등록번호를 입력하세요: ')
# 뒷자리 = 주민번호.split("-")[1]
# if 0 <= int(뒷자리[1:3]) <= 8:
#     print("서울입니다")
# else:
#     print("서울이 아닙니다")

# 129

# num = input('주민등록번호를 입력하세요: ')
# sum1 = int(num[0]*2) + int(num[1]*3) + int(num[2]*4) + \
#        int(num[3]*5) + int(num[4]*6) + int(num[5]*7) + \
#        int(num[7]*8) + int(num[8]*9) + int(num[9]*2) + \
#        int(num[10]*3) + int(num[11]*4) + int(num[12]*5)
# sum2 = 11 - (sum1 % 11)
# sum3 = str(sum2)
# if num[-1] == sum3[-1]:
#     print('유효한 주민등록번호입니다')
# else:
#     print('유효하지 않은 주민등록번호입니다')

# 130

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])

# if 시가 + 변동폭 > 최고가:
#     print('상승장')
# else:
#     print('하락장')
