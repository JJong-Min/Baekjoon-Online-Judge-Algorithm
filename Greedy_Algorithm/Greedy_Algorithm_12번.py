n, w = map(int, input().split())
s = []
c = 0
for _ in range(n):
    s.append(input())
for index in range(len(s)-1):
    if int(s[index]) < int(s[index+1]):
        c += w//int(s[index])
        w %= int(s[index])
    if c>0 and (int(s[index]) > int(s[index+1])):
        w += c*int(s[index])
        c = 0      
if c>0:
    print(c*int(s[-1])+w)
else:
    print(w)
                       
    
