import sys

n = int(sys.stdin.readline())

seats_full = [0 for i in range(101)]
persons = sys.stdin.readline().split()

ans = 0

for person in persons:
    if seats_full[int(person)] == 0:
        seats_full[int(person)] =1
    else:
        ans+=1
print(ans)

