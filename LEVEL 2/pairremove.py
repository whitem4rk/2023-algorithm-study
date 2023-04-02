# 코딩테스트 연습 / 2017 팁스타운 / 짝지어 제거하기
# 실패 - 너무 오래걸림

def solution(s):
    stack = []
    
    for c in s:
        if len(stack) == 0:
            stack.append(c)
            continue        
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return 1 if len(stack) == 0 else 0
        