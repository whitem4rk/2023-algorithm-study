# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 괄호 회전하기
# 실패 - 예외처리

from collections import deque

def check(s):
    stack = []
    for c in s:
        if c == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif c == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else: 
                return False
        else:
            stack.append(c)
    
    return True if len(stack) == 0 else False
            

def solution(s):
    s = deque(s)
    cnt = 0
    for i in range(len(s)):
        if check(s):
            cnt += 1
        
        tmp = s.popleft()
        s.append(tmp)
        
    return cnt