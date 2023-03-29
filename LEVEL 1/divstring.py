# 코딩테스트 연습 / 연습문제 / 문자열 나누기
# 조건 빠뜨림

def solution(s):
    answer = 0
    x, notx = 0, 0
    first = ''
    for c in s:
        if x == 0 and notx == 0:
            first = c
            x += 1
        else:
            if first == c:
                x += 1
            else:
                notx += 1
            
            if x == notx:
                x, notx, fist = 0, 0, ''
                answer += 1
    if x != 0:
        answer += 1
    return answer