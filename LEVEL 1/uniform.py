# 코딩테스트 연습 / 탐욕법(Greedy) / 체육복
# 실패 - 문제 조건 빠뜨림


from collections import Counter

def solution(n, lost, reserve):
    student = [1] * (n+2)
    for re in reserve:
        student[re] += 1
    for l in lost:
        student[l] -= 1
    reserve.sort()
    
    for re in range(1,n+1):
        if student[re] == 2:
            if student[re-1] == 0:
                student[re-1] += 1
            elif student[re+1] == 0:
                student[re+1] += 1
    
    c = Counter(student)
    return c[1]+c[2]-2

solution(5	,[2, 4],	[1, 3, 5])