import sys
N = int(sys.stdin.readline())
participants = {}
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    if name in participants:
        participants[name] += 1
    else:
        participants[name] = 1
for _ in range(N-1):
    name = sys.stdin.readline().rstrip()
    participants[name] -= 1

for participant in participants:
    if participants[participant] == 1:
        print(participant)
        break
