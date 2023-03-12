# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    answer = float('inf')
    candidates = list(permutations(dist, len(dist)))
    weak = weak + [ w+n for w in weak ]

    # weak를 순회하면서 weak[next]-weak[cur] > 현재 친구 이면 cur=next, cnt += 1
    for start in range(len(weak)//2):
        for cand in candidates:
            cnt = 1
            curidx = start
            for i in range(1, len(weak)//2):
                nextidx = start + i
                if weak[nextidx] - weak[curidx] > cand[cnt-1]:
                    cnt += 1
                    curidx = nextidx
                    if cnt > len(dist):
                        break
            
            if cnt <= len(dist):
                answer = min(answer,cnt)
    if answer == float('inf'):
        return -1
    return answer



answer = 2
my = solution(12,[1, 5, 6, 10],[1, 2, 3, 4])
print(my)
print('correct') if answer == my else print('wrong')

