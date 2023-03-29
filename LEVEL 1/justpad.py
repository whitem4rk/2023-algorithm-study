# 코딩테스트 연습 / 연습문제 / 대충 만든 자판
# 실패 - 인덱스, 문제조건

from string import ascii_uppercase

def solution(keymap, targets):
    answer = []
    pad_dict = {}
    
    for c in ascii_uppercase:
        pad_dict[c] = 101
    
    for key in keymap:
        for idx, c in enumerate(key):
            if pad_dict[c] > idx+1:
                pad_dict[c] = idx+1
    
    for target in targets:
        cnt = 0
        for t in target:
            if pad_dict[t] == 101:
                cnt = -1 
                break
            cnt += pad_dict[t]
        answer.append(cnt)
    return answer
