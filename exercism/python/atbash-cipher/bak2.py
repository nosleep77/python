import re

atbash = [
  "abcdefghijklmnopqrstuvwxyz1234567890",
  "zyxwvutsrqponmlkjihgfedcba1234567890"
]

def encode(plain_text):
  
  c = []
  
  plain_text = re.sub(r'\W+', '', plain_text).lower()

  # for a in plain_text:
  #   for b in atbash[0]:
  #     if a == b:
  #       c.append(atbash[1][atbash[0].index(b)])

  c = [atbash[1][atbash[0].index(b)] for a in plain_text for b in atbash[0] if a == b]

  return (' ').join(re.findall('.{1,5}',"".join(c)))

def decode(ciphered_text):
    pass


print(encode("Testing,1 2 3, testing."))