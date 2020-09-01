#백준 MooTube
#bfs
#시간초과가 나는 이유를 못 찾겠다....
#인터넷에서 C++로 해결한 사람의 코드를 보았는데 알고리즘 로직이 비슷했다..ㅠ

N,Q=map(int,input().split(' '))
network=[[0]*N for i in range(N)]

for i in range(N-1):
    x,y,usado=map(int,input().split())
    network[x-1][y-1]=usado
    network[y-1][x-1]=usado

def min_usado(K,video):
    cnt=0
    queue=[video]
    visited={}
    visited.clear()
    visited[video]=0
    while queue:
        n=queue.pop(0)
        for i in range(N):
            if network[n-1][i] != 0 and i+1 not in visited.keys():
                queue.append(i+1)
                if visited[n]!=0:
                    visited[i+1]=min(network[n-1][i],visited[n])
                else:
                    visited[i+1]=network[n-1][i]

    for i in visited:
        if visited[i] >= K:
            cnt+=1

    return cnt

for i in range(Q):
    k,n=map(int,input().split(' '))
    print(min_usado(k,n))
