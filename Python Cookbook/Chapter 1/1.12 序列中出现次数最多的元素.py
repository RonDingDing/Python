
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]
print(word_counts['not'])
# 1
print(word_counts['eyes'])
# 8

####################################################################
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])
# 9


words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']
word_counts = Counter(words)
word_counts.update(morewords)
print(word_counts)
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2, 'around': 2,
#          "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})


######################################################################
a = Counter(words)
b = Counter(morewords)
print(a)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3,
#          'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
print(b)
# Counter({'why': 1, 'are': 1, 'you': 1, 'not': 1,
#          'looking': 1, 'in': 1, 'my': 1, 'eyes': 1})
c = a + b
print(c)
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2, 'around': 2,
#          "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})
d = a - b
print(d)
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2,
#          'around': 2, "don't": 1, "you're": 1, 'under': 1})
 
