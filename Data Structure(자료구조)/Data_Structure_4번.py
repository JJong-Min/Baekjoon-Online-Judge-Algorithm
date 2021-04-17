import sys
N, M, K = map(int, sys.stdin.readline().split())

candidate_score = {}
for i in range(N):
    candidate_score[i+1] = 0

for i in range(M):
    genre = list(map(float, sys.stdin.readline().split()))
    for j in range(0, 2*N, 2):
        if genre[j+1] > candidate_score[genre[j]]:
            candidate_score[genre[j]] = genre[j+1]

score = sorted(list(candidate_score.values()), reverse=True)
answer = sum(score[:K])
print('%.1f' % answer)




# 틀린 코드
'''
import sys
N, M, K = map(int, sys.stdin.readline().split())
genres = []
answer = 0
num = []
for _ in range(M):
    genres.append(sys.stdin.readline().split())

new = [[] for _ in range(N*M)]
i = 0

for genre in genres:
    for o in range(len(genre)):
        if o % 2 == 1:
            continue
        else:
            new[i].append(int(genre[o]))
            new[i].append(float(genre[o+1]))
            i += 1

new = sorted(new, key = lambda x: x[1], reverse = True)
           
answer += new[0][1]
num.append(new[0][0])
cnt = 1

for i in range(1, len(new)):
    if new[i][0] in num:
        continue
    else:
        answer += new[i][1]
        num.append(new[i][0])
        cnt += 1

    if cnt == K:
        break
print(answer)
'''
