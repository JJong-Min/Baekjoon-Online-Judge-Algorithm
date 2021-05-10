A, B = map(int, input().split())
li = []
for i in range(1, 46):
    li += [i]*i
print(sum(li[A-1:B]))
