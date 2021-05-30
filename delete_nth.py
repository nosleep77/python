def delete_nth(order,max_e):
  
    newList = []
    
    for a in order:
        if order.count(a) <= max_e:
            newList.append(a)
            
        else:
            for i in range(max_e):
                if newList.count(a) < max_e:
                    newList.append(a)
                    break
  
    return newList

print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3))

## better version
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans