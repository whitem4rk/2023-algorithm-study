# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 튜플
# 실패

def solution(s):
    numlist = s[2:-2].split('},{')
    numlist.sort(key = lambda x: len(x))
    numset = set()
    answer = []
    for num in numlist:
        num = list(map(int, num.split(',')))
        for n in num:
            if n not in numset:
                numset.add(n)
                answer.append(n)
    return answer