N = int(input())
cards = []
bin = []
for i in range(1, N+1):
    cards.append(i)

order = 0
while len(cards)>1:
    if order % 2 == 0:
        throw = cards.pop(0)
        bin.append(throw)
    else:
        throw = cards.pop(0)
        cards.append(throw)
    order += 1

for i in bin:
    print(i, end=' ')
print(cards[0])

