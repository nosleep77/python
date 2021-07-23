
def convert(number):

  str1 = ""

  if number % 3 == 0:
    str1 += "Pling"
  if number % 5 == 0:
    str1 += "Plang"
  if number % 7 == 0:
    str1 += "Plong"

  if str1 == "":
    str1 = str(number)
  
  return str1



# numbers_to_check = {
#         3: 'Pling',
#         5: 'Plang',
#         7: 'Plong'
#     } # dict stored with its response when checked for factor

# def convert(number):
#     output = ''.join([value for key, value in numbers_to_check.items() if number % key == 0]) # gens list of outputs joined as a singular string to var
#     return str(output or number) # or checking on objects if both items are true always returns first object
#     # if first item eval to 0 returns second object if eval to 1