#케빈 베이컨의 6단계 법칙
#BFS
 
N,M=map(int,input().split())
friend=[[0]*N for i in range(N)]
answer=[]

#friend 배열에 관계를 담는다
for i in range(M):
    x,y=map(int,input().split())
    friend[x-1][y-1]=1
    friend[y-1][x-1]=1

#N번째 사람의 케빈 베이컨의 수를 구하는 함수
def sol_step(K):
    queue = [K]
    visited = [K]
    while(queue):
        n=queue.pop(0)
        for i in range(N):
            if friend[n][i]==1 and i not in visited:
                queue.append(i)
                visited.append(i)
                K_step[i]=K_step[n]+1 
    return sum(K_step)

for i in range(N):
    K_step = [0 for j in range(N)]
    answer.append(sol_step(i))

print(answer.index(min(answer))+1)

