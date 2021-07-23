class PhoneNumber:

  def __init__(self, number):
    self.number = number
    self.area_code = number[:3]
    self.getpnum(self.number)

  def getpnum(self, number):
    n = "".join([ a for a in number if a.isdecimal() ])
    self.number = n

    if len(n) == 10 and (n[0] == "0" or n[0] == "1" or n[3] == "0" or n[3] == "1"):
      raise ValueError("something wrong")

    # if len(n) == 10:
    #   if n[0] == "0":
    #     raise ValueError("10-dig: area code cannot be 0")
    #   if n[0] == "1":
    #     raise ValueError("10-dig: area code cannot be 1")
    #   if n[3] == "0":
    #     raise ValueError("10-dig: exch code cannot be 0")
    #   if n[3] == "1":
    #     raise ValueError("10-dig: exch code cannot be 1")

    if len(n) == 11:
      if n[0] != "1":
        raise ValueError("11-dig: first num has to be 1")
      elif n[1] == "0":
        raise ValueError("11-dig: area code cannot be 0")
      elif n[1] == "1":
        raise ValueError("11-dig: area code cannot be 1")
      elif n[4] == "0":
        raise ValueError("11-dig: exch code cannot be 0")
      elif n[4] == "1":
        raise ValueError("11-dig: exch code cannot be 1")
      else:
        self.number = n.lstrip("1")

    if len(n) < 10:
      raise ValueError("min 10 digit phone num")

    if len(n) > 11:
      raise ValueError("max 11 digit phone num")

    return self.number

  def pretty(self):
    self.num = self.getpnum(self.number)
    num = self.num
    return "("+num[:3]+")-"+num[3:6]+"-"+num[6:]


number = PhoneNumber("12234567890")
print(number.pretty())

    # def test_pretty_print_with_full_us_phone_number(self):
    #     number = PhoneNumber("12234567890")
    #     self.assertEqual(number.pretty(), "(223)-456-7890")