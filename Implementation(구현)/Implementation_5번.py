bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

answer = list(map(int, input().split()))
for _ in range(4):
    answer += list(map(int, input().split()))

check = [0] * 12 
bingo_count = 0
for n in range(25):
    if bingo_count == 3:
        break
    for i in range(5): 
        if bingo_count == 3:
            break
        for j in range(5):
            if bingo_count == 3:
                break
            if answer[n] == bingo[i][j]: 
                bingo[i][j] = 0 
                check[i] += 1 
                check[j+5] += 1 
                if i == j: 
                    check[10] += 1
                if i + j == 4: 
                    check[11] += 1
                for c in range(12):
                    if check[c] == 5: 
                        check[c] = 0 
                        bingo_count += 1
                        if bingo_count == 3:
                            break
print(n)
                    
                        
                        
    
