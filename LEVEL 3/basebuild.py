# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 기지국 설치
# 실패 - O(N) 발상 실패

import math

def solution(n, stations, w):
    answer = 0
    start = 1
    
    for station in stations:
        end = max(1, station - w)
        if end > start:
            answer += math.ceil((end - start) / (2*w+1))
        start = station + w + 1
    
    if start <= n:
        end = n
        answer += math.ceil((end-start+1) / (2*w+1))
    
    return answer
        
    