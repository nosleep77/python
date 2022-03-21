import re

atbash = "abcdefghijklmnopqrstuvwxyz"

def encode(plain_text):
  
  c = []
  
  plain_text = re.sub(r'\W+', '', plain_text).lower()

  for a in plain_text:
    if a not in atbash:
       c.append(a)
    for b in atbash:
      if a == b:
        c.append(atbash[::-1][atbash.index(b)])

  return (' ').join(re.findall('.{1,5}',"".join(c)))

def decode(ciphered_text):
    pass


print(encode("Testing,1 2 3, testing."))

