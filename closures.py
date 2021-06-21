'''
def html_tag(tag):

  def wrap_text(msg):
    print('<{0}>{1}</{0}>'.format(tag, msg))

  def wrap_text2(msg):
    print('where is <{0}>{1}</{0}>'.format(tag, msg))

  return wrap_text2


print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_h1 = html_tag('p')
print_h1('Test Paragraph!')
'''

'''
def outer_func():

  message = 'Hi'

  def inner_func():
    print(message)


  # execute the function
  #return inner_func()
  
  # return the function
  return inner_func

f = outer_func()
#print(f.__name__)

f()
'''

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()

transmit_to_space("what is space")

