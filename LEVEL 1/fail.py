# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 실패율

def solution(N, stages):
    answer = []
    
    rate_list = []
    remain = len(stages)
    # 1 ~ N 단계 계산
    for i in range(1, N+1):
        # stage 돌면서 실패율 계산
        if remain != 0:
            fail = stages.count(i)
            rate  = fail / remain
            remain -= fail
            rate_list.append((i, rate))
        # 남은것이 없어도 모든 스테이지에 0 대입
        else:
            rate_list.append((i, 0))
    
    # 정렬
    rate_list.sort(key=lambda x: x[1], reverse=True)
    answer = [ obj[0] for obj in rate_list]
    return answer

# test case / answer = [3,4,2,1,5]
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))