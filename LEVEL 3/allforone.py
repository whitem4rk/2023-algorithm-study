# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 모두 0으로 만들기
# 실패 - 어렵다

import sys
sys.setrecursionlimit(10 ** 6)

def solution(a, edges):
    if sum(a) != 0:
        return -1
        
    n = len(a)
    graph = [[] for _ in range(n)]
    for node_a, node_b in edges:
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    result = 0
        
    def dfs(child, parent):
        nonlocal a, graph, result
        for c in graph[child]:
            if c != parent:
                dfs(c, child)
        a[parent] += a[child]
        result += abs(a[child])
        
    dfs(0, 0)
    return result