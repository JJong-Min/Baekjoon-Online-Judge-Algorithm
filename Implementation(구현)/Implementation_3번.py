n = int(input())
list = []
for i in range(n):
    x,y=map(int, input().split())
    list.append((x,y))
for j in list:
    rank = 1
    for k in list:
        if j[0]<k[0] and j[1]<k[1]:
            rank += 1
    print(rank, end=' ')
