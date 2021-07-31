SCORE = [
  [[1], ["a","e","i","o","u","l","n","r","s","t"]],
  [[2], ["d","g"]],
  [[3], ["b","c","m","p"]],
  [[4], ["f", "h", "v", "w", "y"]],
  [[5], ["k"]],
  [[8], ["j","x"]],
  [[10], ["q","z"]],
]

def score(word):
  return sum([ SCORE[b][0][0] for a in word for b in range(7) if a.lower() in SCORE[b][1] ])


## alternate solution
# compressed_scores = {1: "AEIOULNRST", 2: "DG",
#                      3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
# score_for = {char: score for score, chars in compressed_scores.items()
#              for char in chars}
# def score(word):
#     word = word.upper()
#     return sum(score_for[letter] for letter in word)

## alternate
# letters_to_scores = {
# 	k: v
# 	for keys, v in zip([["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], ["D", "G"], ["B", "C", "M", "P"], ["F", "H", "V", "W", "Y"], ["K"], ["J", "X"], ["Q", "Z"]], [1, 2, 3, 4, 5, 8, 10])
# 	for k in keys
# }