def isPalindrome(s):
        strs = []
        for i in s:
                if i.isalnum():
                        strs.append(i.lower())

        while len(strs)>1:
                if strs.pop(0) != strs.pop():
                        return False

        return True
