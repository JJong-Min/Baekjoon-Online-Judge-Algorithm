n = int(input())
arr = [0 for _ in range(50000 + 1)]
for i in map(int, input().split()):
    arr[i] += 1
print(max(arr))


'''
# 오답코드
import sys
N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

answer = 0
cnt = 1
for idx in range(1, len(arr)):
    if arr[idx-1] == arr[idx]:
        cnt += 1
        answer = max(answer, cnt)
    else:
        cnt = 1

    

print(answer)
    
'''   
