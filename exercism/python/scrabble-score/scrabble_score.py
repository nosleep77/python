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
