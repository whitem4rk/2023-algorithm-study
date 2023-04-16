# 코딩테스트 연습 / 힙(Heap) / 이중우선순위큐
# 실패 - remove로는 너무 오래걸릴거라 생각했는데 되네...

from heapq import heappush, heappop

def solution(operations):
    small = []    
    for oper in operations:
        cmd, num = oper.split()
        num = int(num)
        
        if cmd == 'I':
            heappush(small, num)
        elif cmd == 'D':
            if len(small) == 0:
                continue
            elif num == 1:
                small.remove(max(small))
            elif num == -1:
                heappop(small)
                
    BIG = 0 if len(small) == 0 else max(small)
    SMALL = 0 if len(small) == 0 else min(small)
    return [BIG, SMALL]