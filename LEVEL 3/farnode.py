# 코딩테스트 연습 / 그래프 / 가장 먼 노드
# 실패 - Counter 정렬   

from collections import deque, Counter

def solution(n, edge):
    edgelist = [[] for _ in range(n+1)]
    for v in edge:
        edgelist[v[0]].append(v[1])
        edgelist[v[1]].append(v[0])
        
    q = deque([(1,0)])
    visited = [False] * (n+1)
    dist = [0] * (n+1)
    
    while q:
        node, cnt = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        dist[node] = cnt
        
        for num in edgelist[node]:
            q.append((num, cnt+1))
    answer = list(sorted(Counter(dist).items(), reverse=True))[0][1]

    return answer