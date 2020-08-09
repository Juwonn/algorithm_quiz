def solution(skill, skill_trees):
    alphabet=[]
    answer=len(skill_trees)
    for i in skill:
        alphabet.append(i)
    
    for i in skill_trees:
        tmp=[]
        idx=[]
        for j in alphabet:
            idx.append(i.find(j))#
            
        for i in range(1,len(arr2)):
            #condition1:current index is not -1 and before index is bigger than current index
            #condition2: current index is not -1 and befor index is -1
            if (idx[i]!=-1 and idx[i-1]>idx[i]) or (idx[i-1]==-1 and idx[i]!=-1):
                answer-=1
                break
                       
    return answer
