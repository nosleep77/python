'''
file operations
https://book.pythontips.com/en/latest/open_function.html

with open('photo.jpg', 'r+') as f:
    jpgdata = f.read()

If you want to read the file, pass in r
If you want to read and write the file, pass in r+
If you want to overwrite the file, pass in w
If you want to append to the file, pass in a
'''

with open('testfile.txt', 'a') as f:
  f.write("who are you\n")

