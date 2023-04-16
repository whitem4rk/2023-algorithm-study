# 코딩테스트 연습 / 연습문제 / 미로 탈출
# 실패 - newmaps 크기 = n+2 * m+2

from collections import deque

direction = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i, j, final_i, final_j, newmaps):
    visited = set()
    q = deque([(i,j,0)])
    
    while q:
        r, c, cnt = q.popleft()
        if (r,c) in visited:
            continue
        visited.add((r, c))
        if (r,c) == (final_i,final_j):
            return cnt
        
        for x,y in direction:
            if newmaps[r+x][c+y] != 'X':
                q.append((r+x,c+y,cnt+1))
                
    return -1
        
    
    
def solution(maps):
    newmaps = [['X'] * (len(maps[0])+2) for _ in range(len(maps)+2)]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            newmaps[i+1][j+1] = maps[i][j]
    
    S = (0,0)
    E = (0,0)
    L = (0,0)
    for i in range(len(newmaps)):
        for j in range(len(newmaps[0])):
            if newmaps[i][j] == 'S':
                S = (i, j)
            if newmaps[i][j] == 'E':
                E = (i, j)
            if newmaps[i][j] == 'L':
                L = (i, j)
    
    stol = bfs(S[0], S[1], L[0], L[1], newmaps)
    ltoe = bfs(L[0], L[1], E[0], E[1], newmaps)
    if stol == -1 or ltoe == -1:
        return -1
    
    return stol + ltoe