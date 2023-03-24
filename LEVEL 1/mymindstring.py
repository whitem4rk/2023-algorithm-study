# 코딩테스트 연습 / 연습문제 / 문자열 내 마음대로 정렬하기
# 성공

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n],x))