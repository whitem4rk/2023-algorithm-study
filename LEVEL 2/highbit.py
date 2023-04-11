# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 2개 이하로 다른 비트
# 실패 

def getmin(binstr):
    allone = True
    binstr = binstr[::-1]
    for idx,c in enumerate(binstr):
        if c == '0':
            curidx= idx
            allone = False
            break
    
    if allone:
        binstr = binstr[:-1]+'01'
    else:
        if curidx > 0:
            binstr = binstr.replace('10','01',1)
        else:
            binstr = binstr.replace('0','1',1)
    
    return binstr[::-1]
    
def solution(numbers):
    answer = []
    for num in numbers:
        binstr = str(bin(num))[2:]
        answer.append(int(getmin(binstr),2))
    return answer