# 코딩테스트 연습 / 연습문제 / 최대공약수와 최소공배수
# 완전 실패 - 유클리드 호제법 잘못알고있었음...

def getgcd(a:int, b:int) -> int:
    if a < b:
        a, b = b, a
    
    if a % b == 0:
        return b
    return getgcd(b, a%b)

def solution(n, m):
    gcd = getgcd(n,m)
    lcm = n * m / gcd
    
    return [gcd, lcm]