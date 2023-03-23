# 코딩테스트 연습 / 연습문제 / 자릿수 더하기
# 실패 - 형변환 빠뜨림

def solution(n):
    
    k = 0
    for num in str(n):
        k += int(num)
    
    return k