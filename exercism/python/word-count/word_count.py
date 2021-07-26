import re
from collections import Counter

def count_words(sentence):
  pattern = r"[a-z0-9]+(?:'[a-z0-9])?"
  return Counter(re.findall(pattern, sentence.lower()))


## alternate
# import re
# def count_words(sentence):
#     pat = re.compile(r"\d+|[a-z]+'[a-z]+|[a-z]+")
#     words = pat.findall(sentence.lower())
#     return {word: words.count(word) for word in words}

## alternate
# import re
# def count_words(sentence):
#     reg_expression = re.findall(r"[a-z0-9]+(?:'[a-z]+)?",sentence.lower())
#     return {num: reg_expression.count(num) for num in reg_expression}