n, k = map(int, input().split())
if n<(k*(k+1))/2:
    print(-1)
else:
    ball = n-((k*(k+1))/2)
    if ball % k == 0:
        print(k-1)
    else:
        print(k)

