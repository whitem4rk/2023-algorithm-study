# 코딩테스트 연습 / 연습문제 / 멀리 뛰기
# 실패 = 조건 빠뜨림

def solution(n):
    road = [0] * 2002
    road[0] = 1
    road[1] = 1
    
    for i in range(2, n+1):
        road[i] = (road[i-1] + road[i-2]) % 1234567
    return road[n]
