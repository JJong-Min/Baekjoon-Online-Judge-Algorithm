n = int(input())
students = []
check = True

for i in range(3):
    x, y = map(int, input().split())
    students.append(x)
    students.append(y)

  
for i in range(students[0]+1):
    a = i
    d = students[0] - a
    e = students[5] - d
    b = students[2] - e
    c = students[1] - b
    f = students[4] - c
    
    if a>=0 and b>=0 and c>=0 and d>=0 and e>=0 and f>=0:
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        check = False
        break
        
if check:
    print(0)
