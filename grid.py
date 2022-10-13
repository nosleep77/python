
grid = 20
x = int(grid / 2)
for i in range(x,0,-1):
  y = grid - i - i
  print(i * '*' + y * ' ')

for i in range(x):
  y = grid - i - i
  print(i * '*' + y * ' ')
  

'''
grid = 20
x = int(grid / 2)
for i in range(x,0,-1):
  y = grid - i - i
  print(i*'*' + y*' ' + i*'*')
'''

""" 
grid = 20
x = int(grid / 2)
for i in range(x):
  y = grid - i - i
  print(i*'*' + y*' ' + i*'*') 
"""

""" grid = 20
#a = []
x = int(grid / 2)
for i in range(x):
  y = grid - i - i
#  a[0:i] = '*'*i
#  a[-1:-i] = '*'*i
  #a[i+1:(-i)-1] = ' ' * y
#  a[i:-i] = ' ' * y
#  print(a)
#  a = [] 
  print(i*'*' + y*' ' + i*'*') """



'''
import requests
#r = requests.get('https://xkcd.com/353/')
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.headers)
'''