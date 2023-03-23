# 코딩테스트 연습 / 연습문제 / 약수의 합

def solution(n):
    
    if n == 0:
        return 0
    
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
    
    return sum(arr)