def in_array(array1, array2):

  #newList = []
  #a = ""

  #return sorted(set(newList), key=str.lower)

  return sorted(set([a for a in array1 for b in array2 if a in b]))


a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1,a2))


'''
  for a in array1:
    for b in array2:
      if a in b:
        newList.append(a)
'''

#sorted(set([a for a in a1 for b in a2 if a in b]))