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

def change(a,loc): #바뀌어야할 방향에 따른 톱니바퀴 회전 
    if a==1: #시계 방향 회전
        gear_list[loc]=gear_list[loc][-1]+gear_list[loc]
        gear_list[loc]=gear_list[loc][:-1]
    elif a==-1: #시계반대 방향 회전
        gear_list[loc] = gear_list[loc]+gear_list[loc][0]
        gear_list[loc] = gear_list[loc][1:]
    else:
        pass

for i in loc_list:
    loc=i[0]
    dir=i[1]
    loc-=1
    go = [0, 0, 0, 0]#각 단계마다 톱니바퀴가 움직이는 방향
    go[loc]=dir
    tmp1=loc
    dir1=dir
    tmp2=loc
    dir2=dir

    while(tmp1<3): #톱니바퀴 위치를 기준으로 오른쪽 검사
        if gear_list[tmp1][2] != gear_list[tmp1+1][-2]:#현재 3시방향 톱니와 다음 톱니바퀴의 9시방향 톱니 비교
            go[tmp1+1]=-dir1 #다르기 때문에 현재 톱니바퀴의 방향과 반대
            dir1=-dir1
        else: #같기 때문에 검사종료
            break
        tmp1+=1

    while (tmp2 > 0):  #톱니바퀴 위치를 기준으로 왼쪽 검사
        if gear_list[tmp2][-2] != gear_list[tmp2 - 1][2] :#현재 9시방향 톱니와 이전 톱니바퀴의 3시방향 톱니 비교
            go[tmp2 - 1] = -dir2 #다르기 때문에 현재 톱니바퀴의 방향과 반대
            dir2 = -dir2 
        else: #같기 때문에 검사종료
            break
        tmp2 -= 1

    #바뀌어야할 톱니바퀴의 방향에 맞추어 톱니바퀴 회전
    for j in range(len(go)):
        change(go[j],j)

answer=0

for i in range(len(gear_list)):
    if gear_list[i][0]=='1':
        answer+=2**i
print(answer)
