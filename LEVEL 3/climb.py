# 코딩테스트 연습 / 2022 KAKAO TECH INTERNSHIP / 등산코스 정하기

from heapq import heappush, heappop

def solution(n:int, paths:list, gates:list, summits:list):
    graph = [[] for _ in range(n+1)]
    summits = set(summits)
    
    # edge 생성
    for path in paths:
        v1, v2, w = path
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    
    visited = [float('inf')] * (n+1)
    q = [(0, gate) for gate in gates]
    
    while q:
        cur_inte, cur = heappop(q)
        if visited[cur] <= cur_inte:
            continue
        else:
            visited[cur] = cur_inte
        if cur in summits:
            continue
        
        for v2, w in graph[cur]:
            w = max(w, cur_inte)
            if visited[v2] <= w:
                continue
            heappush(q, (w, v2))

    answer = [float('inf'), 0]
    for summit in summits:
        if answer[0] > visited[summit]:
            answer[0] = visited[summit]
            answer[1] = summit
        elif answer[0] == visited[summit] and summit < answer[1]:
            answer[1] = summit
        
    return answer[::-1]
    
    

answer = [5,1]
my = solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
print(my)
print('correct') if answer == my else print('wrong')

