# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 점프와 순간 이동
# 성공

def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 1:
            n -= 1
            ans += 1
        else:
            n /= 2
    return ans