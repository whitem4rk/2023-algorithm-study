# 코딩테스트 연습 / 연습문제 / 소수 찾기
# 성공

def solution(n):
    answer = []
    nlist = [True] * (n+1)
    for i in range(2,n+1):
        if nlist[i]:
            answer.append(i)
        for j in range(i,n+1,i):
            nlist[j] = False
        
    return len(answer)