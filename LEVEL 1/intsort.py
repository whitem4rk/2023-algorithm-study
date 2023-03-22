# 코딩테스트 연습 / 연습문제 / 정수 내림차순으로 배치하기
# 실패 - 형변환 자꾸 빠뜨리네...

def solution(n):
    rev_arr = sorted(str(n), reverse=True)
    return int(''.join(rev_arr))