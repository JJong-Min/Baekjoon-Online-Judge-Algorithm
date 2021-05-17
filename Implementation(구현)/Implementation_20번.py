import sys

words = sys.stdin.readline().rstrip()

alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,\
            'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,\
            'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

            
words = words.upper()

for word in words:
    alphabet[word] += 1

max_list = [k for k, v in alphabet.items() if max(alphabet.values()) == v]

if len(max_list) > 1:
    print('?')

else:
    print(max_list[0])
