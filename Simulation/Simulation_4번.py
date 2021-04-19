dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

R, C = map(int,input().split())
board = [[0]*C for _ in range(R)]
k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    board[a][b] = 1
sx,sy = map(int,input().split())
pos = list(map(int,input().split()))
visit = [[0]*C for _ in range(R)]
visit[sx][sy] = 1
cnt = 0
step = 0
while True:
    nx,ny = sx+dx[pos[cnt]],sy+dy[pos[cnt]]
    if 0<=nx<R and 0<=ny<C and not visit[nx][ny] and board[nx][ny] != 1:
        visit[nx][ny] = 1
        sx,sy = nx,ny
        step = 0
    else:
        step +=1
        cnt+=1
    if cnt>3:
        cnt = 0
    if step==4:
        break
print(sx,sy)
