#union find
#집합의 표현

#input vs sys.stdin.readline 
#입력의 수가 많다면 sys.stdin.readline 이 훨씬 빠르다

import sys
input = sys.stdin.readline

n,m=map(int,input().split(' '))
parent=[]

#초기화
for i in range(n+1):
    parent.append(i)


def find(x):
    if parent[x]==x:
        return x
    else:
        p=find(parent[x])
        parent[x] =p
        return p

def union(x,y):
    x=find(x)
    y=find(y)

    if x != y:
        parent[y]=x


answer=[]
for i in range(m):
    flag,x,y=map(int,input().split(' '))
    if flag == 0:
        union(x,y)
    else:
        if find(x) != find(y):
            answer.append('NO')
        else:
            answer.append('YES')

for i in answer:
    print(i)
