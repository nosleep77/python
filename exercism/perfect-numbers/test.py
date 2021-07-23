num=int(input("enter a number "))
# factors=[]
# for i in range(1,num+1):
#     if num%i==0:
#        factors.append(i)
      
factors = [i for i in range(1,num+1) if num%i==0 ]

print ("Factors of {} = {}".format(num,factors[:-1]))