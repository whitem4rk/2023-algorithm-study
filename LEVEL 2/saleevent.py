# 코딩테스트 연습 / 연습문제 / 할인 행사
# 성공

from collections import Counter

def solution(want, number, discount):
    answer = 0
    wantlist = []
    for w, n in zip(want, number):
        wantlist += [w] * n
    wantlist = Counter(wantlist)
    
    for i in range(len(discount)-9):
        tmp = Counter(discount[i:i+10])
        if tmp == wantlist:
            answer += 1
    return answer