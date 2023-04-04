# 코딩테스트 연습 / 연습문제 / 귤 고르기
# 성공

from collections import Counter

def solution(k, tangerine):
    answer = 0
    total = 0
    l = Counter(tangerine)
    l = list(l.values())
    l.sort(reverse=True)
    for cnt in l:
        total += cnt
        answer += 1
        if total >= k:
            break
    return answer