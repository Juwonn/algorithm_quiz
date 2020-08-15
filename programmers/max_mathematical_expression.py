#프로그래머스 카카오 2020 인턴십 수식 최대화
#리스트 사이에 값을 삽입 할때 슬라이싱 말고 insert(n,x) 사용
#배열 깊은 복사 x.copy() 아니면 같은 메모리 주소를 참조하게 된다.

import itertools

def solution(expression):
    def cal(numstk, opstk, priority):
        for i in priority:
            while i in opstk:
                for j in opstk:
                    if i == j:
                        idx = opstk.index(i)
                        op = opstk.pop(idx)
                        n1 = numstk.pop(idx)
                        n2 = numstk.pop(idx)
                        if op == '*':
                            n3 = int(n1) * int(n2)
                            numstk = numstk[:idx] + [n3] + numstk[idx:]
                        elif op == '-':
                            n3 = int(n1) - int(n2)
                            numstk = numstk[:idx] + [n3] + numstk[idx:]
                        else:
                            n3 = int(n1) + int(n2)
                            numstk = numstk[:idx] + [n3] + numstk[idx:]
        return abs(int(numstk[0]))

    operator = ['*', '-', '+']
    priority = itertools.permutations(operator, 3)
    priority = list(priority)
    numstk = []
    opstk = []
    num = ''
    expression += '*'

    for i in expression:
        if i in operator:
            opstk.append(i)
            numstk.append(num)
            num = ''
        else:
            num += i
    opstk.pop(-1)


    answer=0
    for j in range(len(priority)):
        a = numstk.copy()
        b = opstk.copy()
        n = cal(a,b,priority[j])
        if answer< n:
            answer=n
    return answer


