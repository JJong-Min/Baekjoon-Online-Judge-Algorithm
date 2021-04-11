N= int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = cost[0]*km[0]
min_cost = cost[0]
if min(cost) == cost[0]:
    answer = cost[0]*sum(km)
else:
    for i in range(1, len(cost)-1):
        if min_cost <= cost[i]:
            answer += min_cost*km[i]
        else:
            min_cost = cost[i]
            answer += min_cost*km[i]

print(answer)
    
