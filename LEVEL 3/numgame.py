# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 숫자 게임
# 성공

def solution(A, B):
    answer = 0
    i = 0
    A.sort()
    B.sort()
    for b in B:
        if A[i] < b:
            answer += 1
            i += 1
            
    return answer