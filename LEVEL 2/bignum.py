# 코딩테스트 연습 / 정렬 / 가장 큰 수
# 실패 - 발상부터 실패

def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(answer)))

