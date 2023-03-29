# 코딩테스트 연습 / 연습문제 / 둘만의 암호
# 성공

from string import ascii_lowercase

def solution(s, skip, index):
    lowercase = ascii_lowercase
    for c in skip:
        lowercase = lowercase.replace(c, '')
    total = 26 - len(skip)
    
    answer = ''
    for c in s:
        idx = lowercase.index(c)
        idx = (idx+index) % total
        answer += lowercase[idx]
    
    return answer