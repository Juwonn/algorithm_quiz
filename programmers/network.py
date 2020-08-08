##############################
########프로그래머스##########
##########네트워크############
##############################
#######solved with bfs########
##############################

def bfs(a, computers):
    queue = [a]
    visited = []
    while queue:
        n = queue.pop()
        for i in range(len(computers)):
            if computers[n][i] == 1:
                if i in visited:
                    computers[n][i] = 0
                elif i not in visited:
                    visited.append(i)
                    queue.append(i)
                    computers[n][i] = 0
                    computers[i][n] = 0
    return visited

def solution(n, computers):
    node = []
    cnt = 0
    for i in range(len(computers)):
        if computers[i][i] == 1:
            node.append(i)

    for i in node:
        if len(bfs(i,computers))>=1:
            cnt+=1
    return cnt
