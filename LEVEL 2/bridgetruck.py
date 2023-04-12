# 코딩테스트 연습 / 스택/큐 / 다리를 지나는 트럭

from collections import deque

def solution(bl, weight, tw):
    tw = deque(tw)
    bridge = [0] * bl
    bridge = deque(bridge, maxlen = bl)
    cur_sum = 0
    time = 0
    while tw:
        time += 1
        cur_sum -= bridge.popleft()
        if tw[0] + cur_sum > weight:
            bridge.append(0)
        else:
            cur_sum += tw[0]
            bridge.append(tw.popleft())
            
    return time + bl