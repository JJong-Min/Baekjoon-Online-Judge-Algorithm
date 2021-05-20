import sys
n, k = map(int, sys.stdin.readline().split())

ans1 = 1
for i in range(k):
    ans1 *= (n-i)

ans2 = 1

for i in range(k):
    ans2 *= (k-i)

print(ans1//ans2)



# math 라이브러리 이용
'''
import math
a, b = map(int, input().split())
print(math.comb(a, b))
'''
