from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(n, m):
    queue = deque()
    queue.append([n,m])
    while queue:
        nn, mm = queue.popleft()
        for k in range(4):
            nx = nn + dx[k]
            ny = mm + dy[k]
            if 0<= nx <M and 0<=ny<N and graph[ny][nx] == 1:
                graph[ny][nx] = 0 
                queue.append([nx, ny])
            

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0]*M for g in range(N)]
    check = [[] for p in range(K)]
    for num in range(K):
        i, j = map(int, sys.stdin.readline().split())
        check[num].append(i)
        check[num].append(j)
        graph[j][i] = 1

    for ch in check:
        x, y = ch
        if graph[y][x] == 1:
            graph[y][x] = 0
            bfs(x, y)
            cnt += 1

    print(cnt)
        
