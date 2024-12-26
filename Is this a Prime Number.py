outerrange= int(input("enter the outer range"))
innerrange=int(input("enter the inner range"))
for num in range(innerrange, outerrange + 1):
   if num > 1:
        for i in range(2, num):
           if(num % i) == 0:
            break

        else:
           print(num)