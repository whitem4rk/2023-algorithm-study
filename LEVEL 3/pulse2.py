def getSum(sequence, purse):
    cursum = sequence[0]
    cur = 0
    
    for x in sequence:
        purse *= -1
        x *= purse
        cur = max(x, cur+x)
        cursum = max(cursum, cur)
    return cursum

def solution(sequence):
    return max(getSum(sequence,-1), getSum(sequence,1))

