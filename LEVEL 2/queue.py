# 코딩테스트 연습 / 2022 KAKAO TECH INTERNSHIP / 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    d1, d2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(d1), sum(d2)
    
    # 모든 경우의 수는 두 큐의 길이의 합의 2배를 넘지 않는다.
    # 그리디
    for i in range(2 * (len(d1)+len(d2))):
        if sum1 == sum2:
            return i
        elif sum1 > sum2:
            tmp = d1.popleft()
            d2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        elif sum1 < sum2:
            tmp = d2.popleft()
            d1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            
    return -1

# test case / answer = 2
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))