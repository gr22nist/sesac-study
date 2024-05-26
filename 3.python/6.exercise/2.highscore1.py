# 게임 스코어 저장하기
# 점수와 이름 입력받기
# 다양한 모드(score/high/history) 기능 구현

score_dic = {}  

def user_input():
    name = input("당신의 이름을 입력하세요: ")
    
    try:
        score = int(input("당신의 점수를 입력하세요: "))
        score_dic[name] = score
    except ValueError:
        print("입력 오류: 점수는 정수로만 입력 가능합니다")
        return
    
    score_dic[name]
    
def high_md():
    high_score = max(list(score_dic.values()))
    for h in score_dic:
        if score_dic[h] == high_score:
            print("name: ", h, "  |  score: ", score_dic[h])

def history_md():
    for h in score_dic.keys():
        print("name: ", h, "  |  score: ", score_dic[h])
        
        
def select_md():
    print("< 모드 선택 >")
    print("1. 점수 등록, 2. 최고 점수, 3. 등록 일람")
    print()
    
    mode_num = input("원하시는 모드의 번호를 입력하세요: ")

    if mode_num == "1":
        user_input()
        return
    
    elif mode_num == "2":
        high_md()
        return
    
    elif mode_num == "3":
        history_md()
        return
    else:
        print("입력 오류: 올바른 모드선택이 아닙니다")
        

while(True):
    print("")
    print("== High Score! == ", end="\n\n")
    select_md()
    print()

