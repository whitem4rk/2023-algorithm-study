# 코딩테스트 연습 / 연습문제 / 2016년
# 성공

def solution(a, b):
    m = [31,29,31,30,31,30,31,31,30,31,30,31]
    d = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    day = sum(m[:a-1]) + b
    
    return d[day % 7]