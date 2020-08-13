##프로그래머스 124 나라의 숫자
##3진법 개념 사용
##2020 카카오톡 인턴 문제를 풀며 벽을 느끼고 쉬운문제부터 시작중..

def solution(n):
    answer = ''
    while(n!=0):
        remain=n%3
        n=n//3
        if remain ==1:
            answer+='1'
        elif remain ==2:
            answer+='2'
        else:
            n-=1
            answer+='4'
    answer=answer[::-1]
    return answer
