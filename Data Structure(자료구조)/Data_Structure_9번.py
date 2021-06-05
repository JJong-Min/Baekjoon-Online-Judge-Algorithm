#리스트가 아닌 딕셔너리 활용, 시간초과x
n = input()
res = dict()
for _ in range(int(n)):
    per, stat = input().split(" ")
    res[per] = stat

for i in sorted(res.keys(), reverse=True): 
	if res[i] == "enter": print(i)


# python3로는 시간초과, pypy3로는 통과
import sys

n = int(sys.stdin.readline())
person = []

for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        person.append(name)

    else:
        del person[person.index(name)]

person.sort(reverse = True)
for p in person:
    print(p)
