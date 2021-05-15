import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num = sorted(num)

for i in num:
    print(i)


