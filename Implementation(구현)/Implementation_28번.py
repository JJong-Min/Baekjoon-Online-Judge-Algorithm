import sys

arr = []
max_len = 0
for i in range(5):
    arr.append(sys.stdin.readline().rstrip())
    max_len = max(max_len, len(arr[i]))


for i in range(max_len):
    for j in range(5):
        if len(arr[j]) <= i:
            continue
        else:
            print(arr[j][i], end='')


        
