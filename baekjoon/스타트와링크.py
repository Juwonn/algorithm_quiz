import itertools, sys
N=int(input())
stat=[]
team=[i for i in range(N)]

for i in range(N):
    tmp=input().split()
    for i in range(len(tmp)):
        tmp[i]=int(tmp[i])
    stat.append(tmp)

team_list= list(itertools.combinations(team,N//2))
N=sys.maxsize

for i in range(len(team_list)//2):
    j=list(team_list[i])
    k=list(team_list[-i-1])
    a=0
    b=0
    for x in range(len(j)):
        for y in range(x+1,len(j)):
            a=a+stat[j[x]][j[y]]+stat[j[y]][j[x]]
            b=b+stat[k[x]][k[y]]+stat[k[y]][k[x]]
    if N>abs(a-b):
        N=abs(a-b)

print(N)
