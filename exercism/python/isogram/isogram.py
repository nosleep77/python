def is_isogram(string):
  alpha_str = [char.lower() for char in string if char.isalpha()]
  return len(set(alpha_str)) == len(alpha_str)
