# 코딩테스트 연습 / 힙(Heap) / 더 맵게
# 실패 - heapify를 해줘야하는지 몰랐음

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        if len(scoville) == 1:
            if heappop(scoville) < K:
                return -1
            else:
                break
        else:
            num1 = heappop(scoville)
            if num1 >= K:
                break
            num2 = heappop(scoville)

            heappush(scoville, num1 + num2*2)
            answer += 1
    return answer