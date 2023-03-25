# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 소수 만들기
# 성공

from itertools import combinations

def isprime(num:int) -> bool:
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(nums:list) -> int:
    answer = 0
    comb = combinations(nums, 3)
    for c in comb:
        if isprime(sum(c)):
            answer += 1
    return answer