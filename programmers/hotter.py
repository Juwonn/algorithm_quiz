#프로그래머스 더 맵게
#python heapq 라이브러리 사용
#heap: 우선순위 큐와 개념이 비슷하며 완전 이진트리의 한 가지 종류이다.
#부모노드의 index가 n이라 했을 때 왼쪽 자식의 index는 2n 오른쪽 자식의 index는 2n+1 이다. 
#반대로 자식 입장에서 부모노드의 index는 n//2
#최대힙은 부모노드가 자식노드보다 값이 크도록 하며 최소힙은 그 반대이다.
#루트노드를 삭제할 때 가장 마지막 노드를 루트노드로 치환해 준다. 
#heapq.heappush(list,x)
#heapq.heappop(x)

import heapq

def solution(heap, K):
    cnt=0
    scoville=[]
    for i in heap:
        heapq.heappush(scoville,i)
        
    while(scoville[0]<K):  
        if len(scoville)==1:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        cnt=cnt+1
    return cnt
