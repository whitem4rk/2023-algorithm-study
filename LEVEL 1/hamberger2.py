# 코딩테스트 연습 / 연습문제 / 햄버거 만들기
# 실패

def solution(ingredient):
    answer = 0
    
    basket = []
    for obj in ingredient:
        basket.append(obj)
        if len(basket) >= 4:
            if basket[-4] == 1 and basket[-3] == 2 and basket[-2] == 3 and basket[-1] == 1:
                basket.pop()
                basket.pop()
                basket.pop()
                basket.pop()
                answer += 1
    
    return answer