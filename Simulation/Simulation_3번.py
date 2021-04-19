import sys
N1, N2 = sys.stdin.readline().split()
first_group = sys.stdin.readline().rstrip()
second_group = sys.stdin.readline().rstrip()
T = int(sys.stdin.readline())

answer = first_group[::-1]+second_group

if T == 0:
    print(answer)
else:
    for _ in range(T):
        idx_arr = []
        for idx in range(1, len(answer)):
            if answer[idx-1] in first_group and answer[idx] in second_group:
                idx_arr.append(idx)

        for i in idx_arr:
            answer = answer[:i-1] + answer[i] + answer[i-1] + answer[i+1:]

    print(answer)
