def dirReduc(arr):

    dir = " ".join(arr)

    while 1:

        if "NORTH SOUTH" in dir or "SOUTH NORTH" in dir or "EAST WEST" in dir or "WEST EAST" in dir:
          dir = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
          dir = " ".join(dir.split())
        else:
          break

    dir3 = dir.split()
    return dir3

arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(arr))