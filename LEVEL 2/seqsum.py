# 코딩테스트 연습 / 연습문제 / 연속 부분 수열 합의 개수
# 실패

def solution(elements):
    sumset = set()
    elen = len(elements)
    elements *= 2
    for i in range(1, elen+1):
        for j in range(elen):
            sumset.add(sum(elements[j:(j+i)]))
    return len(sumset)