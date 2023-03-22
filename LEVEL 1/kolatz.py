# 코딩테스트 연습 / 연습문제 / 콜라츠 추측
# 성공

def solution(num):
    for i in range(501):
        if num == 1:
            return i
        elif num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    
    return -1
        