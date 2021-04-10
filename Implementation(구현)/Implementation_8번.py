E, S, M = map(int, input().split())
i = 1
while True:
    if (i-E) % 15 == 0 and (i-S) % 28 == 0 and (i-M) % 19 == 0:
        break
    else:
        i += 1
        

print(i)
        
# 중국인의 나머지 정리 이용
    # if i % 15 ==E and i % 28 ==S and i % 19==M일 때는 시간초과발
