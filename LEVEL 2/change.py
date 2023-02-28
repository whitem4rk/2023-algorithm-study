# 코딩테스트 연습 / 2020 KAKAO BLIND RECRUITMENT / 괄호 변환

# 올바른 괄호 확인
def correct(s:str):
    stack = []
    for letter in s:
        if letter == '(':
            stack.append(letter)
        else:
            if len(stack) <= 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
    
    return True if len(stack) == 0 else False

# 균형있는 괄호 확인
def balance(s:str):
    left, right = 0, 0
    for letter in s:
        if letter == '(':
            left += 1
        elif letter == ')':
            right += 1
    return True if right == left else False       
        
        
def solution(p):
    if correct(p):
        return p
    else:
        for i in range(1,len(p)+1):
            # 균형있다면 u,v로 나눔
            if balance(p[:i]):
                u, v = p[:i], p[i:]
                break
        # u가 올바르다면 v만 처리
        if correct(u):
            return u + solution(v)
        # 올바르지 않다면 다르게 수행
        else:
            s = '(' + solution(v) + ')'
            u = u[1:-1]
            
            for letter in u:
                if letter == '(':
                    s += ')'
                else:  
                    s += '('
            return s

# test case 
answer = "()(())()"
my_answer = solution("()))((()")
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

