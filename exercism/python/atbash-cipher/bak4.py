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



# import re
# from string import ascii_lowercase
# SECRET = dict(zip(ascii_lowercase, reversed(ascii_lowercase)))
# def encode(text, decode=False):
#     text = re.sub(r'[^a-z0-9]', '', text.lower())
#     res = ''.join(SECRET.get(i, i) for i in text)
#     return res if decode else ' '.join(re.findall(r'(\w{,5})', res)).strip()
# def decode(text): return encode(text, decode=True)



# from string import ascii_lowercase
# trans = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
# def translate_string(text):
# 	return ''.join([c for c in text if c.isalnum()]).lower().translate(trans)
# def encode(plain_text):
#     cipher = translate_string(plain_text)
#     return " ".join([cipher[i:i+5] for i in range(0, len(cipher), 5)])
# def decode(ciphered_text):
#     return translate_string(ciphered_text)


# from textwrap import wrap
# ALPHABET = "abcdefghijklmnopqrstuvwxyz"
# CIPHER = str.maketrans(ALPHABET, ALPHABET[::-1], ",. ")
# def encode(plain_text):
#     return " ".join(wrap(plain_text.lower().translate(CIPHER), 5))
# def decode(ciphered_text):
#     return ciphered_text.translate(CIPHER)