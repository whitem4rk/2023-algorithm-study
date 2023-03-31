# 코딩테스트 연습 / 연습문제 / JadenCase 문자열 만들기
# 성공 / title()이 생각이 안나서 직접 구현

def solution(s):
    answer = ''    
    answer += s[0].upper()
    check = False
    for i in range(1,len(s)):
        if s[i] == ' ':
            check = True
            answer += ' '
        elif check:
            answer += s[i].upper()
            check = False
        elif not check:
            answer += s[i].lower()
    return answer