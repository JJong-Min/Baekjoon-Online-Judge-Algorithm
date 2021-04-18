import sys
arr = list(map(int, sys.stdin.readline().split()))

answer = [1, 2, 3, 4, 5]

while True:
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        print(arr[0], arr[1], arr[2], arr[3], arr[4])
        if arr == answer:
            break
        
    if arr[1] > arr[2]:
        arr[1], arr[2] = arr[2], arr[1]
        print(arr[0], arr[1], arr[2], arr[3], arr[4])
        if arr == answer:
            break
        
    if arr[2] > arr[3]:
        arr[2], arr[3] = arr[3], arr[2]
        print(arr[0], arr[1], arr[2], arr[3], arr[4])
        if arr == answer:
            break

    if arr[3] > arr[4]:
        arr[3], arr[4] = arr[4], arr[3]
        print(arr[0], arr[1], arr[2], arr[3], arr[4])
        if arr == answer:
            break
