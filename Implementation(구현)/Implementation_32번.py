import sys
n, m = map(int, sys.stdin.readline().split())

a,b = sys.stdin.readline().split()

alphabet = {'A':'3', 'B':'2', 'C':'1', 'D':'2', 'E': '4', 'F':'3', 'G':'1', \
            'H':'3', 'I':'1', 'J':'1', 'K':'3', 'L':'1', 'M':'3', 'N': '2', \
            'O':'1', 'P':'2', 'Q':'2', 'R': '2', 'S':'1', 'T':'2', 'U': '1',\
            'V':'1', 'W': '1', 'X':'2', 'Y':'2', 'Z':'1'}

name = ''
prob = ''
if n<m:
    for i in range(n):
        name += alphabet[a[i]]
        name += alphabet[b[i]]
    for i in range(n,m):
        name += alphabet[b[i]]

elif n>m:
    for i in range(m):
        name += alphabet[a[i]]
        name += alphabet[b[i]]
    for i in range(m,n):
        name += alphabet[a[i]]


else:
    for i in range(n):
        name += alphabet[a[i]]
        name += alphabet[b[i]]

name = list(name)
for i in range(n+m-2):
    for j in range(len(name)-1):
        name[j] = (int(name[j]) + int(name[j+1]))%10
    name = name[:n+m-i-1]

print(str(((name[0]*10)+name[1])%100)+'%')
    

