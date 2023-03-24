# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 내적
# 성공

def solution(a, b):
    answer = 0
    for _a, _b in zip(a,b):
        answer += _a*_b
    return answer