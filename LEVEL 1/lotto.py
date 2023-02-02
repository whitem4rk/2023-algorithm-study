# 코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 로또의 최고순위와 최저순위

def solution(lottos, win_nums):
    answer = []
    
    # 확실한 정답개수 세기
    correct = 0
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
    
    # 0의 개수만큼 최고등수가 오름을 활용
    zero = lottos.count(0)
    # 6등=7등이므로 동일처리
    answer.append(min(7-correct-zero,6))
    answer.append(min(7-correct,6))
    
    return answer

# test case / answer = [3, 5]
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))