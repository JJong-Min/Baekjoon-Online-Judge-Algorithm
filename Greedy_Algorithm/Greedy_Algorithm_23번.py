import sys

N, M = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

box_weight = 0
cnt = 1

if N:
    for i in range(N):
        book = books[i]
        if box_weight + book <= M:
            box_weight += book
        else:
            cnt += 1
            box_weight = book


else:
    cnt = 0
    
print(cnt)

    
    
# N(책의 갯수)가 0인 경우를 예외처리해야 한다!!
