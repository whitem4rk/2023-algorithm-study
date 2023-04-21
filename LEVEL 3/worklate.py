# 코딩테스트 연습 / 연습문제 / 야근 지수
# 실패 - 힙 써도 시간초과 날거같아서 O(n) 방법을 고민했는데 힙이 정답이네...

from heapq import heappush, heappop

def solution(n, works):
    if n > sum(works):
        return 0
    
    newworks = []
    for work in works:
        heappush(newworks, -work)
    
    while n > 0:
        cur = heappop(newworks)
        cur += 1
        n -= 1
        heappush(newworks, cur)
    
    newsum = [x**2 for x in newworks]
    return sum(newsum)