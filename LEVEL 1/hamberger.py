# 코딩테스트 연습 / 연습문제 / 햄버거 만들기

# 시간초과 / 문자열로 변경후 1231을 계속 지우려고 했으나 O(n^2)으로 안되는듯?
# def solution(ingredient):
#     answer = 0
#     tostring = list(map(str, ingredient))
#     tostring = ''.join(tostring)
    
#     while tostring.find('1231') != -1:
#         tostring = tostring.replace('1231','',1)
#         answer += 1
#     return answer

def solution(ingredient):
    answer = 0
    
    basket = []
    for obj in ingredient:
        basket.append(obj)
        # basket의 길이 꼭 확인
        if len(basket) >= 4:
        # 상위 4개가 1231인지 확인
            if basket[-4] == 1 and basket[-3] == 2 and basket[-2] == 3 and basket[-1] == 1:
                basket.pop()
                basket.pop()
                basket.pop()
                basket.pop()
                answer += 1
    
    return answer

# test case / answer = 2
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))