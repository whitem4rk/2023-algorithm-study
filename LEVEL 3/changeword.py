# 코딩테스트 연습 / 깊이/너비 우선 탐색(DFS/BFS) / 단어 변환
# 실패 

from collections import deque

def cntdiff(w1, w2):
    cnt = 0
    for a, b in zip(w1,w2):
        if a != b:
            cnt += 1
    return cnt

def solution(begin, target, words):
    answer = 0
    
    q = deque([[begin,0]])
    visited = set()
    
    while q:
        cur,cnt = q.popleft()
        if cur == target:
            return cnt
        if cur in visited:
            continue
        
        visited.add(cur)
        for word in words:
            if cntdiff(cur, word) == 1:
                q.append([word, cnt+1])
        
    return 0