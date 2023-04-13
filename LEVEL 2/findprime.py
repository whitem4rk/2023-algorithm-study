# 코딩테스트 연습 / 완전탐색 / 소수 찾기
# 성공

from itertools import permutations

def isprime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numlist = []
    numset = set()
    
    for i in range(1,len(numbers)+1):
        numlist += permutations(list(numbers), i)
    for i in range(len(numlist)):
        numset.add(int(''.join(numlist[i])))
    
    print(numset)
    for num in numset:
        if isprime(num):
            answer += 1
    
    return answer