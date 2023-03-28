# 코딩테스트 연습 / 연습문제 / 숫자 짝꿍
# 실패 - 시간초과 int() 가 자리수의 제곱의 시간이 걸린다고한다. 전혀 몰랐던 꿀팁

from collections import Counter

def solution(X, Y):
    answer = ''
    x, y = Counter(X), Counter(Y)
    aset, bset = set(X), set(Y)
    for com in (aset & bset):
        answer += com * min(x[com], y[com])
    
    if answer == '':
        return "-1"
    
    answer = sorted(answer, reverse=True)
    if answer[0] == '0':
        return '0'
    return ''.join(answer)