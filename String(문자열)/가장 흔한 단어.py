import re
import collections
def commonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    
    return counts.most_common()[0][0]
                
                
para = "Aob hit a ball, the Aob BAll flew far after it was hit."
banned = ["hit"]

print(commonWord(para, banned))
        
