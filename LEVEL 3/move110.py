def solution(slist):
    answer = []
    for s in slist:
        stack, num110 = [], 0
        for i in range(len(s)):
            if s[i] == '0':
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop()
                    num110 += 1
                else:
                    stack.append(s[i])
            
            else:
                stack.append(s[i])
    
        stack = ''.join(stack[::-1])
        idx = stack.find('0')

        if idx != -1:
            res = stack[:idx] + '011' * num110 + stack[idx:]
        else:
            res = stack + '011' * num110
        answer.append(''.join(res[::-1]))
    
    return answer
    