# 코딩테스트 연습 / 월간 코드 챌린지 시즌3 / n^2 배열 자르기
# 성공

def solution(n, left, right):
    answer = []
    
    for idx in range(left, right+1):
        result, remain = divmod(idx, n)
        answer. append(max(result+1, remain+1))
    
    return answer