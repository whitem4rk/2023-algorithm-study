# 코딩테스트 연습 / 2017 팁스타운 / 예상 대진표
# 실패

import math

def solution(n,a,b):
    answer = 0
    while True:       
        answer += 1
        
        diva = math.ceil(a/2)
        divb = math.ceil(b/2)
        
        if diva == divb:
            return answer
        
        a = diva
        b = divb