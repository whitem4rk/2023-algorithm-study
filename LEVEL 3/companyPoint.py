def solution(scores):
    
    wanho = scores[0]
    sortlist = sorted(scores, key=lambda x:(-x[0],x[1]))
    
    maxb = sortlist[0][1]
    goodlist = []
    for a,b in sortlist:
        if b >= maxb:
            goodlist.append([a,b])
            maxb = b
    
    if wanho not in goodlist:
        return -1

    sumlist = [x+y for idx,(x,y) in enumerate(goodlist)]
    sumlist.sort(reverse=True)
    return sumlist.index(sum(wanho))+1