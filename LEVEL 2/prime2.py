# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / k진수에서 소수 개수 구하기
# 실패

def ntok(n, k):
    s = ''
    res, rem = 0, 0
    while True:
        n, rem = divmod(n, k)
        s = str(rem) + s
        if n == 0:
            break
    return s

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    kstring = ntok(n, k).split('0')
    answer = 0
    for s in kstring:
        if s != '' and isprime(int(s)):
            answer += 1
    return answer