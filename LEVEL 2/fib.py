# 코딩테스트 연습 / 연습문제 / 피보나치 수
# 실패 - 런타임에러(재귀함수 제한)

import sys
limit_number = 1000000
sys.setrecursionlimit(limit_number)

dp = [-1] * 100001
dp[0] = 0
dp[1] = 1
dp[2] = 1

def fib(n, dp):
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = (fib(n-1, dp) + fib(n-2, dp)) % 1234567
    return dp[n]


def solution(n):
    return fib(n, dp)