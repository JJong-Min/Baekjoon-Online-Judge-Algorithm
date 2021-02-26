T = int(input())
C_list = []
for _ in range(T):
    C_list.append(int(input()))
for c in C_list:
    coin = [25, 10, 5, 1]
    for i in coin:
        count = 0
        count += c//i
        c %= i
        print(count, end=' ')
    print()
