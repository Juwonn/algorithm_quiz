gear1=input()
gear2=input()
gear3=input()
gear4=input()
gear_list=[gear1,gear2,gear3,gear4]
n=int(input())
loc_list=[]

for i in range(n):
    loc,dir=map(int,input().split())
    loc_list.append([loc,dir])

def change(a,loc):
    if a==1:
        gear_list[loc]=gear_list[loc][-1]+gear_list[loc]
        gear_list[loc]=gear_list[loc][:-1]
    elif a==-1:
        gear_list[loc] = gear_list[loc]+gear_list[loc][0]
        gear_list[loc] = gear_list[loc][1:]
    else:
        pass

for i in loc_list:
    loc=i[0]
    dir=i[1]
    loc-=1
    go = [0, 0, 0, 0]
    go[loc]=dir
    tmp1=loc
    dir1=dir
    tmp2=loc
    dir2=dir

    while(tmp1<3):
        if gear_list[tmp1][2] != gear_list[tmp1+1][-2]:
            go[tmp1+1]=-dir1
            dir1=-dir1
        else:
            break
        tmp1+=1

    while (tmp2 > 0):
        if gear_list[tmp2][-2] != gear_list[tmp2 - 1][2]:
            go[tmp2 - 1] = -dir2
            dir2 = -dir2
        else:
            break
        tmp2 -= 1

    for j in range(len(go)):
        change(go[j],j)

answer=0

for i in range(len(gear_list)):
    if gear_list[i][0]=='1':
        answer+=2**i
print(answer)
