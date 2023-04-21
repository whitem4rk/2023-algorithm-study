# 코딩테스트 연습 / 해시 /베스트앨범
# 실패 - 시간초과, 열추출

from collections import defaultdict

def solution(genres, plays):
    answer = []
    record = defaultdict()
    for gen, play,idx in zip(genres, plays,range(len(genres))):
        if gen not in record:
            record[gen] = []
        record[gen].append([idx,play])
    
    for k in record.keys():
        record[k].sort(key=lambda x:(-x[1],x[0]))
    genrerank = []
    
    for k in record.keys():
        genrerank.append([k, sum(list(zip(*record[k]))[1])])
    genrerank.sort(key = lambda x:(-x[1]))
    for genre, s in genrerank:
        answer.append(record[genre][0][0])
        if len(record[genre]) != 1:
            answer.append(record[genre][1][0])
    
    return answer