# 131

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
    
# 사과
# 귤
# 수박


# 132

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")

#####
#####
#####

# 133

# for 변수 in ["A", "B", "C"]:
#   print(변수)

# 변수 = "A"
# print(변수)
# 변수 = "B"
# print(변수)
# 변수 = "C"
# print(변수)

# 134

# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
  
# 변수 = "A"
# print("출력:", 변수)
# 변수 = "B"
# print("출력:", 변수)
# 변수 = "C"
# print("출력:", 변수)

# 135

# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
  
# 변수 = "A" 
# b = 변수.lower()
# print("변환:", b)
# 변수 = "B" 
# b = 변수.lower()
# print("변환:", b)
# 변수 = "C" 
# b = 변수.lower()
# print("변환:", b)

# 136

# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

# for 변수 in [10, 20, 30]:
#   print(변수)
  
# 리스트 = [10, 20, 30]
# for 변수 in 리스트:
#   print(변수)

# 137

# list = [10, 20, 30]
# for num in list:
#   print(num)
  
# 138

# list = [10, 20, 30]
# line = ('-------')
# for num in list:
#   print(num)
#   print(line)
  
# 139

# list = [ 10, 20, 30]
# print('++++')
# for num in list:
#   print(num)

# 140
# for l in [1, 2, 3, 4]:
#   print("-------")

# 141

# list = [100, 200, 300]
# for l in list:
#   print(l + 10)

# 142

# list = ["김밥", "라면", "튀김"]
# for l in list:
#   print('오늘의 메뉴:', l)

# 143

# stock = ["SK하이닉스", "삼성전자", "LG전자"]

# for s in stock:
#   print(len(s))

# 144

# animal = ['dog', 'cat', 'parrot']

# for a in animal:
#   print(a, len(a))
  
# 145

# animal = ['dog', 'cat', 'parrot']
# for a in animal:
#   print(a[0])


# 146

# num = [1, 2, 3]
# for n in num:
#   print("3 x", n)

# 147

# num = [1, 2, 3]

# for n in num:
#   print("3 x", n, "=", 3 * n )

# for n in num:
#   print("3 x {} = {}".format(n, 3 * n))

# 148

# list = ["가", "나", "다", "라"]
# list = list[1:]
# for l in list:
#   print(l)
  
# for l in list[1:]:
#   print(l)
  
# 149

# list = ["가", "나", "다", "라"]
# for l in list[::2]:
#   print(l)
  
# 150

# list = ["가", "나", "다", "라"]
# for l in list[::-1]:
#   print(l)

# 151

# list = [3, -20, -3, 44]
# for n in list:
#   if n < 0:
#     print(n)

# 152

# list = [3, 100, 23, 44]
# for m in list:
#   if m % 3 == 0:
#     print(m)

# 153

# list = [13, 21, 12, 14, 30, 18]
# for m in list:
#     if (m % 3 == 0) and (m < 20):
#       print(m)
      
# 154

# list = ["I", "study", "python", "language", "!"]
# for w in list:
#   if len(w) >= 3:
#     print(w)

# 155

# list = ["A", "b", "c", "D"]
# for u in list:
#   if u.isupper():
#     print(u)
    
# 156

# list = ["A", "b", "c", "D"]
# for u in list:
#   if u.islower():
#     print(u)

# 157

# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a[0].upper() + a[1:])

# 158

# list = ['hello.py', 'ex01.py', 'intro.hwp']
# for s in list:
#     s = s.split('.')
#     print(s[0])

# 159

# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for f in list:
#   file = f.split('.')
#   if file[1] == 'h':
#     print(f)
  
# 160

# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for file in list:
#   f = file.split('.')
#   if (f[1] == 'h') or (f[1] == 'c'):
#     print(file)


# 161

# for i in range(100):
#   print(i)

# 162

# for i in range(2002, 2051, 4):
#   print(i) 

# 163

# for i in range(3, 31, 3):
#   print(i)

# 164

# for i in range(100):
#   print(99 - i)

# 165

# for i in range(10):
#   print(i / 10)

# 166

# for g in range(1, 10):
#   n = g * 3
#   print(f'3x{g} = {n}')

# for g in range(1, 10):
#   print(3, "x", g, "=", 3 * g)


# 167

# num = 3
# for g in range(1, 10, 2):
#   if g % 2 == 1:
#     print(num, "x", g, "=", num * g)
  
# 168

# plus = 0
# for i in range(1, 11):
#   plus += i
#   print("합: ", plus)

# 169

# plus = 0
# for i in range(1, 11, 2):
#   plus += i
#   print("합: ", plus)

# 170

# result = 1
# for i in range(1, 11):
#   result *= i
#   print(result)

# 171

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#   print(price_list[i])

# 172

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#   print(i, price_list[i])

# for i, data in enumerate(price_list):
#     print(i, data)

# 173

# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print((len(price_list) - 1) - i, price_list[i])

# 174

# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])

# 175
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1):
#   print(my_list[i], my_list[i+1])

# for i in range(1, len(my_list)):
#   print(my_list[i-1], my_list[i])

# 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list) - 2):
#   print(my_list[i], my_list[i+1], my_list[i+2])
   
# 177

# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1, 0, - 1):
#   print(my_list[i], my_list[i-1])
  
# 178

# my_list = [100, 200, 400, 800]
# for i in range(len(my_list) - 1):
#   print(abs(my_list[i+1] - my_list[i]))

# 179

# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(1, len(my_list) - 1):
#   print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180

# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []
# for i in range(len(low_prices)):
#   volatility.append(high_prices[i] - low_prices[i])
#   print(volatility)

# 181


# 182


# 183


# 184


# 185


# 186


# 187


# 188


# 189


# 190


# 191


# 192


# 193


# 194


# 195


# 196


# 197


# 198


# 199


# 200