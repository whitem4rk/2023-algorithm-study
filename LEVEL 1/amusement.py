# 코딩테스트 연습 / 위클리 챌린지 / 부족한 금액 계산하기
# 성공

def solution(price, money, count):
    price_list = [price*(i+1) for i in range(count)]    
    return 0 if sum(price_list) <= money else sum(price_list) - money