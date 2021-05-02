import sys

N = int(sys.stdin.readline())
people = []
for _ in range(N):
    people.append(input().split())

old_person = [people[0][0]]
young_person = [people[0][0]]

old_day = int(people[0][1])
old_month = int(people[0][2])
old_year = int(people[0][3])

young_day = int(people[0][1])
young_month = int(people[0][2])
young_year = int(people[0][3])


for idx in range(1, N):
    if int(people[idx][3]) > young_year:
        young_year = int(people[idx][3])
        young_day = int(people[idx][1])
        young_month = int(people[idx][2])
        young_person.pop()
        young_person.append(people[idx][0])
        
    elif int(people[idx][3]) == young_year:
        if int(people[idx][2]) > young_month:
            young_year = int(people[idx][3])
            young_day = int(people[idx][1])
            young_month = int(people[idx][2])
            young_person.pop()
            young_person.append(people[idx][0])

        elif int(people[idx][2]) == young_month and int(people[idx][1]) > young_day:
            young_year = int(people[idx][3])
            young_day = int(people[idx][1])
            young_month = int(people[idx][2])
            young_person.pop()
            young_person.append(people[idx][0])

    elif int(people[idx][3]) < old_year:
        old_year = int(people[idx][3])
        old_day = int(people[idx][1])
        old_month = int(people[idx][2])
        old_person.pop()
        old_person.append(people[idx][0])

    elif int(people[idx][3]) == old_year:
        if int(people[idx][2]) < old_month:
            old_year = int(people[idx][3])
            old_day = int(people[idx][1])
            old_month = int(people[idx][2])
            old_person.pop()
            old_person.append(people[idx][0])

        elif int(people[idx][2]) == old_month and int(people[idx][1]) < old_day:
            old_year = int(people[idx][3])
            old_day = int(people[idx][1])
            old_month = int(people[idx][2])
            old_person.pop()
            old_person.append(people[idx][0])


print(young_person[0])
print(old_person[0])
            
        
    
    
