def is_isogram(string):
  alpha_str = [char.lower() for char in string if char.isalpha()]

  return len(set(alpha_str)) == len(alpha_str)

  return True if  [alpha_str[b] for a in range(len(alpha_str)) 
   for b in range(len(alpha_str)) 
   if alpha_str[a] == alpha_str[b] and a != b] == [] else False

# print(is_isogram("isogram"))

#from collections import Counter
# def is_isogram(string):
#     counts = Counter(string.lower())
#     del counts[' ']
#     del counts['-']
#     return all(c < 2 for c in counts.values())

# def is_isogram(string):
#     isogram = False
#     s1 = [x for x in list(string.upper()) if x.isalpha()]
#     s2 = [x for x in set(string.upper()) if x.isalpha()]
#     if len(s1) == len(s2):
#         isogram = True
#     return isogram

# def is_isogram(string):
#     prepared_string = string.replace("-", "").replace(" ", "").lower()
#     return len(set(prepared_string)) == len(prepared_string)