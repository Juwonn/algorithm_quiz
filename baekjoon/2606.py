#바이러스
#bfs

N=int(input())
pair_num=int(input())
pair=[]
network=[[0]*N for i in range(N)]
for i in range(pair_num):
    x,y=map(int,input().split(' '))
    network[x-1][y-1]=1
    network[y-1][x-1]=1

queue=[0]
visited=[0]
while queue:
    n=queue.pop(0)
    for i in range(N):
        if network[n][i]==1 and i not in visited:
            queue.append(i)
            visited.append(i)
print(len(visited)-1)

