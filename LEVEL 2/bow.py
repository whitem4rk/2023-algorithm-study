# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 양궁대회

from itertools import combinations_with_replacement

def solution(n, info):
    # 이길 수 없다면 -1
    answer = [-1]
    maxGap = -1
    
    # 중복조합 경우의 수
    candidates = list(combinations_with_replacement(range(0, 11), n))
    
    for candidate in candidates:
        info2 = [0] * 11
        apeach, lion = 0, 0
        
        for score in candidate:
            info2[10 - score] += 1
        # 점수 합산
        for score, (a, l) in enumerate(zip(info, info2)):
            if a == l == 0:
                continue
            elif a >= l:
                apeach += (10 - score)
            else:
                lion += (10 - score)
        # 라이언이 이기는 경우
        if lion > apeach:
            # 점수차가 현재 최고 점수차보다 클 때 갱신
            gap = lion - apeach
            if gap > maxGap:
                maxGap = gap
                answer = info2
    return answer

# test case / answer = [0,2,2,0,1,0,0,0,0,0,0]
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))