# 풀이 1
def removeDuplicateLetters(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))

    return ''
