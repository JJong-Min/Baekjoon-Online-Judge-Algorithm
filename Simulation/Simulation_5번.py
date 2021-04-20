from collections import deque
N, K, M = map(int, input().split())
queue = deque(i for i in range(1, N+1))
cnt = 0
while queue:
    if cnt//M % 2 == 0: 
        for _ in range(K-1):
            queue.append(queue.popleft())
    else:
        for _ in range(K):
            queue.appendleft(queue.pop())
    cnt += 1
    print(queue.popleft())
    
    
    
