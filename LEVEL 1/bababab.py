# 코딩테스트 연습 / 연습문제 / 옹알이 (2)
# 실패 - 도저히 모르겠음... 로직은 맞는데 답은 자꾸 틀림 뭐지?

def solution(babbling):
    answer = 0
    can = ['aya','ye','woo','ma']
    cant = ['ayaaya', 'yeye', 'woowoo','mama']
    can_bab = set(babbling)
        
    for bab in babbling:
        for c in cant:
            if c in bab:
                can_bab.discard(bab)
    
    for bab in can_bab:
        tmp = bab
        for c in can:
            tmp = tmp.replace(c,' '*len(c))
        if tmp == ' '*len(bab):
            answer += 1 
            
    return answer


solution(["woayao"])