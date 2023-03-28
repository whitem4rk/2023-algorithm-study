# 코딩테스트 연습 / 연습문제 / 기사단원의 무기
# 실패 - 시간초과

def solution(number, limit, power):
    answer = 0
    cntlist = [0] * (number+1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            cntlist[j] += 1
    
    for cnt in cntlist:
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    
    return answer