# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 이모티콘 할인행사

from itertools import product

def solution(users, emoticons):
    answer = []
    # 세일율 중복순열
    candidates = list(product([10,20,30,40],repeat=len(emoticons)))
    memory = []
    
    for candidate in candidates:
        sum = 0
        membership = 0
        
        for sale_limit, price_limit in users:
            user_sum = 0
            for idx, emo_price in enumerate(emoticons):
                # user의 세일율보다 크거나 같다면 구매
                if candidate[idx] >= sale_limit:
                    user_sum += int(emo_price * (100-candidate[idx]) / 100)
            
            # user의 총 구매액이 한계 금액보다 크다면 멤버쉽가입 & 구매취소
            if user_sum >= price_limit:
                user_sum = 0
                membership += 1
                
            sum += user_sum
            
        # 기록
        memory.append([membership,sum])
    
    # 1번째 2번째 원소 내림차순
    memory.sort(key=lambda x: [-x[0], -x[1]])
    answer = memory[0]
        
    return answer


# test case / answer = [1, 5400]
print(solution([[40, 10000], [25, 10000]],[7000, 9000]))