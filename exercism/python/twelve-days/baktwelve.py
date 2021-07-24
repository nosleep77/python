def recite(start_verse, end_verse):

  days = {
    1: ["first", "a Partridge in a Pear Tree."],
    #2: ["second", "two Turtle Doves, "],
    2: ["second", "two Turtle Doves, and"],
    3: ["third", "three French Hens, "],
    4: ["fourth", "four Calling Birds, "],
    5: ["fifth", "five Gold Rings, "],
    6: ["sixth", "six Geese-a-Laying, "],
    7: ["seventh", "seven Swans-a-Swimming, "],
    8: ["eighth", "eight Maids-a-Milking, "],
    9: ["ninth", "nine Ladies Dancing, "],
    10: ["tenth", "ten Lords-a-Leaping, "],
    11: ["eleventh", "eleven Pipers Piping, "],
    12: ["twelfth", "twelve Drummers Drumming, "],
  }

  begin = startline(start_verse,days)
  if start_verse == end_verse:
    return [getlines(end_verse,days,begin)]

  else:
    complines = []
    for n in range(start_verse,end_verse+1):
      begin = startline(n,days)
      lines = getlines(n,days,begin)
      complines.append(lines)

    return complines

def startline(n,days):
  start = "On the "
  sent = " day of Christmas my true love gave to me: "
  return "".join([start, days[n][0], sent ])

def getlines(n,days,begin):
  joiner = "and "
  lines = []
  for a in range(n,1-1,-1):
    lines += days[a][1]
    # if a==2 and n>1:
    #   lines += joiner
  lines = "".join(lines)
  return "".join([begin, lines])
