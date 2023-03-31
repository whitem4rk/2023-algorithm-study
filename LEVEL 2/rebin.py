# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 이진 변환 반복하기
# 성공

def solution(s):
    del0 = 0
    delcnt = 0
    while s != '1':
        del0 += s.count('0')
        s = s.replace('0', '')
        tmplen = len(s)
        s = bin(tmplen)[2:]
        delcnt += 1
    return [delcnt, del0]