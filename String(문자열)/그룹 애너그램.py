import collections
def Anagrams(strs):
    anagram_dict = collections.defaultdict(list)
    for i in strs:
        anagram_dict[''.join(sorted(i))].append(i)
    return anagram_dict.values()


lists = ["eat", 'tea', 'tan', 'ate', 'nat', 'bat']

print(Anagrams(lists))
