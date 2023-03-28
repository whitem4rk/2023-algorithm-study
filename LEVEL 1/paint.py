# 코딩테스트 연습 / 연습문제 / 덧칠하기
# 성공

def solution(n, m, section):
    answer = 0
    topaint = [False] * (n+1)
    for sec in section:
        topaint[sec] = True
        
    idx = 1
    while idx <= n:
        if topaint[idx]:
            answer += 1
            idx += m
        else:
            idx += 1
    
    return answer