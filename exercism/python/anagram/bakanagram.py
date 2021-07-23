from re import findall


def find_anagrams(word, candidates):
  
  b=[]

  for a in candidates:
    if a.lower() == word.lower():
      continue
    if sorted(list(a.lower())) == sorted(list(word.lower())):
      b.append(a)
  return b

  #[ a for a in candidates if a.lower() != word.lower() if 

print(find_anagrams("Orchestra",["cashregister", "Carthorse", "radishes"]))