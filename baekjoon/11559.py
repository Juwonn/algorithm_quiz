#뿌요뿌요
#bfs 사용

block=[[',',',',',',',',',',',',',',',']]
color=['R','G','B','P','Y']
answer=0

#블록 초기화
#배열 index 참조 오류를 피하기위해 ',' 문자로 블록 테두리를 둘러 쌓아줌

for i in range(12):
    tmp=[',']
    line=input()
    for i in line:
        tmp.append(i)
    tmp.append(',')
    block.append(tmp)
block.append([',',',',',',',',',',',',',',','])

#bfs 함수 
#블록의 위치를 읽을 때 위에서 아래로 읽으므로 현재 위치 기준에서 좌,우,하가 이어진 색깔인지 확인한다. 
#이어진 블록의 개수가 4개 이상이면 이어진 블록의 위치를 배열을 return 아니면 False return 

def bomb(puyo,loc):
    queue=[loc]
    visited=[loc]
    while(queue):
        p=queue.pop(0)
        
        #우
        if block[p[0]][p[1]+1]==puyo and [p[0],p[1]+1] not in visited:
            queue.append([p[0],p[1]+1])
            visited.append([p[0],p[1]+1])
        
        #좌
        if block[p[0]][p[1]-1]==puyo and [p[0],p[1]-1] not in visited:
            queue.append([p[0],p[1]-1])
            visited.append([p[0],p[1]-1])
        
        #하
        if block[p[0]+1][p[1]]==puyo and [p[0]+1,p[1]] not in visited:
            queue.append([p[0]+1,p[1]])
            visited.append([p[0]+1,p[1]])

    if len(visited)>=4:
        return visited
    else:
        return False

while(1):
    flag=0
    a=[]
    for i in range(13):
        for j in range(7):
            if block[i][j] in color:
                tmp=bomb(block[i][j],[i,j])
                if tmp is not False:
                    for k in tmp:
                        if k not in a:
                            a.append(k)
                    flag=1
            else:
                continue

    for i in a:
        for j in range(i[0],1,-1):
            block[j][i[1]]=block[j-1][i[1]]
        block[1][i[1]]='.'

    if flag==0:
        print(answer)
        break
    else:
        answer+=1
