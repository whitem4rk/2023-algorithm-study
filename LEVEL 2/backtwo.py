# 코딩테스트 연습 / 연습문제 / 뒤에 있는 큰 수 찾기
# 실패

def solution(numbers):
    answer = [-1] * len(numbers)
    minstack = []
    for idx,num in enumerate(numbers):
        while minstack and minstack[-1][1] < num:
            answer[minstack.pop()[0]] = num
        minstack.append((idx,num))
    return answer