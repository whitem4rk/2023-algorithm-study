# 코딩테스트 연습 / 연습문제 / 자연수 뒤집어 배열로 만들기
# 실패 - 형변환 빠뜨림

def solution(n):
    return [ int(x) for x in str(n)[::-1] ]