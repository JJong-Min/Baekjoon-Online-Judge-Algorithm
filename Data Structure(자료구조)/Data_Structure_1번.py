N = int(input())
participants = []
for i in range(N):
    participants.append(list(map(int, input().split())))

for idx in range(len(participants)):
    participants[idx].append(idx+1)

participants = sorted(participants, key = lambda x: (-x[0], x[1], x[2]))



print(participants[0][3])
