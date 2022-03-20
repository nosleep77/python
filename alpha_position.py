

def alphabet_position(text):
  sent = ""
  for a in text:
    if a.isalpha():
      sent = sent + " " + str(ord(a.lower()) - 96)
    else:
      continue
  return sent


print(alphabet_position("The sunset sets at twelve o' clock."))

## better version
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

