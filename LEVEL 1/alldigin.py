# 코딩테스트 연습 / 연습문제 / 문자열 다루기 기본
# 실패 - and, or 정확히


def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for c in s:
        if not c.isdigit():
            return False
    
    return True