# 코딩테스트 연습 / 연습문제 / 정수 제곱근 판별
# 실패 - 예외처리 놓침

def solution(n):
    if n == 1:
        return 4
    
    for i in range(1, n):
        if i**2 == n:
            return (i+1)**2
    return -1
