# 코딩테스트 연습 / 완전탐색 / 카펫
# 성공

def solution(brown, yellow):
    
    for height in range(1, int(yellow**(1/2))+1):
        width, remain = divmod(yellow, height)
        
        if remain == 0:
            width += 2
            height += 2
            if ((width + height) * 2 - 4) == brown:
                return [width, height]
        