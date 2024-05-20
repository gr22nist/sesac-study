# 51~70 ==========================================================list

movie_rank = ['닥터 스트레인지','스플릿','럭키']
print(movie_rank)

movie_rank.append('배트맨')
print(movie_rank)

movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3] # del 과 .remove는 무슨 차이지?
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2] # 삭제하면 새로 인덱싱 되어 순서가 바뀌니 고려해서 삭제
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

nums = [1, 2, 3, 4, 5]
print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

nums = [1, 2, 3, 4, 5]
aver = sum(nums) / len(nums)
print(aver)

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])  # [::2] 도 되긴 하는데 무슨 차이일까

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

string = "삼성전자/LG전자/Naver"
result = string.split("/")
print(result)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)

# 71~80 =============================================tuple

my_variable = ()

movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

int_tuple = (1,)

# t = (1, 2, 3)
# t[0] = 'a'  # tuple은 이뮤터블

t = 1, 2, 3, 4
print(t)  # 괄호가 없어도 tuple

# t = ('a', 'b', 'c') # 'A' 추가는 불가능
# t = ('A', 'b', 'c') 새로 만들어야 함

interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)

interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data)

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

data = tuple(range(2,100,2))
print(data)

# 81~100 =============================================dictionary

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score, b = scores
print(valid_score)

temp = {}

icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(icecream)

icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print("메로나 가격: ", ice["메로나"])

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

# ice['메로나'] = 1300

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice['메로나']
print(ice)

# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']  # 없는 키 써서

inventory = {"메로나": [300,20], "비비빅": [400,3], "죠스바": [250,100]}
print(inventory)

print(inventory["메로나"][0], "원")

print(inventory["메로나"][1], "개")

inventory["월드콘"] = [500,7]
print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice= list(icecream.keys())
print(ice)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice= list(icecream.values())
print(ice)

print(sum(icecream.values()))

new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)
