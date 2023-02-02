# 코딩테스트 연습 / 2020 카카오 인턴십 / 키패드 누르기


def solution(numbers, hand):
    answer = ''
    
    # 초기값 설정 / 리스트의 인덱스를 활용할것
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    left_list = [(0,3)]
    right_list = [(2,3)]
    
    for number in numbers:
        # number가 왼쪽에 위치할때
        if number in keypad[0]:
            left_list.append((0,keypad[0].index(number)))
            answer += 'L'
        # number가 오른쪽에 위치할때
        elif number in keypad[2]:
            right_list.append((2,keypad[2].index(number)))
            answer += 'R'
        # # number가 중앙에 위치할때
        else:
            cur_idx = (1,keypad[1].index(number))
            recent_left = left_list[-1]
            recent_right = right_list[-1]
            # 손가락에서 number까지의 거리는 x,y값의 차이값
            left_distance = abs(cur_idx[0]-recent_left[0]) + abs(cur_idx[1]-recent_left[1])
            right_distance = abs(cur_idx[0]-recent_right[0]) + abs(cur_idx[1]-recent_right[1])
            
            # 더 거리가 짧은 손가락 위치이동
            if right_distance > left_distance:
                left_list.append(cur_idx)
                answer += 'L'
            elif right_distance < left_distance:
                right_list.append(cur_idx)
                answer += 'R'
            # 두 개의 거리가 값다면 오른/왼손잡이에 따라 결정
            else:
                if hand == 'right':
                    right_list.append(cur_idx)
                    answer += 'R'
                else: 
                    left_list.append(cur_idx)
                    answer += 'L'
    
    return answer

# test case / answer = 'LRLLLRLLRRL'
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))