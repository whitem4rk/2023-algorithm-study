# 코딩테스트 연습 / 스택/큐 / 올바른 괄호
# 성공

def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            if c == ')':
                return False
            stack.append('(')
        elif c == '(':
            stack.append('(')
        elif c == ')':
            stack.pop()
        
    if len(stack) == 0:
        return True
    else:
        return False
