while True:
    try:
        A, B, C = map(int, input().split())
        count = max(B-A, C-B)
        print(count-1)
    except:
        break
