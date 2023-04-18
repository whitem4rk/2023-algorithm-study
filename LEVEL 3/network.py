# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 네트워크
# 실패

from collections import deque

def solution(n, computers):
    answer = 0
    visited = set()
    
    for i in range(n):
        q = deque([])
        if i not in visited:
            q.append(i)
            answer += 1
        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            for idx,com in enumerate(computers[cur]):
                if com == 1:
                    q.append(idx)
        
    
    return answer