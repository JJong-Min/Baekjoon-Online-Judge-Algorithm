N = str(input())
arr = []
for i in N:
   arr.append(int(i))

arr = sorted(arr, reverse = True)
for i in arr:
    print(i, end='')
