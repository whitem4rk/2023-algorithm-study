# 코딩테스트 연습 / 2022 KAKAO BLIND RECRUITMENT / 신고 결과 받기
# 성공

def solution(id_list, report, k):
    table = [[0] * len(id_list) for _ in range(len(id_list))]
    report = set(report)
    
    id_dict = {}
    for idx, id in enumerate(id_list):
        id_dict[id] = idx
        
    
    for re in report:
        start, end = re.split()
        start, end = id_dict[start], id_dict[end]
        table[end][start] += 1
    
    mail_list = [0] * len(id_list)
    for i in range(len(id_list)):
        if sum(table[i]) >= k:
            for j in range(len(id_list)):
                if table[i][j] != 0:
                    mail_list[j] += 1
    
    return mail_list