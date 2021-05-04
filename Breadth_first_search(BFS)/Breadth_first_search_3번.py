from collections import deque
import sys

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(i, j):
    graph[i][j] = 0
    queue = deque()
    queue.append([i,j])
    while queue:
        x, y = queue.popleft()
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < H and ny >= 0 and ny < W and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
            
while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    graph = []

    for i in range(H):
        graph.append(list(map(int, input().split())))
    
    cnt = 0

    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
        
    
