import itertools
arr=[]
def sol(user_id,banned_id):
    for j in range(len(user_id)):
            if len(user_id[j]) != len(banned_id[j]):
                return False
            else:
                for k in range(len(user_id[j])):
                    if banned_id[j][k]=='*':
                        continue
                    if banned_id[j][k]!=user_id[j][k]:
                        return False
    return True

def solution(user_id, banned_id):
    answer=[]
    for i in itertools.permutations(user_id,len(banned_id)):
        if sol(i,banned_id):
            i=set(i)
            if i not in answer:
                answer.append(i)
    
    return(len(answer))
            
                    
                        
            
