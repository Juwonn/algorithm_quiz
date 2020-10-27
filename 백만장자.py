n=int(input())
for i in range(n):
    a=input()
    arr=input().split(' ')
    for k in range(len(arr)):
        arr[k] = int(arr[k])

    tmp=arr[-1]
    buy=0

    for j in range(len(arr)-1,-1,-1):
        if arr[j]>tmp:
            tmp=arr[j]
        else:
            buy=buy+tmp-arr[j]
    print(f'#{i+1} {str(buy)}')
