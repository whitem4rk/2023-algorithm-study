# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 크레인 인형뽑기 게임


def solution(board, moves):
    answer = 0
    
    # 크레인으로 옮겨닮을 바구니
    basket = []
    # board transpose하고 0이 아닌값만 queue로 관리
    transpose = [ [] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                transpose[i].append(board[j][i])
                
    # crane 수행
    for move in moves:
        # 해당 열의 크기가 0이 아님을 확인
        if len(transpose[move-1]) != 0:
            crane = transpose[move-1].pop(0)
            basket.append(crane)
            # 바구니 크기가 2 이상임을 확인 / 상위 2개가 같을 시 삭제
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
            
    return answer


# test case / answer = 4
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
