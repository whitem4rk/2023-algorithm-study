# 코딩테스트 연습 / 연습문제 / 두 정수 사이의 합
# 성공

def solution(a, b):
    if a > b:
        a, b = b, a
    
    s = 0
    for i in range(a,b+1):
        s += i
    
    return s