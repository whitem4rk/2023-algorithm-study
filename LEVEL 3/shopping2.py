# 코딩테스트 연습 / 2020 카카오 인턴십 / 보석 쇼핑
# 실패 - 요즘 잘 안풀림...

from collections import deque

def solution(gems):
    gemdict = {}
    q = deque()
    kind = len(set(gems))
    rangelen = 100003
    answer = []
    for idx, gem in enumerate(gems):
        if gem not in gemdict:
            gemdict[gem] = 0
        gemdict[gem] += 1
        q.append([idx+1,gem])
        
        while q and gemdict[q[0][1]] > 1:
            gemdict[q[0][1]] -= 1
            q.popleft()
        
        if len(gemdict) == kind and rangelen > (q[-1][0] - q[0][0]):
            rangelen = q[-1][0] - q[0][0]
            answer = [q[0][0],q[-1][0]]
    
    return answer