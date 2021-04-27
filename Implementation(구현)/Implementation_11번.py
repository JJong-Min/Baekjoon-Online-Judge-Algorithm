import sys
N=int(sys.stdin.readline())
students_number = []
for _ in range(N):
    students_number.append(sys.stdin.readline().rstrip())



answer = 0
length = len(students_number[0])


while True:
    check = []
    answer += 1
    idx = length-answer

    for student in students_number:
        new_number = student[idx:]
        if new_number not in check:
            check.append(new_number)
        else:
            continue


    if len(check) == N:
        break

        
print(answer)
    
