# 코딩테스트 연습 / 연습문제 / 명예의 전당 (1)
# 실패 - 문제 조건 빠뜨림

import heapq

def solution(k, score):
    answer = []
    honor = []
    
    for i in range(len(score)):
        heapq.heappush(honor, score[i])
        if len(honor) == k+1:
            heapq.heappop(honor)
        answer.append(min(honor))            
    
    return answer