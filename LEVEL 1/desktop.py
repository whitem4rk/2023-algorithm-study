# 코딩테스트 연습 / 연습문제 / 바탕화면 정리
# 실패 - 문제조건 빠뜨림

def solution(wallpaper):
    row_len = len(wallpaper)
    col_len = len(wallpaper[0])
    
    start = [row_len-1, col_len-1]
    end = [0, 0]
    
    for i in range(row_len):
        for j in range (col_len):
            if wallpaper[i][j] == '#':
                start[0], start[1] = min(start[0], i), min(start[1], j)
                end[0], end[1] = max(end[0], i+1), max(end[1], j+1)
    
    return start+end