#유기농 배추키우기
#bfs

T= int(input())

for i in range(T):
    M,N,K=map(int,input().split())
    arr=[[0]*M for k in range(N)]

    queue=[]
    ans=0
    for j in range(K):
        x,y=map(int, input().split())
        arr[y][x]=1

    for k in range(N):

        for l in range(M):
            if arr[k][l]==1:
                queue.append([k,l])
                while(queue):
                    a=queue.pop()
                    arr[a[0]][a[1]] = 0

                    if a[0]>0:
                        if arr[a[0]-1][a[1]] == 1:
                            queue.append([a[0] - 1, a[1]])
                    if a[0]+1<N:
                        if arr[a[0]+1][a[1]] == 1:
                            queue.append([a[0] + 1, a[1]])

                    if a[1]>0:
                        if arr[a[0]][a[1] - 1] == 1:
                            queue.append([a[0], a[1] - 1])
                    if a[1]+1<M:
                        if arr[a[0]][a[1]+1]==1:
                            queue.append([a[0],a[1]+1])

                ans+=1
    print(ans)
