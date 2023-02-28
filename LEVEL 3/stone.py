# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 징검다리 건너기

# 효율성 실패
# def solution(stones, k):
#     minimum = max(stones[:k])
#     for i in range(len(stones)-k+1):
#         tmp = max(stones[i:i+k])
#         minimum = min(minimum, tmp)
#     return minimum

def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    # 이진탐색으로 k칸이 0이되는 최소 answer를 찾는다
    while left <= right:
        mid = (left+right) // 2
        cnt = 0
        
        for stone in stones:
            if (stone-mid) <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                break
        
        if cnt < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    
    return answer


# test case 
answer = 3
my_answer = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
print(my_answer)
print('correct') if answer == my_answer else print('wrong')

