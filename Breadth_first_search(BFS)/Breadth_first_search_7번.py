from collections import deque
import sys

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        for j in graph[a]:
            if check[j] == False:
                queue.append(j)
                check[j] = True




N,M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
check = [False]*(N+1)

cnt = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    if check[i] == False:
        bfs(i)
        cnt += 1

print(cnt)
