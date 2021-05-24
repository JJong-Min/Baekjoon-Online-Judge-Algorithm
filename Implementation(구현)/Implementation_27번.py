import sys

word = sys.stdin.readline().rstrip()

new_word =''
for i in range(len(word)-1,-1, -1):
    new_word += word[i]

if word == new_word:
    print(1)

else:
    print(0)


# 간결한 코드
'''
word = sys.stdin.readline().rstrip()

if word == word[::-1]:
    print(1)

else:
    print(0)

'''
