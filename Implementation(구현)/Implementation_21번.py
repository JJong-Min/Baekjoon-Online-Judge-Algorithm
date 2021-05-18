import sys

x, y = map(int, sys.stdin.readline().split())

Day_of_the_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

answer_day = 1

for i in range(0, x):
    answer_day += days[i]

answer_day += y

answer = Day_of_the_week[(answer_day-1)%7]

print(answer)

