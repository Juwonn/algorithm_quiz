#연산자 끼워넣기
#연산자를 나타내는 숫자 입력을 문자열로 변환해서 배열에 쌓는다.
#순열을 사용해 나올수 있는 연산자의 경우의 수를 구하고 중복제거를 통해 같은 연산자의 중복을 제거한다.
#중복 제거를 하지 않으면 시간초과 남
#결과값을 배열에 담아 min(),max() 함수 사용 후 출력
import itertools
N=int(input())
num=input().split(' ')
num=[int(i) for i in num]
operator=input().split(' ')
op_char=['+','-','*','/']
op_list=[]
result=[]

for i in range(len(operator)):
    for j in range(int(operator[i])):
        op_list.append(op_char[i])

op_list=set(itertools.permutations(op_list,len(op_list)))

for i in op_list:
    i=list(i)
    num_cp = num.copy()
    tmp=num_cp.pop(0)
    for op in i:
        n=num_cp.pop(0)
        if op =='*':
            tmp=tmp*n
        elif op =='/':
            if tmp<0:
                tmp=abs(tmp)
                tmp = tmp // n
                tmp=tmp*(-1)
            else:
                tmp = tmp // n
        elif op =='+':
            tmp=tmp+n
        else:
            tmp=tmp-n

    result.append(tmp)
print(max(result))
print(min(result))



