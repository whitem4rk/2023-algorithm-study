# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 약수의 개수와 덧셈
# 성공

def solution(left, right):
    answer = 0
    is_even = [True] * (right+1)
    
    for i in range(1, right):
        i = i**2
        if i > right:
            break
        else:
            is_even[i] = False
    
    for idx in range(left, right+1):
        if is_even[idx]:
            answer += idx
        else:
            answer -= idx
    
    return answer