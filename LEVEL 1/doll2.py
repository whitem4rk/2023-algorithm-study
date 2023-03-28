# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 크레인 인형뽑기 게임
# 실패 - out of range, 전치행렬

def solution(board, moves):
    board = list(map(list,zip(*board)))
    stack = []
    answer = 0
    
    for move in moves:
        for idx, doll in enumerate(board[move-1]):
            if doll != 0:
                stack.append(doll)
                board[move-1][idx] = 0
                if len(stack) != 1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    
    return answer
                