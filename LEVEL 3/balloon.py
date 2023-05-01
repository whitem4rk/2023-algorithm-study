# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 풍선 터트리기
# 실패 - 성장이 멈춘 느낌.. 흠..

def solution(a):
    answer = 0
    leftmin = [0] * len(a)
    rightmin = [0] * len(a)
    
    curmin = 1000000000
    for i in range(1, len(a)):
        if a[i-1] < curmin:
            curmin = a[i-1]
        leftmin[i] = curmin
    
    curmin = 1000000000
    for i in reversed(range(len(a)-1)):
        if a[i+1] < curmin:
            curmin = a[i+1]
        rightmin[i] = curmin
    for i in range(1,len(a)-1):
        if a[i] < rightmin[i] or a[i] < leftmin[i]:
            answer += 1
        
    return answer + 2


