# 코딩테스트 연습 / 2020 카카오 인턴십 / 키패드 누르기
# 성공

def solution(numbers, hand):
    answer = ''
    pad = [[1,4,7,-1],[2,5,8,0],[3,6,9,-1]]
    cur_left = (0,3)
    cur_right = (2,3)
    
    for num in numbers:
        if num in pad[0]:
            answer += 'L'
            cur_left = (0,pad[0].index(num))
        elif num in pad[2]:
            answer += 'R'
            cur_right = (2,pad[2].index(num))
        else:
            idx = pad[1].index(num)
            left_dist = abs(cur_left[0]-1) + abs(cur_left[1]-idx)
            right_dist = abs(cur_right[0]-1) + abs(cur_right[1]-idx)
            if left_dist < right_dist:
                cur_left = (1,idx)
                answer += 'L'
            elif right_dist < left_dist:
                cur_right = (1,idx)
                answer += 'R'
            else:
                if hand == 'left':
                    cur_left = (1,idx)
                    answer += 'L'
                else:
                    cur_right = (1,idx)
                    answer += 'R'
                                   
    return answer