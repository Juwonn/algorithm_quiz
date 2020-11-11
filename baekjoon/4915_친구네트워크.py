#

def find(x):
    if parent[x]==x:
        return x
    else:
        p=find(parent[x])
        parent[x]=p
        return p

def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        parent[y]=x
        number[x]+=number[y]

N=int(input())
for k in range(N):
    n=int(input())
    parent = {}
    number = {}
    for i in range(n):
        cnt = 0
        a,b=map(str,input().split(' '))
        if a not in parent:
            parent[a]=a
            number[a]=1
        if b not in parent:
            parent[b]=b
            number[b]=1

        union(a,b)
        print(parent)
        print(number)
        print(number[find(parent[a])])
