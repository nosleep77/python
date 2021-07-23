import re
class PhoneNumber:

  def __init__(self, number):
    self.number = number
    self.area_code = number[:3]
    self.getpnum(self.number)

  def getpnum(self, number):
    n = "".join([ a for a in number if a.isdecimal() ])
    if len(n) == 11 and n[0] == "1":
      n = n.lstrip("1")
    self.number = n

    pattern = r"^[^0-1]\d\d[^0-1]\d{6}$"
    if not re.search(pattern, self.number):
      raise ValueError("something is wrong with ph num")

    # if len(n) < 10 or len(n) > 11:
    #   raise ValueError("incorrect length")

    # if len(n) == 11 and (n[0] != "1" or int(n[1]) < 2 or int(n[4]) < 2):
    #   raise ValueError("something wrong. check area code, exchange code.")

    # if len(n) == 10 and (int(n[0]) < 2 or int(n[3]) < 2):
    #   raise ValueError("something wrong. check area code, exchange code.")

    return self.number

  def pretty(self):
    num = self.getpnum(self.number)
    return "("+num[:3]+")-"+num[3:6]+"-"+num[6:]


