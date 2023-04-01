# 코딩테스트 연습 / 탐욕법(Greedy) / 구명보트
# 실패 - 시간초과

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people) > 1:
        big, small = people[-1], people[0]
        if limit < big + small:
            people.pop()
        else:
            people.pop()
            people.popleft()
        answer += 1
    
    return answer + 1 if len(people) == 1 else answer
        