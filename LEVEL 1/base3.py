# 코딩테스트 연습 / 월간 코드 챌린지 시즌1 / 3진법 뒤집기
# 실패 - int n진법 형변환

def solution(n):
    answer = ''
    while True:
        result, remain = divmod(n, 3)
        answer += str(remain)
        if result == 0:
            break
        n = result
    return int(answer,3)