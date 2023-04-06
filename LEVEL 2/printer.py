# 코딩테스트 연습 / 스택/큐 / 프린터
# 실패

def solution(priorities, location):
    answer = []
    remain = {}
    for p in priorities:
        if p in remain:
            remain[p] += 1
        else:
            remain[p] = 1
    
    cnt = 0
    idx = 0
    m = max(priorities)
    while cnt != len(priorities):
        p = priorities[idx % len(priorities)]
        if p == m:
            cnt += 1
            remain[p] -= 1
            answer.append(idx % len(priorities))
            if remain[p] == 0:
                del remain[p]
                if len(remain) == 0:
                    break
                m = max(remain)
        
        idx += 1 
    return answer.index(location) + 1