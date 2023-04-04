# 코딩테스트 연습 / 연습문제 / N개의 최소공배수
# 실패

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def solution(arr):
    answer = arr[0]
    g = 1
    for a in arr:
        answer = (answer*a) / gcd(answer, a)
    return answer
    
