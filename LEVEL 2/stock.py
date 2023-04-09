# 코딩테스트 연습 / 스택/큐 / 주식가격
# 실패 - 문제풀이를 실패했음 while이 필요했었음

def solution(prices):
    answer = [0] * len(prices)
    stack = [(0, prices[0])]
    
    for i in range(1, len(prices)):
        while stack and prices[i] < stack[-1][1]:
            cur_idx, cur_price = stack.pop()
            answer[cur_idx] = i - cur_idx
        stack.append((i, prices[i]))

    while stack:
        cur_idx, cur_price = stack.pop()
        answer[cur_idx] = len(prices) - cur_idx - 1
    
    return answer