#공유기 설치
#
#공유기 설치 간격을 두고 
#공유기 설치 개수가 기준보다 많으면 공유기 설치 간격을 늘리고 반대는 줄인다. 

N,C=map(int,input().split())
house=[]
for i in range(N):
    house.append(int(input()))
house.sort()

left=1
right=house[-1]-house[0]
answer=0

def binary(mid):
    cnt = 1
    current_loc=house[0]
    for i in house:
        if current_loc+mid<=i:
            current_loc=i
            cnt+=1
    return cnt

while(left<=right):
    mid = (right + left) // 2
    tmp = binary(mid)
    if tmp<C:
        right=mid-1
    elif tmp>=C:
        answer=mid
        left=mid+1

print(answer)


