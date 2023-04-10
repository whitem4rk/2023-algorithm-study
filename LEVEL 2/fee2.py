# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 주차 요금 계산
# 실패 - 오래걸림, 인덱스 관리

from collections import defaultdict
import math

def timeToInt(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def solution(fees, records):
    basic_time, basic_fee = fees[0], fees[1]
    per_time, per_fee = fees[2], fees[3]
    cardict = defaultdict()
    for record in records:
        time, car, state = record.split()
        time = timeToInt(time)
        
        if car not in cardict:
            cardict[car] = [0, 0]
            
        if state == "IN":
            cardict[car][0] = time
        elif state == "OUT":
            cardict[car][1] += time - cardict[car][0]
            cardict[car][0] = -1
    feelist = [] 
    for car, v in cardict.items():
        print(cardict)
        print(feelist)
        if v[0] != -1:
            cardict[car][1] += (60*24-1) - v[0]
        feelist.append((car, basic_fee + math.ceil(max((cardict[car][1]-basic_time), 0)/per_time)* per_fee))
    feelist.sort()
    return [fee for car, fee in feelist]
