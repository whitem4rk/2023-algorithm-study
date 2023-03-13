# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 표현 가능한 이진트리

from math import ceil, log2
from collections import deque

def is_bintree(num:str, depth:int):
    q = deque()
    q.append((0,len(num),1,1))
    
    while q:
        start, end, cnt, parent_state = q.popleft()
        if cnt > depth:
            continue
        
        cur = (start + end) // 2
        print(start, end, cur)
        # 부모노드가 0인데 자식이 1이라면 false
        if num[cur] == '1' and parent_state == 0:
            return False
        elif num[cur] == '1'and parent_state == 1:
            q.append((start,cur,cnt+1,1))
            q.append((cur,end,cnt+1,1))
        elif num[cur] == '0':
            q.append((start,cur,cnt+1,0))
            q.append((cur,end,cnt+1,0))
    
    return True

def solution(numbers):
    answer = []
    
    for num in numbers:
        # num의 길이가 2^n -1 보다 작다면 0으로 채움
        num = str(bin(num))[2:]
        depth = ceil(log2(len(num)+1))
        new_num = num.zfill((2**depth)-1)
        # 이중트리가 맞는지 확인 (bfs)
        if is_bintree(new_num, depth):
            answer.append(1)
            continue    
        answer.append(0)
    return answer



answer = [1, 1, 0, 1]
my = solution([7, 42, 5, 15])
print(my)
print('correct') if answer == my else print('wrong')