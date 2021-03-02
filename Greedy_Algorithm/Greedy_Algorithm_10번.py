N, M = map(int, input().split())
cnt_block = 1
if N == 1:
    cnt_block = 1
elif N == 2:
    if (M >= 7):
        cnt_block = 4
    else:
        cnt_block = (M+1) // 2
elif N >= 3:
    if(M >= 7):
        cnt_block = (M - 2)
    elif(M >= 4):
        cnt_block = 4
    else:
        cnt_block = M

print(cnt_block)

