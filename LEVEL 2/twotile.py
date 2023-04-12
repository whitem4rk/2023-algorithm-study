# 코딩테스트 연습 / 연습문제 / 2 x n 타일링
# 실패

import sys
sys.setrecursionlimit(1000000)

def recursion(n, arr):
    if arr[n] != 0:
        return arr[n]
    
    if n == 1 or n == 2:
        return n
    
    else:
        arr[n] = (recursion(n-1, arr) + recursion(n-2, arr))%1000000007 
        return arr[n]

def solution(n):
    arr = [0] * (n+1)
    arr[1], arr[2] = 1, 2
    return recursion(n, arr)
