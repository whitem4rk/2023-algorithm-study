# 코딩테스트 연습 / 연습문제 / 하샤드 수
# 성공

def solution(x:int) -> bool:
    d = sum(map(int, str(x)))
    if x % d == 0:
        return True
    return False