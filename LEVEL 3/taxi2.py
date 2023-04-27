from heapq import heappush, heappop

def dijkstra(start,end,table):
    dist_list = [float('inf')] * len(table)
    dist_list[start] = 0
    q = [(0, start)]
    
    while q:
        cur_dist, cur_node = heappop(q)
        if cur_dist > dist_list[cur_node]:
            continue
            
        for ta in table[cur_node]:
            next_node, edge_dist = ta
            next_dist = cur_dist + edge_dist
            if next_dist < dist_list[next_node]:
                dist_list[next_node] = next_dist
                heappush(q, (next_dist, next_node))
    return dist_list[end]

def solution(n, s, a, b, fares):
    table = [[] for _ in range(n+1)]
    for fare in fares:
        fr, to, dist = fare
        table[fr].append((to,dist))
        table[to].append((fr,dist))
    
    answer_list = []
    for letwalk in range(1,n+1):
        result = dijkstra(s,letwalk,table) + dijkstra(letwalk,a,table) + dijkstra(letwalk,b,table)
        answer_list.append(result)
        
    return min(answer_list)
        

solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])