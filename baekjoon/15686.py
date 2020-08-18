# 백준_치킨배달
# Brute force
# 그래프에서 치킨집과 집의 좌표를 배열에 저장 한다.
# 폐업시키지 않을 치킨집이 최대 M개 이므로
# M개의 좌표를 담은 치킨집의 조합 배열을 구한다. 조합은 itertools.combinations(list,n)을 사용한다.
# 각 조합마다 집과의 최소거리를 계산함.
# 반복문을 통해 최솟값을 구하는 문제이므로 초기 최솟값은 Python3 에서 정수의 최댓값인 sys.maxsize를 사용한다.

import itertools, sys

N,M=map(int,input().split())
house=[]
chicken=[]

for i in range(N):
    V=input().split(' ')
    for j in range(len(V)):
        if V[j]=='1':
            house.append([i,j])
        elif V[j]=='2':
            chicken.append([i,j])

chicken_comb=itertools.combinations(chicken,M)
answer=sys.maxsize

for i in chicken_comb:
    dis_list=[sys.maxsize for i in range(len(house))]
    for chic_loc in i:
        for house_loc in range(len(house)):
            dis=abs(house[house_loc][0]-chic_loc[0])+abs(house[house_loc][1]-chic_loc[1])
            if dis<dis_list[house_loc]:
                dis_list[house_loc]=dis
    tmp=sum(dis_list)
    if tmp<answer:
        answer=tmp
        
print(answer)
