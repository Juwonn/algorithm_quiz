#달팽이는 올라가고 싶다.
#이분탐색 알고리즘으로 풀었으나 시간초과가 떴다.(1번 풀이)
#수학식으로 간단하게 풀수 있다.(2번 풀이)

# 1번 풀이

A,B,V=map(int,input().split())
left=1
right=V

while(left<right-1):
    mid=(left+right)//2
    days=0
    for i in range(mid):
        days+=A
        if days>=V:
            right=mid
            break
        days-=B
    if days<V:
        left = mid
print(left+1)

# 2번 풀이
import math

A,B,V = map(int,input().split())
print(math.ceil((V-A)/(A-B))+1)
