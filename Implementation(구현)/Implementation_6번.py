k = int(input())
record = []
for _ in range(k):
    num = int(input())
    if num == 0:
        record.pop()
    else:
        record.append(num)

print(sum(record))
                        
                        
    
