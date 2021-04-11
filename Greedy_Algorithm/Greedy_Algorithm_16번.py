N= int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
answer = arr[-1]
num = len(arr)
for i in arr:
    answer = max((i*num), answer)
    num -= 1

print(answer)

