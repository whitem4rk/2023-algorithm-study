# 코딩테스트 연습 / 정렬 / H-Index
# 실패 - 문제 잘못 이해

def solution(citations):
    citations.sort(reverse=True)
    for idx, cit in enumerate(citations):
        if cit <= idx:
            return idx
    return len(citations)

