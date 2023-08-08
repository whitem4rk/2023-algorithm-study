from collections import Counter

def solution(a):
    count = Counter(a)
    max_answer = 0
    for letter, freq in count.most_common():
        if freq <= max_answer:
            break
        answer = 0
        flag = 0
        for aletter in a:
            if aletter != letter:
                if flag > 0:
                    answer += 1
                    flag = 0
                else:
                    flag -= 1
            else:
                if flag < 0:
                    answer += 1
                    flag = 0
                else:
                    flag += 1
        max_answer = max(answer, max_answer)
    return max_answer * 2
