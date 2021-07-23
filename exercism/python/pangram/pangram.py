def is_pangram(sentence):

  a = "abcdefghijklmnopqrstuvwxyz"
  b = ''.join(sorted(set(filter(lambda x: x.isalpha(), sentence.lower()))))

  x for x in sentence.lower()

  return True if a == b else False

sentence = "The quick brown fox jumps over the lazy dog."


[ x for x in sentence.lower() if x in a ]

[ True for x in sentence.lower() if x in a ]