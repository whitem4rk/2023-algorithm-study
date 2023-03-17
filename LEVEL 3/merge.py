# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 표 병합

def solution(commands:list) -> list:
    answer = []
    table = [[''] * 51 for _ in range(51)]
    parent_table = [[(r, c) for c in range(51)] for r in range(51)]
    
    # union-find 부모찾기
    def find(r, c):
        if parent_table[r][c] == (r, c):
            return (r, c)
        else:
            p_r, p_c = parent_table[r][c]
            return find(p_r, p_c)
        
    
    for command in commands:
        cmd = command.split()
        if cmd[0] == "UPDATE":
            # 좌표값 변경
            if len(cmd) == 4:
                r, c, value = int(cmd[1]), int(cmd[2]), cmd[3]
                p_r, p_c = find(r,c)
                table[p_r][p_c] = value
            # 값 찾고 값 변경
            else:
                value1, value2 = cmd[1], cmd[2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if table[i][j] == value1:
                            table[i][j] = value2
                
        elif cmd[0] == 'MERGE':
            r1, c1, r2, c2 = int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4])
            pr1, pc1 = find(r1, c1)
            pr2, pc2 = find(r2, c2)
            
            # 이미 병합된 상태
            if (pr1, pc1) == (pr2, pc2):
                continue
            
            # (pr1, pc1)로 병합
            parent_table[pr2][pc2] = (pr1, pc1)
            if table[pr1][pc1] == '':
                table[pr1][pc1] = table[pr2][pc2]
            table[pr2][pc2] = ''
            
        elif cmd[0] == 'UNMERGE':
            r, c = int(cmd[1]), int(cmd[2])
            p_r, p_c = find(r, c)
            value = table[p_r][p_c]
            unmerged_list = []
            # 부모가 같은 것의 좌표 추출
            for i in range(1, 51):
                for j in range(1, 51):
                    cur_pr, cur_pc = find(i, j)
                    if (cur_pr, cur_pc) == (p_r, p_c):
                        unmerged_list.append((i,j))
            # 분해
            for i, j in unmerged_list:
                table[i][j] = ''
                parent_table[i][j] = (i,j)
            # r,c만 value    
            table[r][c] = value     
                    
        elif cmd[0] == 'PRINT':
            r, c = int(cmd[1]), int(cmd[2])
            r, c = find(r,c)
            if table[r][c] == '':
                answer.append("EMPTY")
            else:
                answer.append(table[r][c])
    
    return answer

answer = ["EMPTY", "group"]
my = solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
print(my)
print('correct') if answer == my else print('wrong')