def convert_upper(f):
  print("convert_upper")


@convert_upper
def my_name():
    print("my_name")
    return my_name

f = my_name()
f()