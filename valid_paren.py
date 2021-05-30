def valid_parentheses(string):
    
    open = "("
    close = ")"
    newStr = string
    
    
    while open in newStr or close in newStr:

      if newStr == "":
        return True
    
      if newStr[0] == ")":
        return False    
    
      if newStr[-1] == "(":
        return False

      if open in newStr and not close in newStr:
        return False
      
      if close in newStr and not open in newStr:
        return False

      for a in newStr:
        if a == close:
          return False
        if a == open:
            b = newStr.find(a)       
            if close in newStr[b:]:
              newStr = newStr.replace(a, '', 1)
              newStr = newStr.replace(close, '', 1)
              break

            else:
                return False
        
    return True

        
print(valid_parentheses("gomge)hrp(gtvatsagi)(l(xsjex)a)rlyv(()nmynpl"))


## better version
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False