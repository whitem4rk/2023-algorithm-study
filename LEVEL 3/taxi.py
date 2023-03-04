# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 합승 택시 요금
# 플로이드 와샬로도 풀이 가능
import heapq

def dijkstra(x:int, v1:int, v2:int, s:int, fares:list) -> int:
    dist_list = [float('inf')] * len(fares)
    dist_list[x] = 0
    visited = [False] * len(fares)
    q = []
    heapq.heappush(q, (0,x))
    
    while q:
        cur_d, cur = heapq.heappop(q)
        visited[cur] = True
        if cur_d > dist_list[cur]:
            continue
        
        for fare in fares[cur]:
            v, dist = fare
            if not visited[v]:
                if cur_d + dist < dist_list[v]:
                    heapq.heappush(q, (cur_d + dist,v))
                    dist_list[v] = cur_d + dist
    return dist_list[v1] + dist_list[v2] + dist_list[s]        
                
            
def solution(n, s, a, b, fares):
    distance = [[] for _ in range(n+1)]
    
    for fare in fares:
        v1, v2, f = fare
        distance[v1].append((v2, f))
        distance[v2].append((v1, f))

    dist_list = []
    # 임의의 한곳에서부터 a,b,s 까지의 거리들의 합이 최소인것을 찾음
    for x in range(1,n+1):
        dist_list.append(dijkstra(x,a,b,s,distance))
    answer = min(dist_list)
    
    return answer


answer = 82
my = solution(6,4,6,2,[[4,1,10],[3,5,24],[5,6,2],[3,1,41],[5,1,24],[4,6,50],[2,4,66],[2,3,22],[1,6,25]])
print(my)
print('correct') if answer == my else print('wrong')