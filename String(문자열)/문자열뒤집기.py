# 풀이 1
def reverseString1(s):
        left, right = 0, len(s)-1
        while left<right:
                s[left], s[right] = s[right], s[left]
                left +=1
                right-=1


# 풀이 2
def reverseString2(s):
        s.reverse()


# 풀이3
def reverseString3(s):
        s[:] = s[::-1]
        
s = ['a','b','c','d','e']
reverseString1(s)
print(s)

s = ['a','b','c','d','e']
reverseString2(s)
print(s)

s = ['a','b','c','d','e']
reverseString3(s)
print(s)
