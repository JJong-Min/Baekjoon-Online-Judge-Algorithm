N = int(input())
arr = []
for i in range(N):
    arr.append(input())
arr = list(set(arr))
arr = sorted(arr, key = lambda x: (len(x), x))

for i in arr:
    print(i)
