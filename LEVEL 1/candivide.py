# 코딩테스트 연습 / 연습문제 / 나누어 떨어지는 숫자 배열
# 성공

def solution(arr:list, divisor:int) -> list:
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
            
    answer.sort()
    
    if not answer:
        return [-1]
    else:
        return answer