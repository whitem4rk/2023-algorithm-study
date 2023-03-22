# 코딩테스트 연습 / 연습문제 / x만큼 간격이 있는 n개의 숫자
# 성공

def solution(x, n):
    return [x*(i+1) for i in range(n)]