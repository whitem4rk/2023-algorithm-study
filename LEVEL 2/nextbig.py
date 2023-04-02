# 코딩테스트 연습 / 연습문제 / 다음 큰 숫자
# 실패 - 시간초과

from collections import Counter

def solution(n):
    answer = 0
    nb = Counter(bin(n))
    n1 = nb['1']
    for i in range(n+1, 1000001):
        b1 = Counter(bin(i))['1']
        if b1 == n1:
            return i
