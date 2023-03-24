# 코딩테스트 연습 / 연습문제 / 시저 암호
# 실패 - ascii_lowercase 까먹음

from string import ascii_lowercase, ascii_uppercase

def solution(s, n):
    answer = ''
    l = ascii_lowercase
    u = ascii_uppercase
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
        else:
            if s[i].islower():
                idx = l.index(s[i])
                answer += l[(idx+n) % 26]
            else:
                idx = u.index(s[i])
                answer += u[(idx+n) % 26]
    return answer

solution("ab",1)