# 코딩테스트 연습 / 해시 / 완주하지 못한 선수
# 실패 - most_common 까먹음

from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    
    for com in completion:
        participant[com] -= 1
    return participant.most_common(1)[0][0]

