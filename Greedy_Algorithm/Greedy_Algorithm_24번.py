import sys
strings = sys.stdin.readline().rstrip()

answer = 'UCPC'

cnt = 0

for i in strings:
    if i == answer[cnt]:
        cnt += 1

    if cnt == 4:
        break
    
if cnt == 4:
    print("I love UCPC")

else:
    print("I hate UCPC")
    

