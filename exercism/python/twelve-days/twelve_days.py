def recite(start_verse, end_verse):

  days = {
    1: ["first", "a Partridge in a Pear Tree."],
    2: ["second", "two Turtle Doves, and "],
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

  return [getlines(n,days,startline(n,days)) for n in range(start_verse,end_verse+1)]

def startline(n,days):
   return f"On the {days[n][0]} day of Christmas my true love gave to me: "

def getlines(n,days,begin):
  return "".join([begin, "".join([days[a][1] for a in range(n,1-1,-1)])])


