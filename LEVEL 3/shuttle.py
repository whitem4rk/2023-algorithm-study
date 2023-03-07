# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 셔틀버스

from collections import deque

def time_to_min(t):
    h, m = map(int ,t.split(':'))
    return 60*h + m

def min_to_time(m):
    h, m = divmod(m, 60)
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    return h+':'+m

def solution(n, t, m, timetable):
    answer = 0
    
    # 분으로 바꾸고 정렬
    new_table = []
    for time in timetable:
        new_table.append(time_to_min(time))
    new_table.sort()
    new_table = deque(new_table)    
    
    # 해당시간에 맞게 크루들 배치
    shuttle = [[] for _ in range(n)]
    for i in range(len(shuttle)):
        until = 540 + (i*t)
        while new_table:
            if new_table[0] > until or len(shuttle[i]) == m: break
            shuttle[i].append(new_table[0])
            new_table.popleft()
            
    # 막차에 좌석이 없는경우 마지막 크루시간 -1
    if len(shuttle[-1]) == m:
        answer = shuttle[i][-1] - 1
    # 좌석이 있는경우 막차시간 -1
    else:
        answer = 540 + t * (n-1)
    return min_to_time(answer)



answer = "09:09"
my = solution(2,10,2,["09:10", "09:09", "08:00"])
print(my)
print('correct') if answer == my else print('wrong')