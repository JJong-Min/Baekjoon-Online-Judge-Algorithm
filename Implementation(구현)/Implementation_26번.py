import sys
n = int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(sys.stdin.readline().rstrip())

ans1 = 0
ans2 = 0

for i in range(n):
    cnt = 0
    for j in range(n):

        if graph[i][j] == '.':
            cnt += 1
        elif graph[i][j] == 'X' and cnt>=2:
            ans1 += 1
            cnt = 0

        else:
            cnt = 0

    if cnt >=2:
        ans1 += 1

    



for i in range(n):
    cnt = 0
    for j in range(n):
        
        if graph[j][i] == '.':
            cnt += 1

        elif (graph[j][i] == 'X' and cnt>=2):
            ans2 += 1
            cnt = 0
        else:
            cnt = 0

    if cnt >=2:
        ans2 += 1
print(ans1, ans2)
