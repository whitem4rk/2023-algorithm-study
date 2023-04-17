# 코딩테스트 연습 / 연습문제 / 최고의 집합
# 실패 - 나머지만큼 1씩 더하는 생각을 못함

def solution(n, s):
    answer = []
    
    result, remain = divmod(s, n)
    if result == 0:
        return [-1]
    answer = [result] * n
    for i in range(remain):
        answer[n-i-1] += 1
    
    return answer