import itertools
def solution(numbers):
    arr=itertools.combinations(numbers,2)
    answer = []
    for i in arr:
        i=list(i)
        num=i[0]+i[1]
        if num not in answer:
            answer.append(num)
    answer.sort()
    return answer
