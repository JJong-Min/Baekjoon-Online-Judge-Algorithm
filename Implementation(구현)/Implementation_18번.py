import sys

n = sys.stdin.readline().rstrip()

if int(n) < 10:
    new_n = n+n
else:
    back_num = int(n[0]) + int(n[1])
    new_n = n[-1] + str(back_num)[-1]


answer = 1

while True:
    if int(n) == int(new_n):
        break
    
    if int(new_n) < 10:
        new_n = new_n[-1]+new_n[-1]
    else:
        back_num = int(new_n[0]) + int(new_n[1])
        new_n = new_n[-1] + str(back_num)[-1]



    answer+=1

print(answer)
