# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 캐시

def solution(cacheSize, cities):
    answer = 0
    cache = []
    # 모든 city를 소문자로 변경
    low_cities = [obj.lower() for obj in cities]
    
    for city in low_cities:
        # hit일때 캐시안에 city 삭제
        if city in cache:
            cache.remove(city)
            answer += 1
        # miss일때 일단 진행
        else:
            answer += 5
        
        # city를 cache에 넣고 길이초과시(miss 일때) pop
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
            
    return answer


# test case / answer = 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))