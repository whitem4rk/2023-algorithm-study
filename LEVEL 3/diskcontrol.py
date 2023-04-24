# 코딩테스트 연습 / 힙(Heap) / 디스크 컨트롤러
# 성공

from heapq import heappush, heappop

def solution(jobs):
    reqheap = []
    total_time = 0
    timetable = [[] for _ in range(1000001)]
    progress = 0
    
    for job in jobs:
        time, req = job
        timetable[time].append(req)
    
    for i in range(1000001):
        for req in timetable[i]:
            heappush(reqheap, req)
        
        if progress == 0 and len(reqheap) != 0:
            progress = heappop(reqheap)
        elif progress == 0 and len(reqheap) == 0:
            continue

        total_time += (len(reqheap) + 1)
        progress -= 1
        
    return total_time // len(jobs)