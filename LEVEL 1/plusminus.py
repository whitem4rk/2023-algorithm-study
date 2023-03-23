# 코딩테스트 연습 / 월간 코드 챌린지 시즌2 / 음양 더하기
# 실패 - zip() 빠뜨림

def solution(absolutes, signs):
    answer = 0
    for num, op in zip(absolutes, signs):
        answer = answer + num if op else answer - num
    return answer

