# 코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 로또의 최고 순위와 최저 순위
# 성공

def solution(lottos, win_nums):
    rank = {6:1, 5:2,4:3,3:4,2:5,1:6,0:6}
    max_correct = 0
    min_correct = 0
    for lotto in lottos:
        if lotto == 0:
            max_correct += 1
        elif lotto in win_nums:
            max_correct += 1
            min_correct += 1
            
    return [rank[max_correct],rank[min_correct]]