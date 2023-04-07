# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 압축
# 실패

from string import ascii_uppercase

def solution(msg):
    cdict = {c:i+1 for i, c in enumerate(ascii_uppercase)}
    answer = []
    before, cur, curnum, curidx = '', '', 27, 0
    while curidx != len(msg):
        cur += msg[curidx]
        if cur in cdict:
            before = cur
            curidx += 1
        else:
            cdict[cur] = curnum
            answer.append(cdict[before])
            curnum += 1
            cur, before = '',''
    answer.append(cdict[cur])
    return answer