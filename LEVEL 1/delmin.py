# 코딩테스트 연습 / 연습문제 / 제일 작은 수 제거하기
# 성공

def solution(arr):
    mini = min(arr)
    arr.remove(mini)
    return arr if len(arr) != 0 else [-1]