# 코딩테스트 연습 / 연습문제 / 최솟값 만들기
# 성공  

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += a*b
    return answer