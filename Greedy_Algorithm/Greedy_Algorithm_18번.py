import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

answer = 0
for idx in range(N-1, 0, -1):
    if arr[idx] <= arr[idx-1]:
        answer += arr[idx-1] - arr[idx] + 1
        arr[idx-1] = arr[idx] - 1

print(answer)
    
