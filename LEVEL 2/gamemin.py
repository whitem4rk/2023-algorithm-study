# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 게임 맵 최단거리
# 실패

from collections import deque

dir = [(1,0),(-1,0),(0,1),(0,-1)]

def solution(maps):
    n, m = len(maps), len(maps[0])
    newmap = [[0] * (m+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            newmap[i+1][j+1] = maps[i][j]        
    
    visited = [[False] * (m+2) for _ in range(n+2) ]
    q = deque([(1,1,1)])
    while q:
        cur_row, cur_col, cur_cnt = q.popleft()
        if visited[cur_row][cur_col]:
            continue
        
        visited[cur_row][cur_col] = True
        if cur_row == n and cur_col == m:
            return cur_cnt
            
        for row, col in dir:
            r = cur_row + row
            c = cur_col + col
            if newmap[r][c] == 1:
                q.append((r,c,cur_cnt+1))
    
    return -1