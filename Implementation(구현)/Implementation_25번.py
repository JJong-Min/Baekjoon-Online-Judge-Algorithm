import sys
x, y = sys.stdin.readline().split()
rev_x = ''
rev_y = ''
for i in range(len(x)-1, -1, -1):
    rev_x += x[i]


for i in range(len(y)-1, -1, -1):
    rev_y += y[i]


ans = str(int(rev_x) + int(rev_y))

rev_ans = ''

for i in range(len(ans)-1, -1, -1):
    rev_ans += ans[i]


print(int(rev_ans))
