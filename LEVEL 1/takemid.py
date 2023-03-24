# 코딩테스트 연습 / 연습문제 / 가운데 글자 가져오기
# 성공

def solution(s):
    half = len(s) // 2
    if len(s) % 2 == 1:
        return s[half]
    else:
        return s[half-1:half+1]