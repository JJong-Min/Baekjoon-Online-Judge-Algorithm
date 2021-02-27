input1 = input()
a = ord('A')
count = 0
for i in input1:
    b = abs(a - ord(i))
    c = abs(b-25)+1
    if b>=c:
        count += c
    else:
        count += b
    a = ord(i)
print(count)
