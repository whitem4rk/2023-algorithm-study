# 코딩테스트 연습 / 2019 KAKAO BLIND RECRUITMENT / 실패율
# 실패 - out of range... 범위 할당 항상 신중하자


def solution(N:int, stages:list) -> list:
    stage_sum = [0] * (N+3)
    stage_fail = [0] * (N+3)
    
    for s in stages:
        stage_sum[1] += 1
        stage_sum[s+1] -= 1
        stage_fail[s] += 1
    
    for i in range(1,len(stage_sum)):
        stage_sum[i] += stage_sum[i-1]
    
    rate_list = []
    for i in range(1, len(stage_sum)-2):
        if stage_sum[i] == 0:
            r = 0
        else:
            r = stage_fail[i]/stage_sum[i]
        rate_list.append((r,i))
    rate_list.sort(key=lambda x:(-x[0],x[1]))
    answer = []
    for rate in rate_list:
        answer.append(rate[1])
        
    return answer