# 코딩테스트 연습 / 동적계획법(Dynamic Programming) / 등굣길

from collections import deque
dir = [[0,1],[1,0]]

def solution(m, n, puddles):
    maps = [[0] * (m+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            maps[i+1][j+1] = 1
    for x,y in puddles:
        maps[y][x] = 0
    
    dp = [ [0] * (m+2) for _ in range(n+2) ]
    dp[1][0] = 1
    q = deque([[1,1]])
    
    while q:
        i, j = q.popleft()
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 10000000007
        
        for x,y in dir:
            if maps[i+x][j+y] != 0:
                q.append([i+x, j+y])
    
    return dp[n][m]
