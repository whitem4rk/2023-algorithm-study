# 코딩테스트 연습 / 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 다단계 칫솔 판매
# 실패 - 최적화

from collections import defaultdict

treedict = defaultdict(str)
treedict['-'] = ''
selldict = defaultdict(list)
selldict['-'] = []
def solution(enroll, referral, seller, amount):
    for en, ref in zip(enroll, referral):
        selldict[en] = []
        treedict[en] = ref
            
    for sell, amo in zip(seller,amount):
        amo *= 100
        if not treedict[sell]:
            selldict[sell].append(amo)
            continue 
        while treedict[sell]:
            if amo == 0:
                break
            parentcash = amo // 10
            amo = amo - parentcash
            
            selldict[sell].append(amo)
            sell = treedict[sell]
            
            amo = parentcash
    del selldict['-']
    return [sum(v) for v in selldict.values()]