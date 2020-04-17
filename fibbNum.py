maxFib = int(input(" Enter max fibb number? "))

result, n1, n2 =0, 0, 1


# check if the number of terms is valid
if maxFib <= 0:
   print("Please enter a positive integer")
elif maxFib == 1:
   print("Fibonacci sequence up to",maxFib)
   print(n1)
else:
   print("Fibonacci sequence:")
   while n1 < maxFib:
     if n1 % 2 != 0 :
        result += n1;
     print(n1)
     nextNum = n1 + n2
     n1 = n2
     n2 = nextNum
print("the sum of the num is",result)
