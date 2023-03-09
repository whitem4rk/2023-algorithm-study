# 코딩테스트 연습 / 2021 카카오 채용연계형 인턴십 / 표 편집

# 다른 풀이에는 다 linked list로 구현되어있어서 원형 linked list로 구현했는데
# 자꾸 오답이라고한다.뭐가 문제인건지 모르겠다. (index -1값이 마지막 값임을 이용함)
def solution(n, k, cmd):
    table = ['O'] * n
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1,n)] + [-1]
    # down = [i for i in range(1,n)] + [0]
    clear_stack = []
    
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c.split()[1])):
                k = up[k]
        elif c[0] == 'D':
            for _ in range(int(c.split()[1])):
                k = down[k]
        elif c[0] == 'C':
            clear_stack.append(k)
            table[k] = 'X'
            ###############
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]
            
            # down[up[k]] = down[k]
            # up[down[k]] = up[k]
            ###############
            
            # # 마지막 행은 up 나머지는 down
            k = up[k] if down[k] == -1 else down[k]
                        
        elif c[0] == 'Z':
            pop_k = clear_stack.pop()
            table[pop_k] = 'O'
            ###############
            if up[pop_k] != -1:
                down[up[pop_k]] = pop_k
            if down[pop_k] != -1:
                up[down[pop_k]] = pop_k
                
            # down[up[pop_k]] = pop_k
            # up[down[pop_k]] = pop_k
            ###############
    return ''.join(table)

answer = "OOOOXOOO"
my = solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
print(my)
print('correct') if answer == my else print('wrong')
