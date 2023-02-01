# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 다트 게임
import re

def solution(dartResult):
    answer = 0
    
    # 숫자와 연산을 list화
    numbers = re.findall(r'\d+', dartResult)
    numbers = list(map(int, numbers))
    operators = re.findall(r'[^\d]+', dartResult)
    
    # 연산을 숫자로 표현 (단, *의 경우  += 이전값*2 해줘야함을 유의)
    plus_dict = {'S':1, 'D':2, 'T':3}
    mul_dict = {'*': 2, '#':-1}
    
    # 이전 값 저장
    oneback = 0
    
    for number, operator in zip(numbers, operators):
        # 제곱 
        operand = number ** plus_dict[operator[0]]
        
        # 연산 문자열 길이가 2 이상일경우
        if len(operator) == 2:
            # 단순 곱셈
            operand *= mul_dict[operator[1]]
            if operator[1] == '*':
                # 이전값 한번 더 덧셈
                answer += oneback
                
        oneback = operand
        answer += operand
    return answer


# test case / answer = 37
print(solution('1S2D*3T'))