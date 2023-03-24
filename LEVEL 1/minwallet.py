# 코딩테스트 연습 / 완전탐색 / 최소직사각형
# 실패 - 아이디어 마저 생각못함...

def solution(sizes):
    max_list = []
    min_list = []
    
    for a, b in sizes:
        max_list.append(max(a,b))
        min_list.append(min(a,b))
    
    return max(max_list) * max(min_list)