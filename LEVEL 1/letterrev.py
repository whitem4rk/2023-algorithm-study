# 코딩테스트 연습 / 연습문제 / 문자열 내림차순으로 배치하기
# 실패 - sorted의 반환타입은 list

def solution(s):
    return ''.join(sorted(s, reverse=True))