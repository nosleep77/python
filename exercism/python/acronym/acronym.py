import re
def abbreviate(words):
  pattern = r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9])?"
  return "".join([a[0] for a in re.findall(pattern, words.upper())])


# import re
# def abbreviate(words):
#     return ''.join([w[0].upper() for w in re.split(r'[ _-]+',words)])