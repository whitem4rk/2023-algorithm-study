# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 예산

from itertools import combinations

def solution(d:list, budget:int) -> int:
    d.sort()
    
    cur_sum = 0
    for idx, money in enumerate(d):
        cur_sum += money
        if cur_sum > budget:
            return idx
    return len(d)
