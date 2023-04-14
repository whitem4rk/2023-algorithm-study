# 코딩테스트 연습 / 동적계획법(Dynamic Programming) / N으로 표현
# 실패 - 구현을 못함

def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1,9):
        allcase = set()
        origin = int(str(N)*i)
        allcase.add(origin)
        
        for j in range(i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    allcase.add(op1-op2)
                    allcase.add(op1+op2)
                    allcase.add(op1*op2)
                    if op2 != 0:
                        allcase.add(op1 // op2)
        if number in allcase:
            answer = i
            break
    
        dp.append(allcase)
        
    return answer
