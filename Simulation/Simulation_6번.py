from collections import deque
import sys
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = list((map(int, input().split())))
    queue = deque(enumerate(arr))

    cnt = 0
    flag = -1
    answer = 0
    while queue:
        point = queue.popleft()
        if point[1] == max(arr):
            cnt +=1
            arr.remove(point[1])
            flag = point[0]

        else:
            queue.append(point)

        if point[0] == M:
            answer = cnt
        
    print(answer)
        
            
    
