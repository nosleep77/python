def find_anagrams(word, candidates):
  return [ a for a in candidates if sorted(a.lower()) == sorted(word.lower())
           if a.lower() != word.lower() ]