# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [1차] 캐시
# 실패 - cachesize == 0 일때 고려 안함

from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            time += 5
    return time