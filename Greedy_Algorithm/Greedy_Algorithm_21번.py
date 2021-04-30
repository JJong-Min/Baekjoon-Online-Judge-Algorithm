import sys
N, L = map(int, sys.stdin.readline().split())
errors = list(map(int, sys.stdin.readline().split()))
errors.sort()
start = errors[0]
end = errors[0]+L
cnt = 1
for i in range(N):
    if start <= errors[i] < end:
        continue
    else:
        start = errors[i]
        end = errors[i] + L
        cnt += 1

print(cnt)
