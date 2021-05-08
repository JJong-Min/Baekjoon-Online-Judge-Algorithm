import sys

N = sys.stdin.readline().rstrip()

length = len(N)
answer = 0

for i in range(1, length):
    answer += (i*9*(10**(i-1)))
num = 10**(length-1)   
answer = answer + (length*(int(N)-num+1))

print(answer)

