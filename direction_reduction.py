def dirReduc(arr):

    dir = " ".join(arr)

    while "NORTH SOUTH" in dir or "SOUTH NORTH" in dir or "EAST WEST" in dir or "WEST EAST" in dir:
        dir = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
        dir = " ".join(dir.split())

    dir3 = dir.split()
    return dir3

plan = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(plan))