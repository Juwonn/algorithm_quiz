#프로그래머스_2020_카카오_인턴십
#거리를 구하는 식에서 틀렸다.
#x**2와 math.sqrt(x) 는 항상 같은값을 반환하지 않음.
#아마도 부동소수점을 다른 방식으로 표현하거나 LSB 차이임.

def solution(numbers, hand):
    keypad=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    answer = ''
    currentL=[3,0]
    currentR=[3,2]
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            currentL=keypad[i]
        elif i in [3,6,9]:
            answer+='R'
            currentR=keypad[i]
        else:
            # disL=(currentL[0]-keypad[i][0])**2+(currentL[1]-keypad[i][1])**2
            # disR=(currentR[0]-keypad[i][0])**2+(currentR[1]-keypad[i][1])**2
            
            disL=abs(currentL[0]-keypad[i][0])+abs(currentL[1]-keypad[i][1])
            disR=abs(currentR[0]-keypad[i][0])+abs(currentR[1]-keypad[i][1])
            if disL<disR:
                answer+='L'
                currentL=keypad[i]
            elif disL>disR:
                answer+='R'
                currentR=keypad[i]
            else:
                if hand=="right":
                    answer+='R'
                    currentR=keypad[i]
                else:
                    answer+='L'
                    currentL=keypad[i]
    return answer
