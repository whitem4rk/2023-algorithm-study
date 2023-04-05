# 코딩테스트 연습 / 해시 / 위장
# 실패 

def solution(clothes):
    category = {}    
    for cloth in clothes:
        if cloth[1] in category:
            category[cloth[1]] += 1
        else:
            category[cloth[1]] = 1

    answer = 1
    for cnt in category.values():
        answer *= (cnt+1)
        
    return answer - 1