def response(hey_bob):
  bob_alpha = "".join([x for x in hey_bob if x.isalpha()])

  if not bob_alpha.isupper() and len(hey_bob.rstrip()) > 0 and hey_bob.rstrip()[-1] == "?":
    return "Sure."
  elif bob_alpha.isupper() and hey_bob[-1] == "?":
    return "Calm down, I know what I'm doing!"
  elif hey_bob.isspace() or hey_bob =="":
    return "Fine. Be that way!"
  elif bob_alpha.isupper():
    return "Whoa, chill out!"
  else:
    return "Whatever."
