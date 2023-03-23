# 코딩테스트 연습 / 연습문제 / 수박수박수박수박수박수?
# 성공

def solution(n):
    cnt = n // 2
    answer = '수박' * cnt
    if n % 2 == 1:
        answer += '수'
    return answer