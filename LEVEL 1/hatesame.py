# 코딩테스트 연습 / 스택/큐 / 같은 숫자는 싫어
# 성공

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or answer[-1] != a:
            answer.append(a)
    return answer