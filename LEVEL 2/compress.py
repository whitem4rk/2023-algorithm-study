# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / [3차] 압축

from string import ascii_uppercase
from collections import deque
def solution(msg):
    answer = []
    alpha = list(ascii_uppercase)
    # 알파벳 인덱스, 사용여부 저장
    alpha_dict = {}
    for idx,a in enumerate(alpha):
        alpha_dict[a] = idx+1
    
    str_check = ''
    msg_list = deque(msg)
    while len(msg_list):
        str_check += msg_list[0]
        
        if str_check in alpha_dict:
            msg_list.popleft()
        else:
            # 사전에 없다면 이전 문자까지만 저장
            alpha_dict[str_check] = len(alpha_dict) + 1
            answer.append(alpha_dict[str_check[:-1]])
            str_check = ''

        if len(msg_list) == 0:
            answer.append(alpha_dict[str_check])
        
    return answer


# test case / answer = 	[11, 1, 27, 15]
print(solution('KAKAO'))