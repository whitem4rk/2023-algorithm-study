# 코딩테스트 연습 / 월간 코드 챌린지 시즌3 / 없는 숫자 더하기
# 성공

def solution(numbers):
    answer = 45
    for num in numbers:
        answer -= num
    return answer