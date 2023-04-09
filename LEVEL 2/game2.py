# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] n진수 게임
# 실패 - 반복문 인덱스 관리

numdict = {i:hex(i)[2:].upper() for i in range(16)}

def tenToN(i, n):
    tmp = []
    while True:
        div, mod = divmod(i, n)
        tmp.append(numdict[mod])
        if div == 0:
            break   
        i = div
    return tmp[::-1]

def solution(n, t, m, p):
    numlist = []
    for i in range(m*t):
        numlist += tenToN(i, n)
    plist = [numlist[i] for i in range(p-1, m*t, m)]
    return ''.join(plist)