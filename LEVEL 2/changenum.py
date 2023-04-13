# 코딩테스트 연습 / 연습문제 / 숫자 변환하기
# 실패 - bfs 시간초과

def solution(x, y, n):
    dp = [1000000] * (y+1)
    dp[x] = 0
    for i in range(x, y):
        if i+n <= y:
            dp[i+n] = min((dp[i]+1), dp[i+n])
        if i*2 <= y:
            dp[i*2] = min((dp[i]+1), dp[i*2])
        if i*3 <= y:
            dp[i*3] = min((dp[i]+1), dp[i*3])        
            
    return -1 if dp[y] == 1000000 else dp[y]