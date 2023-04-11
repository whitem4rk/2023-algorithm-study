# 코딩테스트 연습 / 완전탐색 / 모음사전
# 실패 - product 인자, tuple처리

from itertools import product

def solution(word):
    dict = []
    for i in range(1,6):
        dict += list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
    dict.sort()
    return dict.index(tuple(word)) + 1