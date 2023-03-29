# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 신규 아이디 추천
# 실패 - 정규식 미숙, index 실수

import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    new_list = re.findall('[a-zA-Z0-9]|-|_|\.', new_id)
    new_id = ''.join(new_list)
    # 3
    while True:
        next_id = new_id.replace('..','.')
        if next_id == new_id:
            break
        new_id = next_id
    # 4
    if len(new_id) >= 2:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) == 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
    
    # 5
    if len(new_id) == 0:
        new_id = 'a'
    
    #6 
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id