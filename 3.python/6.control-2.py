# if 문: 조건문

x = 50

if (x < 10):    # 이 조건이 True 일 때
    print('x가 10보다 작습니다.')
else:   # 이 조건이 False 일 때
    print('x가 10보다 큽니다.')
    
score = 92

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
    
print(score, grade)

print("score: {}; grade: {}".format(score, grade))

print("score: {0}; grade: {1}".format(score, grade))
print("score: {1}; grade: {0}".format(score, grade))

print('점수는 {score} 이고, 성적은 {grade} 입니다.')    # 문자열
print(f'점수는 {score} 이고, 성적은 {grade} 입니다.')   # 포맷팅

math = 90
eng = 80

if math >= 90 and eng >= 90:
    print('졸업조건 충족')
else:
    print('졸업조건 미흡')
    
if math >= 90 or eng >= 90:
    print('졸업조건 충족')
else:
    print('졸업조건 미흡')