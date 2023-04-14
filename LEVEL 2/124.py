# 코딩테스트 연습 / 연습문제 / 124 나라의 숫자
# 실패 - 못품

def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]