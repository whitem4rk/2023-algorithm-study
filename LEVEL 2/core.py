def solution(n, cores):
    
    if n <= len(cores):
        return n

    n -= len(cores)
    left = 1
    right = max(cores) * n
    while left < right:
        mid = (left + right) // 2
        count = 0
        for c in cores:
            count += mid // c
        
        if count >= n:
            right = mid
        elif count < n:
            left = mid + 1

    for c in cores:
        n -= (left-1) // c
    
    for i in range(len(cores)):
        if left % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1
    
    