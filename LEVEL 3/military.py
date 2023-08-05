from collections import deque

def bfs(graph, destination):
    visited = set()
    dist = [-1 for _ in range(len(graph))]
    
    q = deque()
    q.append((destination, 0))
    
    while q:
        cur, curdist = q.popleft()
        if cur in visited:
            continue
        
        visited.add(cur)
        dist[cur] = curdist
        
        for node in graph[cur]:
            q.append((node, curdist+1))
    
    return dist

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = bfs(graph, destination)
    
    answer = []
    for s in sources:
        answer.append(dist[s])
    
    return answer
