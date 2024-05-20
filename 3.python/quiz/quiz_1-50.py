# 01~10 ===========================================================begin

print(f'1번 답: Hello World')

print(f"2번 답: Mary's cosmetics")

print(f'3번 답: 신씨가 소리질렀다. "도둑이야".')

print(f"4번 답: C:\Windows")

print("안녕하세요.\n만나서\t\t반갑습니다.") # \n = 줄바꿈(multi-line) \t = tab

print("오늘은", "일요일")  # 오늘은 일요일

print('naver','kakao', 'sk','samsung', sep=';') # sep(separation), 구분자

print('naver','kakao', 'sk','samsung', sep='/')

print("first", end=""); print("second")

print(5/3)

# 11~20 ===================================================variable

삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액)) #type으로 자료유형 확인가능
print(현재가, type(현재가))
print(PER, type(PER))

s = "hello"
t = "python"
print(s+"!", t)

print(2+2*3) # 8

a = "132"
print(type(a)) # class 'str'

str1 = "720"
int1 = int(str1)
print(int1, type(int1))

int2 = 100
str2 = str(int2)
print(str2, type(str2))

str3 = "15.79"
float1 = float(str3)
print(float1, type(float1))

year = "2020"
print(int(year)-1)
print(int(year)-2)
print(int(year)-3)

월금액 = 48584
총금액 = 월금액 * 36
print(총금액)

# 21~50 ===========================================================string

lang = 'python'
print(lang[0],lang[2])

license_plate = "24가 2210"
print(license_plate[-4:])

string = "홀짝홀짝홀짝"
print(string[::2])  # print(string[1:6:2]) 짝짝짝

string = "PYTHON"
print(string[::-1]) # ::-1 reverse

cell_num = "010-1234-5678"
cell_num1 = cell_num.replace("-"," ")
print(cell_num1)

phone_num = "010-1234-5678"
phone_num1 = phone_num.replace("-","")
print(phone_num1)

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# lang = 'python'
# lang[0] = 'P'
# print(lang) # 문자열은 이뮤터블

string = 'abcdfe2a354a32a'
upper = string.replace('a','A')
print(upper)

string = 'abcd'
string.replace('b', 'B')
print(string) # abcd, 문자열은 이뮤터블로 적용 안된 상태로 출력

a = "3"
b = "4"
print(a + b)  # 34

print("Hi" * 3) # HiHiHi

print("-"*80)

t1 = 'python'
t2 = 'java'
tsum =t1+' '+t2+' '
print(tsum*4)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))  # %s 문자열타입의 값, %d 정수타입의 값, %?? 뭐지 이건
print("이름: %s 나이: %d" % (name2, age2))

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

상장주식수 = "5,969,782,550"
리플레이스 = 상장주식수.replace(",","")
정수변환 = int(리플레이스)
print(정수변환,type(정수변환))

분기 = "2020/03(E) (IFRS연결)"
분기절취선 = 분기.split('(')
print(분기절취선[0])

data = "   삼성전자    "
공백제거 = data.strip()
print(공백제거)

ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

ticker2 = "BTC_KRW"
ticker3 = ticker2.lower()
print(ticker3)

hll = 'hello'
hll1 = hll.capitalize()
print(hll1)

# file_name = "보고서.xlsx"
# file_name.endswith("xlsx", "xls") # 이거 왜 안돼

# file_name = "2020_보고서.xlsx"
# file_name.startswith("2020")  # ...? 원래 안되나?

aa = "hello world"
aaa = aa.split()
print(aaa)

ticker0 = "btc_krw"
ticker00 = ticker0.split("_")
print(ticker00)

date = "2020-05-01"
date0 = date.split("-")
print(date0)

data = "039490     "
data1 = data.rstrip()
print(data1)