# 코딩테스트 연습 / 2021 KAKAO BLIND RECRUITMENT / 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    
    # 메일받는 횟수 저장
    answer = [0] * len(id_list)
    # report를 당한 횟수 저장
    report_dict = {obj:0 for obj in id_list}
    
    # 중복 report를 제거한후, report 횟수 +1
    for obj in set(report):
        reporter, reported = obj.split()
        report_dict[reported] += 1
        
    # 다시 report를 순회하면서, 저장된 report 횟수가 k 보다 클 경우 신고자의 메일받는 횟수 +1
    for obj in set(report):
        reporter, reported = obj.split()
        if report_dict[reported] >= k:
            answer[id_list.index(reporter)] += 1
        
    return answer

# test case / answer = [2,1,1,0]
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))