# 코딩테스트 연습 / 탐욕법(Greedy) / 큰 수 만들기
# 실패 - 조합(시간초과), heap(시간초과)


def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer) - k])