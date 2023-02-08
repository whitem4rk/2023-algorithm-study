# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / k진수에서 소수 개수 구하기
import re

# n을 k진수 str으로 변환
def ntok(n:int, k:int) -> int:
    result = ''
    while n != 0:
        n, mod = divmod(n,k)
        result += str(mod)
    return result[::-1]

# 소수판별
def is_prime(n:int) -> bool:
    if n != 1:
        # 제곱근 n이 아닌 그냥 n을 썼을때 시간초과
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
    else:
        return False
    return True

def solution(n, k):
    obj = ntok(n,k)
    # 문자열에서 0+ 을 기준으로 split
    nozero = re.split('0+',obj)
    final = []
    for num in nozero:
        if num == '':
            continue
        if is_prime(int(num)):
            final.append(num)
    
    return len(final)

# test case / answer = 3
print(solution(437674,3))