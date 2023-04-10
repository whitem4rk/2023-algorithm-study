# 코딩테스트 연습 / 2018 KAKAO BLIND RECRUITMENT / [3차] 파일명 정렬
# 실패 - 문제 잘못읽음, 구현 못함

def solution(files):
    answer = []
    for file in files:
        numstart = -1
        numend = -1
        for idx, f in enumerate(file):
            if numstart == -1 and f.isdigit():
                numstart = idx
            elif numstart != -1 and not f.isdigit():
                numend = idx
                break
        if numend == -1:
            numend = len(file)
        answer.append([file[:numstart],file[numstart:numend],file[numend:]])
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(ans) for ans in answer]