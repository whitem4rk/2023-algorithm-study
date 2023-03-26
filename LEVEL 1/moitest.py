# 코딩테스트 연습 / 완전탐색 / 모의고사
# 성공

def solution(answers):
    answer = []
    num1 = [1,2,3,4,5] * 20000
    num2 = [2,1,2,3,2,4,2,5] * 1250
    num3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnt1, cnt2, cnt3 = 0, 0, 0 
    for i in range(len(answers)):
        if answers[i] == num1[i]:
            cnt1 += 1
        if answers[i] == num2[i]:
            cnt2 += 1
        if answers[i] == num3[i]:
            cnt3 += 1
    
    m = max(cnt1, cnt2, cnt3)
    if cnt1 == m:
        answer.append(1)
    if cnt2 == m:
        answer.append(2)
    if cnt3 == m:
        answer.append(3)
        
    
    return answer