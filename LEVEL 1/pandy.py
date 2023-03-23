# 코딩테스트 연습 / 연습문제 / 문자열 내 p와 y의 개수
# 성공

def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    for c in s.lower():
        if c == 'p':
            p_cnt += 1
        elif c == 'y':
            y_cnt += 1

    if p_cnt == y_cnt:
        return True
    else:
        return False 