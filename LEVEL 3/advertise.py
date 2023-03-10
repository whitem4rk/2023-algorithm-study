# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 광고 삽입

# "01:00:00" -> 3600
def time_to_sec(time:str) -> int:
    h,m,s = map(int, time.split(':'))
    return (h * 60 * 60) + (m * 60) + (s)

# 3600 -> "01:00:00"
def sec_to_time(sec:int) -> str:
    h = sec
    h ,s = divmod(h,60)
    h ,m = divmod(h,60)
    
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    s = str(s).zfill(2)
    return h+':'+m+':'+s
    
def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time) 
    adv_time = time_to_sec(adv_time)
    timetable = ([0] * play_time) + [0]
    
    # 누적합을 이용해서 각 초마다 시청 횟수를 저장
    for log in logs:
        start, end = log.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        timetable[start] += 1
        timetable[end] -= 1
    
    for i in range(1, len(timetable)):
        timetable[i] += timetable[i-1]
    
    # adv_time 시간동안의 합들을 배열을 순회하면서 저장하고 최대인값과 인덱스를 찾음    
    cur = sum(timetable[:adv_time])
    sumstack = [cur]
    for i in range(adv_time, play_time):
        cur += timetable[i]
        cur -= timetable[i-adv_time]
        sumstack.append(cur)
    
    answer = sumstack.index(max(sumstack))    
    return sec_to_time(answer)


answer = "01:30:59"
my = solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
print(my)
print('correct') if answer == my else print('wrong')

