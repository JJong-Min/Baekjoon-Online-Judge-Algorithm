from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = [i for i in range(1, n+1)]
    
    q = deque([(1, 1, '1')])
    while q:
        current_sum, num_idx, ans = q.popleft()
        
        if num_idx == n:
            if current_sum == 0:
                print(ans)
                    
        else:
            number = numbers[num_idx]
            q.append((eval(''.join(list((ans+str(number)).split()))), num_idx +1, ans+' '+str(number)))
            q.append((current_sum+number, num_idx + 1, ans+'+'+str(number)))
            q.append((current_sum-number, num_idx + 1, ans+'-'+str(number)))
            

    print()
