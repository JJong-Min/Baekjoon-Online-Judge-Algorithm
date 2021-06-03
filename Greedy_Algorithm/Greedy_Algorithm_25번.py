import sys

n = int(sys.stdin.readline())
first = map(int,sys.stdin.readline().split())
second = map(int,sys.stdin.readline().split())
first_,second_=0,0
for i in first:
    first_ += abs(i)
for i in second:
    second_ += abs(i)
print(first_+second_)
