# 코딩테스트 연습 / 연습문제 / 크기가 작은 부분 문자열
# 실패 - 인덱스 문제

def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer
