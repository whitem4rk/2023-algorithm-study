# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 미로 탈출 명령어

# 그리디, DFS  
# 궁금증 - BFS로도 풀 수 있을까? / 수행 시간 계산은 어떻게 하지?
from collections import deque

def solution(n, m, x, y, r, c, k):
    mincnt = abs(r-x) + abs(c-y)
    if (k - mincnt)%2 != 0 or (k - mincnt) < 0:
        return "impossible"
    
    q = deque()
    q.append((x,y,0,''))
    while q:
        curx, cury, cnt, path = q.pop()
        if cnt == k and (curx, cury) == (r, c):
            return path
        mincnt = abs(curx-r) + abs(cury-c)
        # 거리가 너무 멀어지면 무효
        if mincnt > k-cnt:
            continue    
        
        if curx > 1:
            q.append((curx-1, cury, cnt+1, path+'u'))
        if cury < m:
            q.append((curx, cury+1, cnt+1, path+'r'))
        if cury > 1:
            q.append((curx, cury-1, cnt+1, path+'l'))
        if curx < n:
            q.append((curx+1, cury, cnt+1, path+'d'))
    

answer = "dllrl"
my = solution(3,4,2,3,3,1,5)
print(my)
print('correct') if answer == my else print('wrong')