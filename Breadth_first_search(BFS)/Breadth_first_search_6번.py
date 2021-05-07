import sys
from collections import deque

def bfs(n):
    queue = deque()
    queue.append(n)
    visit = [0 for i in range(N+1)]
    visit[n] = 1

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[a] + 1
                queue.append(i)


N = int(sys.stdin.readline())
goal_x, goal_y = map(int, sys.stdin.readline().split())

M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
result = [0 for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


bfs(goal_x)

if result[goal_y] == 0:
    print(-1)
    
else: print(result[goal_y])
