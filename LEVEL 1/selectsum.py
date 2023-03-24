# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 두 개 뽑아서 더하기
# 성공

from itertools import combinations

def solution(numbers):
    answer = set()
    comb = combinations(numbers, 2)
    
    for c in comb:
        answer.add(sum(c))
        
    return sorted(list(answer))