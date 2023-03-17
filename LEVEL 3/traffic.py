# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 추석 트래픽

def time_to_sec(time:str) -> int:
    h,m,s = map(float, time.split(':'))
    total = h * 60000 * 60
    total += m * 60000
    total += s*1000
    return total

def solution(lines:list) -> int:
    answer = 0
    table = []
    for line in lines:
        t1,t2,t3 = line.split()
        t2 = time_to_sec(t2)
        t3 = float(t3[:-1]) * 1000
        table.append((t2-t3+1, t2))
    print(table)
    for i in range(len(table)):
        end = table[i][1]
        cnt = 0
        for j in range(i, len(table)):
            start2 = table[j][0]
            if start2 < end + 1000:
                cnt += 1
        answer = max(answer,cnt)
    
    return answer


answer = 1
my = solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
print(my)
print('correct') if answer == my else print('wrong')