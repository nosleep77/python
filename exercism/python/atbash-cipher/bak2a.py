import re

atbash = [
  "abcdefghijklmnopqrstuvwxyz",
  "zyxwvutsrqponmlkjihgfedcba"
]

def encode(plain_text):
  
  c = []
  
  plain_text = re.sub(r'\W+', '', plain_text).lower()

  for a in plain_text:
    if a not in atbash[0]:
       c.append(a)
    for b in atbash[0]:
      if a == b:
        c.append(atbash[1][atbash[0].index(b)])

  return (' ').join(re.findall('.{1,5}',"".join(c)))

def decode(ciphered_text):
  ciphered_text = ciphered_text.replace(' ','')
  return "".join([atbash[0][atbash[1].index(b)] for a in ciphered_text for b in atbash[1] if a == b])


print(encode("Testing,1 2 3, testing."))