def solution(n, lost, reserve):
    tmp=[]
    cnt=0
    lost.sort()
    reserve.sort()
    for i in reserve:
        if i in lost:
            tmp.append(i)
    for i in tmp:
        lost.remove(i)
        reserve.remove(i)
            
        
    for i in lost:
        if i-1 in reserve and i-1>0:
            reserve.pop(reserve.index(i-1))
            cnt+=1
            continue
        if i+1 in reserve and i+1<=n:
            reserve.pop(reserve.index(i+1))
            cnt+=1
            continue
    
            
    return n-len(lost)+cnt
