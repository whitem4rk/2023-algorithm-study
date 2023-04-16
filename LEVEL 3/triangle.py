# 코딩테스트 연습 / 동적계획법(Dynamic Programming) / 정수 삼각형
# 실패 - deepcopy

import copy

def solution(triangle):
    dp = copy.deepcopy(triangle)
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = 0
    dp[0][0] = 0
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i][j]+triangle[i][j], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i][j]+triangle[i][j], dp[i+1][j+1])
    last = [ a+b for a,b in zip(triangle[-1], dp[-1])]
    return max(last)
