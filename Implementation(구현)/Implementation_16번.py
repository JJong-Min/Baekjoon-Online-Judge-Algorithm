# 정답 코드

import sys

n = int(sys.stdin.readline())

papers = [[0]*101 for _ in range(101)]

answer = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            papers[i][j] = 1


for paper in papers:
    answer += paper.count(1)

print(answer)


# 틀린 코드
'''
import sys

n = int(sys.stdin.readline())

papers = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    papers.append([x, y])

answer = 100 * n

for idx_1 in range(n):
    for idx_2 in range(n):
        if idx_1 == idx_2:
            continue
        if papers[idx_1][0] <= papers[idx_2][0] < papers[idx_1][0] + 10:
            answer -= (papers[idx_1][0] + 10 - papers[idx_2][0]) * \
                      (max(papers[idx_1][1],papers[idx_2][1]) - 
                       min(papers[idx_1][1], papers[idx_2][1]))
'''
