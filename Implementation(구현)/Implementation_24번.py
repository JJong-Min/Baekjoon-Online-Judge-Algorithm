import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

arr = [ i*i for i in range(1, 101)]

ans = []

for i in range(m, n+1):
    if i in arr:
        ans.append(i)


if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])

