i = 1
while True:
    L, P, V = map(int, input().split())
    if L==0 and P==0and V==0: break
    else:
        count = 0
        count += (V//P)*L
        count += min(V%P, L)
        print('Case %d: %d' %(i, count))
        i += 1
