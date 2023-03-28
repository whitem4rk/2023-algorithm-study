# 코딩테스트 연습 / 연습문제 / 과일 장수
# 실패 - 인덱스...


def solution(k, m, score):
    score.sort(reverse=True)
    
    cnt = 0
    for j in range(m, len(score)+1, m):
        cnt += min(score[j-m:j]) * m
    
    return cnt