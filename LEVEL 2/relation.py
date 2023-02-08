# 코딩테스트 연습/ 2019 KAKAO BLIND RECRUITMENT / 후보키
from itertools import combinations

def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    
    # column을 뽑을 수 있는 모든 경우의수
    comb = []
    for i in range(1, col+1):
        comb.extend(combinations(range(col), i)) 
    
    # 각각의 경우의 수로 모든 db tuple을 뽑은후 set으로 만들어 중복한 값이 있는지 확인
    candidate = []
    for c in comb:
        # 각각의 조합에서 
        tmp = [tuple(item[idx] for idx in c) for item in relation]
        if len(set(tmp)) == row:
            candidate.append(c)
    
    tmp = set(candidate)
    # 유일성은 만족했으므로 최소성이 만족하는지 확인
    for i in range(len(candidate)):
        for j in range(i+1, len(candidate)):
            if len(candidate[i]) == len(set(candidate[i]).intersection(set(candidate[j]))):
                tmp.discard(candidate[j])
    answer = len(tmp)
    return answer


# test case / answer = 2
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))