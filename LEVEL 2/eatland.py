# 코딩테스트 연습 / 연습문제 / 땅따먹기
# 실패 - copy()

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            tmp = land[i-1].copy()
            tmp.pop(j)
            land[i][j] += max(tmp)
    return max(land[-1])