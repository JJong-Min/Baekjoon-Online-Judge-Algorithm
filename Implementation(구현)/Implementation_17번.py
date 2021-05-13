import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))

    arr = sorted(arr, reverse = True)

    print(arr[2])
