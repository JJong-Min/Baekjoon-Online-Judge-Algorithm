import sys
#풀이 1
def maxProfit1(prices):
    answer = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer = max(answer, prices[j]-prices[i])

    return answer

#풀이 2
def maxProfit2(prices):
    answer = 0
    min_price = sys.maxsize
    for i in prices:
        min_price = min(min_price, i)
        answer = max(answer, i-min_price)
    return answer


prices = [7,1,5,3,6,4]
print(maxProfit1(prices))
print(maxProfit2(prices))
