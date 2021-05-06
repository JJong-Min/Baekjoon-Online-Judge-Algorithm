from collections import deque
import sys

dx = [1, 2, 1, 2, -1, -2, -1, -2]
dy = [-2, -1, 2, 1, -2, -1, 2, 1]
T = int(sys.stdin.readline())


def bfs(x, y, end_x, end_y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return graph[x][y] - 1
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<i and 0<=ny<i and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])




for t in range(T):
    i = int(sys.stdin.readline())
    graph = [[0]*i for _ in range(i)]

    x, y = map(int, sys.stdin.readline().split())
    
    goal_x, goal_y = map(int, sys.stdin.readline().split())

    if x == goal_x and y == goal_y:
        print(0)
        continue

    print(bfs(x,y, goal_x, goal_y))

