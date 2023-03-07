# 코딩테스트 연습 / 2020 카카오 인턴십 / 수식 최대화

import re
from itertools import permutations

def solution(expression):
    sum_list = []
    # 숫자, 연산자 따로 관리
    nums = re.findall('\d+', expression)
    oper = re.findall('[^\d]', expression)
    # 우선순위 모든 경우의 수
    perm = list(permutations(['+','-','*'], 3))
    
    # 우선순위부터 oper에 연산처리를 한다음 num[i+1], oper[i] 삭제
    for per in perm:
        tmp_nums = nums.copy()
        tmp_oper = oper.copy()
        for p in per:
            idx = 0
            while idx != len(tmp_nums)-1:
                if tmp_oper[idx] == p:
                    result = eval(tmp_nums[idx]+tmp_oper[idx]+tmp_nums[idx+1])
                    tmp_nums[idx] = str(result)
                    tmp_nums.pop(idx+1)
                    tmp_oper.pop(idx)
                else:
                    idx += 1
        sum_list.append(abs(int(tmp_nums[0])))
        
    return sorted(sum_list,reverse=True)[0]


# test case 
answer = 60420
my_answer = solution("100-200*300-500+20")
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

