# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 주차 요금 계산

import math

def solution(fees, records):
    answer = []
    basic_time, basic_fee = fees[0], fees[1]
    per_time, per_fee = fees[2], fees[3]
    
    # park 기록 / key = 차번호: value = 시간
    park_dict = {}
    hsum_dict = {}
    for rec in records:
        time, num, state = rec.split(' ')
        # OUT
        if num in park_dict:
            # 시간을 분으로 환산한 값의 차이를 넣는다
            cur_h, cur_m = int(time[0:2]), int(time[-2:])
            in_h, in_m = int(park_dict[num][0:2]), int(park_dict[num][-2:])
            cur_m += cur_h * 60
            in_m += in_h * 60
            hsum_dict[num] += cur_m - in_m
            del park_dict[num]
        # IN
        else:
            park_dict[num] = time
            if num not in hsum_dict:
                hsum_dict[num] = 0

    # OUT처리 안된것들 처리
    for num, time in park_dict.items():
        cur_h, cur_m = 23, 59
        in_h, in_m = int(park_dict[num][0:2]), int(park_dict[num][-2:])
        cur_m += cur_h * 60
        in_m += in_h * 60
        hsum_dict[num] += cur_m - in_m
    
    # 요금정산
    hsum_dict = dict(sorted(hsum_dict.items()))
    for num, sum in hsum_dict.items():
        total = basic_fee
        if sum > basic_time:
            total = basic_fee + math.ceil((sum-basic_time)/per_time) * per_fee
        answer.append(total)
    
    return answer

# test case / answer = [14600, 34400, 5000]
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))