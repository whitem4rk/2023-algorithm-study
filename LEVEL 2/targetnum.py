# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 타겟 넘버
# 실패 - 중복순열

from itertools import product

def solution(numbers, target):
    answer = 0
    pro = product([1,-1], repeat=len(numbers))
    for p in pro:
        arr = [x if sign==1 else x*-1 for sign,x in zip(p,numbers)]
        if target == sum(arr):
            answer += 1
    return answer