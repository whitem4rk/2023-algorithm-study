# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 택배 배달과 수거하기

# 시간초과 O(n^2)
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     storage = [0,0]
#     end = n
    
#     while end != -1:
#         if deliveries[end-1] + pickups[end-1] == 0:
#             end -= 1
#             continue
#         sum_down = 0
#         sum_up = 0
        
#         for i in reversed(range(end)):
#             down = deliveries[i]
#             if sum_down + down > cap:
#                 down = down - (sum_down+down - cap)
#             sum_down += down
#             deliveries[i] -= down
        
#         for i in reversed(range(end)):
#             up = pickups[i]
#             if sum_up + up > cap:
#                 up = up - (sum_up + up - cap)
#             sum_up += up
#             pickups[i] -= up
#         answer += end*2
#     return answer

def solution(cap, n, deliveries, pickups):
    answer = 0

    up_sum = 0
    down_sum = 0
    
    # 한번 갔다올때마다 최대 cap개의 배달, 수거가 가능
    # 마지막 집부터 (배달, 수거) 통틀어 최소 몇번 방문해야하는지 계산하고 초과된 값은 - 로 저장해놓음
    # 39번쨰 줄 이유 => n번째 집에 배달을 1번, 수거를 0번 왕복해야한다면 배달을 1번 수행할동안 n보다 작은 집에 수거를 미리 시행할수 있기 때문
    for i in reversed(range(n)):
        up_sum += deliveries[i]
        down_sum += pickups[i]
        
        while up_sum > 0 or down_sum > 0:
            up_sum -= cap
            down_sum -= cap
            answer += (i+1) * 2
        
    return answer


# test case / answer = 16
print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))