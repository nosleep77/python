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

    return self.number

  def pretty(self):
    num = self.getpnum(self.number)
    return "("+num[:3]+")-"+num[3:6]+"-"+num[6:]


