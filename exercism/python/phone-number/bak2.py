class PhoneNumber:

  def __init__(self, number):
    self.number = number
    self.area_code = number[:3]
    self.getpnum(self.number)

  def getpnum(self, number):
    n = "".join([ a for a in number if a.isdecimal() ])
    self.number = n

    if len(n) < 10 or len(n) > 11:
      raise ValueError("incorrect length")

    if len(n) == 11 and (n[0] != "1" or int(n[1]) < 2 or int(n[4]) < 2):
      raise ValueError("something wrong. check area code, exchange code.")
    else:
      self.number = n.lstrip("1")

    if len(n) == 10 and (int(n[0]) < 2 or int(n[3]) < 2):
      raise ValueError("something wrong. check area code, exchange code.")

    return self.number

  def pretty(self):
    num = self.getpnum(self.number)
    return "("+num[:3]+")-"+num[3:6]+"-"+num[6:]








# import re
# class PhoneNumber:
#     REPLACES = ["+", "1", "(", ")", ".", "-", " "]
#     def __init__(self, number):
#         number = "".join([c for c in number if c not in PhoneNumber.REPLACES])
#         match = re.findall(r"^[1]?([2-9]\d{2}[2-9]\d{6}$)", number)

#         if match:
#             self.number = match[-1]
#         else:
#             raise ValueError("number malformed")
#     @property
#     def area_code(self):
#         return self.number[:3]
#     def pretty(self):
#         return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"