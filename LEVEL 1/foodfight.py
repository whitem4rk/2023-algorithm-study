# 코딩테스트 연습 / 연습문제 / 푸드 파이트 대회
# 성공

def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i) * (food[i] // 2)
    
    answer = answer + '0' + answer[::-1]
    
    return answer