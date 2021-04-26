import sys
n=int(sys.stdin.readline())
if n%10!=0:
    print(-1)
else:
    print(n//300)
    n%=300
    print(n//60)
    n%=60
    print(n//10)
