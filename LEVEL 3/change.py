# 코딩테스트 연습 / 연습문제 / 거스름돈
# 실패

def solution(n, money):
    dp = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            dp[i] = (dp[i] + dp[i-m]) % 1000000007
    return dp[n]
