N = int(input())
height = list(map(int, input().split()))

answer = 0
maxheight = 0
count = 0
for i in height:
    if i > maxheight:
        maxheight = i
        count = 0
    else:
        count+=1

    answer = max(answer, count)

print(answer)

