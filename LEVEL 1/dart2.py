# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 다트 게임
# 실패 - re 숙련도 부족

import re

def solution(dartResult):
    oplist = re.findall('\D\D?', dartResult)
    numlist = re.findall('\d\d?', dartResult)
    three = [0,0,0]
    for idx in range(len(numlist)):
        num, exp = int(numlist[idx]), oplist[idx][0]
        if exp == 'D':
            num = num ** 2
        elif exp == 'T':
            num = num ** 3
            
        if len(oplist[idx]) == 2:
            if oplist[idx][1] == '*':
                num *= 2
                if idx != 0:
                    three[idx-1] *= 2
            elif oplist[idx][1] == '#':
                num *= -1
                
        three[idx] = num
    return sum(three)
            
solution("1S2D*3T")