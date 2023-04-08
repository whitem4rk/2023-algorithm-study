# 코딩테스트 연습 / 완전탐색 / 피로도
# 실패 - 반복문 로직 오류

from itertools import permutations

def solution(k, dungeons):
    permute = permutations(range(len(dungeons)))
    answer = []
    for per in permute:
        cnt = 0
        cur = k
        for p in per:
            min_need, minus = dungeons[p][0], dungeons[p][1]
            if cur >= min_need:
                cur -= minus
                cnt += 1
            else:
                cur = 0
        answer.append(cnt)
    return max(answer)