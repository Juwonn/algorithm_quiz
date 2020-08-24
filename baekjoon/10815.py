#숫자 카드
#출력 형식을 똑같이 맞춰줘야 한다.
#가지고 있는 카드를 정렬한 후 이분탐색을 통해 카드를 가지고 있는지 체크한다.

N=int(input())
card=input().split()
M=int(input())
check=input().split()

card=[int(i) for i in card]
check=[int(i) for i in check]
card.sort()
answer=[]

for check_num in check:
    left = 0
    right = len(card) - 1
    while(left<right-1):
        mid = (left+right) // 2
        if card[mid]>check_num:
            right=mid
        else:
            left=mid

    if card[left]==check_num or card[right]==check_num:
        answer.append(1)
    else:
        answer.append(0)

for i in range(len(answer)-1):
    print(answer[i],end=' ')
print(answer[-1])
