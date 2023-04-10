# 코딩테스트 연습 / Summer/Winter Coding(~2018) / 스킬트리
# 성공

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = deque(skill)
        answer += 1
        for t in tree:
            if t in tmp and t != tmp[0]:
                answer -= 1
                break
            elif t in tmp and t == tmp[0]:
                tmp.popleft()
    return answer