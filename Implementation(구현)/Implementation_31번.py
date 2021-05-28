import sys
K = int(sys.stdin.readline())
fibonacci = [0] * (K + 1)
fibonacci[1] = 1

for i in range(2, K + 1):
    fibonacci[i] = fibonacci[i-1] +  fibonacci[i-2] 
print(fibonacci[K-1], fibonacci[K])




#시간 초과
'''
k = int(sys.stdin.readline())

words = 'A'


for i in range(k):
    new_words = ''
    for word in words:
        if word =='B':
            new_words += 'BA'
        else:
            new_words += 'B'

    words = new_words
    

print(words.count('A'), words.count('B'))

    
'''
