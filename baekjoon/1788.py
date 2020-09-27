#피보나치수의 확장
#피보나치에 입력하는 수가 음수이면 (짝수 음수)일 때 결과는 음수// (음수 홀수) 음수일 때 결과 양수


b={}
b[0]=0
b[1]=1
#b[-1]=1
for n in range(2,1000001):
    b[n]=b[n-1]%1000000000+b[n-2]%1000000000


a=int(input())

if a>0:
    print(1)
    print(b[a] % 1000000000)
elif a==0:
    print(0)
    print(0)
else:
    if (-a)%2==0:
        print(-1)
        print(b[-a]%1000000000)
    else:
        print(1)
        print(b[-a]%1000000000)




