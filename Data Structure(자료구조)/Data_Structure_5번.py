import sys
n = int(sys.stdin.readline())

for i in range(n):
    case = sys.stdin.readline().split()
    case = ' '.join(case[::-1])

    print("Case #"+str(i+1)+":", case)
    
