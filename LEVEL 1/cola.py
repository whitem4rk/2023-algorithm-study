# 코딩테스트 연습 / 연습문제 / 콜라 문제
# 성공

def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break
        n += b-a
        answer += b
    return answer