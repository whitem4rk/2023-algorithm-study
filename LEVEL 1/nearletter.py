# 코딩테스트 연습 / 연습문제 / 가장 가까운 같은 글자
# 성공

def solution(s):
    answer = []
    char_dict = {}
    
    for idx, c in enumerate(s):
        if c not in char_dict:
            answer.append(-1)
        else:
            answer.append(idx - char_dict[c])
        char_dict[c] = idx
    return answer