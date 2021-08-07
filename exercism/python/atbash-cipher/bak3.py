import re

atbash = [
  "abcdefghijklmnopqrstuvwxyz1234567890",
  "zyxwvutsrqponmlkjihgfedcba1234567890"
]

def encode(plain_text):
  
  plain_text = re.sub(r'\W+', '', plain_text).lower()
  c = [atbash[1][atbash[0].index(b)] for a in plain_text for b in atbash[0] if a == b]
  return (' ').join(re.findall('.{1,5}',"".join(c)))

def decode(ciphered_text):
  ciphered_text = ciphered_text.replace(' ','')
  return "".join([atbash[0][atbash[1].index(b)] for a in ciphered_text for b in atbash[1] if a == b])

print(decode("vc vix    r hn"))