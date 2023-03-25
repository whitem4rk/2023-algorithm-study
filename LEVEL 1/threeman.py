# 코딩테스트 연습 / 연습문제 / 삼총사
# 성공

from itertools import combinations

def solution(number):
    answer = 0
    combination = combinations(number, 3)
    
    for comb in combination:
        if sum(comb) == 0:
            answer += 1
        
    return answer