# 코딩테스트 연습 / 연습문제 / 최댓값과 최솟값
# 성공

def solution(s):
    a = list(map(int, s.split()))
    return "" + str(min(a)) +" "+ str(max(a))