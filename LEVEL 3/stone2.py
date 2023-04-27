# 코딩테스트 연습 / 2019 카카오 개발자 겨울 인턴십 / 징검다리 건너기
# 실패 
 
def solution(stones, k):
    
    start = 1
    end = max(stones)
    
    while start <= end:
        mid = (end+start) // 2
        
        cnt = 0
        for stone in stones:
            
            if stone <= mid:
                cnt += 1
            else:
                cnt = 0
            
            if cnt == k:
                break
        
        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
        
    return answer  
            