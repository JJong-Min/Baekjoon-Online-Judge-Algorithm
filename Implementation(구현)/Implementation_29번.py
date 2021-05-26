import sys

scores = []
for _ in range(10):
    scores.append(int(sys.stdin.readline()))
ans = 0
for score in scores:
    ans += score
    if ans >= 100:
        if ans - 100 > 100 - (ans-score):
            ans -= score

        break

print(ans)
            


        
